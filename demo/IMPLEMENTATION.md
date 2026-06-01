# IMPLEMENTATION.md — LLVM Clang AST Parsing & Fortran Heuristics

This document describes the technical implementation details of **FCValidator**, specifically detailing the compiler frontends, AST traversal, parser pipelines, and validation logic.

---

## 1. C Parser: Clang Compiler AST Integration (`libclang`)

The C Parser (`fcv/parsers/c_parser.py`) integrates directly with LLVM's compiler frontend via the official **Clang Python Bindings (`libclang`)**. This enables production-grade C validation, supporting all compiler macros, system headers, and typedef chains.

### Compilation Database & AST Extraction
Instead of reading code as raw text, Clang compiles the header into a Translation Unit (TU) AST. The C parser performs the following:

```python
import clang.cindex as cl

# Initialize Clang Index
index = cl.Index.create()

# Compile the target header file to an AST
# Target standard C11 and define necessary standard directives
tu = index.parse(
    filepath,
    args=['-x', 'c', '-std=c11', '-D__STDC_LIMIT_MACROS', '-D__STDC_CONSTANT_MACROS']
)
```

### Traversing AST Nodes (Cursors)
The parser performs a depth-first pre-order traversal of the compiled AST, selecting specific node cursors to reconstruct function and struct signatures:

- **`CursorKind.FUNCTION_DECL`**: Marks the declaration of a function. The parser extracts:
  - Function name (e.g., `dgemm_`).
  - Return type.
  - Full ordered argument list.
  - Source location (file, line number).
- **`CursorKind.PARM_DECL`**: Represents an individual function parameter.
- **`CursorKind.STRUCT_DECL`**: Marks structural record declarations.
- **`CursorKind.FIELD_DECL`**: Identifies struct member declarations, enabling byte-offset and order alignment checks.

### Typedef Resolution Chain
A critical advantage of using `libclang` is the automatic traversal of typedef chains. The tool resolves deep definitions like:
`lapack_int` ⟶ `int32_t` ⟶ `int` ⟶ `4 bytes`
This is achieved by accessing Clang's canonical type representation:
```python
# Automatically resolves typedefs to underlying canonical types
canonical_type = cursor.type.get_canonical()
```

---

## 2. Fortran Parser: RegEx + Logical Line Reconstruction

Because Fortran parser tools (like Flang AST parsers) require massive toolchain installations, the Fortran Parser (`fcv/parsers/fortran_parser.py`) implements a high-performance **logical-line RegEx parser** designed to process standard Fortran `BIND(C)` interface blocks with near 100% accuracy.

### Parser Stages:
1. **Case Normalization**: Downcases all source text since Fortran is case-insensitive (excluding character string literals).
2. **Comment Stripping**: Removes all single-line comments prefixed by `!` (while preserving literal quotes).
3. **Continuation Joining**: Scans for the `&` line-continuation symbol and joins multi-line declarations into continuous single logical lines.
4. **Interface Extraction**: Extracts blocks starting with `interface` and ending with `end interface`.
5. **Procedure Matching**: Scans for `subroutine` or `function` declarations containing `bind(c)`.
6. **Type and Attribute Resolution**: Scans each variable declaration inside the block for attributes:
   - `value` attribute $\longrightarrow$ Pass-by-value.
   - `intent(in/out/inout)` $\longrightarrow$ Parameter flow direction.
   - `dimension` or arrays (`(..)` or `(*)`) $\longrightarrow$ Array pointers.
   - `iso_c_binding` constants (e.g., `c_int`, `c_double`) $\longrightarrow$ Standard ISO-C map.

---

## 3. Mismatch Detection Algorithms

The **Comparator Engine** (`fcv/engine/comparator.py`) and the **ABI Analysis Engine** (`fcv/engine/abi.py`) compare the parsed IR structures to isolate incompatibilities.

### Case A: Hidden String Length (ABI Danger)
In standard Fortran (non-`BIND(C)`), passing a `CHARACTER(LEN=*)` variable causes the compiler to implicitly append an extra integer argument representing the string's length at the end of the argument list. The C program is unaware of this, causing a call-stack mismatch and application crash.
- **Detection**:
  ```python
  if is_fortran_character_string and not is_bind_c:
      # Append hidden parameters to the IR proc list and trigger ERROR
  ```

### Case B: Scalar Width & Type Mismatches
Verifies that parameter widths match precisely.
- **Detection**:
  ```python
  if f_param.type.bytes != c_param.type.bytes:
      self._add_mismatch(
          category="TYPE_WIDTH",
          severity="ERROR",
          message=f"Width mismatch: Fortran {f_param.name} ({f_param.type.bytes}B) vs C {c_param.name} ({c_param.type.bytes}B)"
      )
  ```

### Case C: Value vs Reference Attributes
For standard scalar parameters, C passes variables by value by default, whereas Fortran passes by reference (pointer) unless the `VALUE` attribute is explicitly specified.

---

## 4. The Assumed-Shape Array Descriptor Trap (`CFI_cdesc_t`)

When a Fortran interface defines an assumed-shape array (e.g., `real :: x(:)`), the compiler does not pass a raw address. Instead, it passes a descriptor structure defined by the modern ISO C Interoperability standard (`ISO_Fortran_binding.h`):

```c
/* ISO_Fortran_binding.h equivalent representation */
typedef struct CFI_cdesc_t {
    void *base_addr;           // Raw pointer to array start
    size_t elem_len;           // Size of an element in bytes
    int version;               // CFI_VERSION
    CFI_attribute_t attribute; // Assumed, allocatable, or pointer
    CFI_type_t type;           // Element type code
    CFI_rank_t rank;           // Dimensions
    CFI_dim_t dim[];           // Bounds info (rank elements)
} CFI_cdesc_t;
```

A C function expecting a simple `double*` will read this structure as raw float data, causing a segmentation fault.

FCValidator detects this in the **Comparator Engine** by analyzing the rank specification:
```python
if isinstance(ft, ArrayType) and ft.is_assumed_shape:
    if not isinstance(ct, StructType) or "CFI_cdesc_t" not in ct.name:
        self._add_mismatch(
            category="ARRAY_DESCRIPTOR",
            severity="ERROR",
            message="Fortran assumed-shape passes CFI_cdesc_t descriptor. C header must receive CFI_cdesc_t*."
        )
```

---

## 5. Case D: Complex Return Call-Stack ABI
Functions returning `COMPLEX` values are returned differently depending on compiler ABI:
- **Direct Return**: Returned via standard registers (e.g. `xmm0/xmm1` on x86_64).
- **Structure Return (`sret`)**: The compiler silently inserts an implicit first parameter (the `sret` pointer) representing the return address of the structure, shifting all actual parameter positions by one.
FCValidator flags complex returns lacking the `BIND(C)` attribute to protect developers from call-stack displacement.
