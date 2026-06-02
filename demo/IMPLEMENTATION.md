# IMPLEMENTATION.md — FEM Solver Interoperability and ABI Details

This document explains the technical implementation details of the interface boundaries between our web dashboard and the Fortran numerical engine, highlighting the compiler-level binary traps and how they are identified.

---

## 👥 Student Development Team & Credits
Developed as part of the Compiler Design Course Project:
* **Tanmay Dev D** (1RV23CS269) — CS Dept, RVCE  
* **Tarun.R** (1RV23CS271) — CS Dept, RVCE  
* **Tejasvi Vasant Hegde** (1RV23CS272) — CS Dept, RVCE  

---

## 1. The Legacy Name-Mangling Underscore (`compute_displacement_`)

In high-performance computing, when a Fortran subroutine is compiled without standard interoperability keywords, the compiler mangles the subroutine's symbol.
Specifically, **gfortran** converts all subroutine characters to lowercase and appends a trailing underscore:

```fortran
! Inside buggy/fem_solver.f90
SUBROUTINE COMPUTE_DISPLACEMENT(material, nx, ny, load, displacement)
```
Translates to the exported binary symbol:
$$\text{compute\_displacement\_}$$

For a C wrapper or dynamically loaded FFI engine (like `ctypes`) to call this, the programmer must explicitly declare and load the mangled symbol name:
```c
// Inside buggy/fem_wrapper.h
void compute_displacement_(char *material, long *nx, long *ny, double *load, double *displacement);
```

### The Security & Maintenance Risk:
If the Fortran library is recompiled on a different compiler (e.g., Intel `ifx` or Cray `ftn` under specialized settings) that does not append a single underscore, or appends two underscores, the C code fails to link. 
Modern **BIND(C)** completely eliminates this risk by instructing the compiler to preserve the exact character case and suppress any mangling:
```fortran
! Inside fixed/fem_solver.f90
subroutine compute_displacement(material, nx, ny, load, displacement) bind(c, name="compute_displacement")
```
Which binds exactly to the unmangled C symbol name:
$$\text{compute\_displacement}$$

---

## 2. The Hidden String Length Stack Shift

When passing a `CHARACTER(len=*)` variable to a legacy Fortran subroutine, the compiler must track the string's length at runtime. Because legacy Fortran does not use NUL-terminated strings (unlike C), the compiler silently appends a hidden `size_t` (8-byte on 64-bit platforms) argument to the end of the argument list:

### ⚠️ Buggy Memory Frame Call Stack
When the C wrapper invokes `compute_displacement_`, it expects to push exactly **5 arguments** to the CPU registers:

```
Registers (AMD64 ABI / Windows x64 ABI):
1. RCX: Pointer to material ("steel")
2. RDX: Pointer to nx (100)
3. R8:  Pointer to ny (100)
4. R9:  Pointer to load (5000.0)
5. [Stack Frame]: Pointer to displacement (output)
```

However, the legacy Fortran compiler compiles `compute_displacement_` expecting **6 arguments**:
```
Expected Arguments:
1. RCX: Pointer to material
2. RDX: Pointer to nx
3. R8:  Pointer to ny
4. R9:  Pointer to load
5. [Stack Frame]: Pointer to displacement
6. [Stack Frame]: Hidden size_t length of material (implicitly appended!)
```

Because C is unaware of the 6th parameter, it does not push the string length. The Fortran engine, attempting to read the 6th argument, reads random stack garbage. Under standard optimization flags, this register mismatch corrupts the stack frame pointer and immediately triggers a segmentation fault or a memory read overflow.

### Modern BIND(C) Resolution:
Under `BIND(C)`, passing an array of `character(kind=c_char)` prevents the compiler from appending the hidden string length, converting it to a standard, interoperable C-style string address pointer:
```fortran
character(kind=c_char), dimension(*), intent(in) :: material
```

---

## 3. LP64 Pointer Size Discrepancies (4-Byte vs 8-Byte Shifts)

On a modern 64-bit Linux HPC system (`LP64` data model), standard pointers are **8 bytes**, and a C `long` variable is **8 bytes**. However, a default Fortran `INTEGER` is **4 bytes**.

In our buggy wrapper, the grid parameters `nx` and `ny` are declared as:
```c
// C Header
long *nx, long *ny; // 8-byte pointer to 8-byte integers
```
But in the legacy Fortran subroutine, they are processed as:
```fortran
! Fortran Core
INTEGER :: nx, ny   // 4-byte scalar integers passed by reference
```

```
C side:      [ 8 bytes of long (value: 100) ]  <-- Address passed
Fortran:     [ 4 bytes read ]  [ 4 bytes offset ]
```

When Fortran attempts to dereference the 8-byte pointer passed by C, it reads only the first **4 bytes** from the address. If the value fits in 4 bytes and is little-endian, it reads `100` correctly. However, when returning or accessing adjacent stack variables, the 8-byte pointer boundary causes a 32-bit shift in memory layout. This shift displaces the pointer address of the subsequent argument `load`, causing the solver to read memory noise and return the corrupted displacement: `9234872139823.15 m`.

### BIND(C) Resolution:
The fixed interface maps the scalars explicitly using the `ISO_C_BINDING` parameters, passed by value to fit directly into CPU registers:
```fortran
integer(c_int), value :: nx, ny
```

---

## 4. Dynamic Loading and Ctypes FFI Mapping in `app.py`

The Flask application (`demo_app/app.py`) loads these compiled dynamic libraries using Python's standard `ctypes` foreign function interface.

### The Dynamic Symbol Loading:
```python
# app.py parameter binding snippet
import ctypes

# 1. Loading the DLL
lib = ctypes.CDLL("./demo_app/libfem_solver_fixed.dll")

# 2. Binding parameter types for the fixed BIND(C) interface
lib.compute_displacement.argtypes = [
    ctypes.c_char_p,                 # const char* material
    ctypes.c_int,                    # int nx (passed by value)
    ctypes.c_int,                    # int ny (passed by value)
    ctypes.c_double,                 # double load (passed by value)
    ctypes.POINTER(ctypes.c_double)  # double* displacement (output)
]
```

By explicitly mapping parameter types under the fixed mode, Python passes the arguments in standard register layouts:
- `material` is passed as a NUL-terminated C string (`c_char_p`).
- `nx` and `ny` are passed as 4-byte standard integers by value (`c_int`), matching the `integer(c_int), value` definition in Fortran.
- `displacement` is passed as an output double-precision pointer, retrieving the final calculation cleanly.
