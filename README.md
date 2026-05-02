# FCValidator: Fortran-C Cross-Language Interface Validator

## The Problem: The "Silent Data Corruption" Crisis in HPC
When writing high-performance computing (HPC) software (like LAPACK, BLAS, or modern scientific simulations), developers frequently mix Fortran for numerical heavy-lifting with C/C++ for networking, memory management, and system-level operations. 

To bridge the gap between these languages, developers use Fortran's `BIND(C)` interoperability standard. However, **compilers do not verify cross-language interfaces**. If a Fortran subroutine expects an 8-byte `INTEGER` but the C header provides a 4-byte `int`, the compiler will happily link them. At runtime, this results in silent stack corruption, segmented faults, or subtle mathematical inaccuracies that can invalidate months of scientific computation without ever throwing an error.

Common catastrophic mismatches include:
* **The "Hidden String Length" Trap:** Fortran strings implicitly append length variables to the end of argument lists. C functions unaware of this will corrupt the stack when Fortran attempts to write to that length variable.
* **Array Memory Layout:** Fortran represents 2D arrays in Column-Major order, while C uses Row-Major order. Accessing `a[i][j]` in C directly maps to `a(i, j)` in Fortran, causing silent transposition errors.
* **Platform-Dependent Traps:** `long` is 4 bytes on Windows 64-bit, but 8 bytes on Linux/macOS. Hardcoding interfaces to `long` causes cross-platform crashes.
* **Harvard Architecture Pointer Traps:** Mixing up data pointers (`c_ptr`) and instruction pointers (`c_funptr`) will cause immediate hardware-level segfaults on modern architectures like Apple ARM64 (M-series chips).

## What Purpose It Serves
**FCValidator** solves this problem by acting as a strict, static analysis gatekeeper. It reads your Fortran interface and your C header file, translates them into a normalized Intermediate Representation (IR), and statically validates that every single parameter, return type, struct padding, and pointer aligns perfectly at the binary/ABI level.

It does this **without needing to compile the code**. It is designed to be fast, lightweight, and capable of catching the 36 hardest ABI edge-cases known to break mixed-language systems.

## Features
- **Zero-Compile Verification:** Uses Clang AST for C headers and an intelligent RegEx-based AST for Fortran to statically analyze interfaces.
- **Strict ABI Compliance:** Validates data structures, struct padding, array shapes, string null-termination, and complex number semantics according to Fortran 2003 `ISO_C_BINDING` specifications.
- **Dynamic Type Engine:** Instead of brittle string matching, it aggressively maps everything down to fundamental bytes (`integer:4`, `complex:16`) via the `ISO_C_BINDING` table, throwing deterministic errors when ABIs fracture.

## Installation

Ensure you have Python 3.10+ and `libclang` installed on your system.

```bash
pip install -e .
```

## How to Use

The tool operates via a simple Command Line Interface (CLI). You provide it the path to your Fortran interface file and the corresponding C header.

```bash
fcv validate src/interface.f90 include/header.h --platform lp64
```

### Options:
* `--platform`: Specify the target integer model. `lp64` (Linux/macOS defaults where `long` is 8 bytes) or `ilp64` (specialized 64-bit integer models).
* `--format`: Output format. `text` (default console output), `json` (for scripting pipelines), or `sarif` (for GitHub Security Code Scanning).
* `--severity`: Filter the output by `info`, `warning`, or `error`. Default is `warning`.

### Example Output
If you pass an 8-byte pointer to a 4-byte integer, the tool will output an actionable error directly to the terminal:
```
ERROR   [my_routine] interface.f90 <-> header.h
  Scalar type mismatch: Parameter 'size' base type mismatch: Fortran integer (8 bytes) vs C integer (4 bytes)
```

## Test Suite
The tool includes an exhaustive suite of the "Hardest Test Cases" mimicking the exact ABI flaws that broke HPC libraries like LAPACK. Run the tests using:
```bash
pytest fcv/tests/test_hard_cases.py -v
```
