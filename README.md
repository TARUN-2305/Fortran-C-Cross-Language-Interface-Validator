# FCValidator

**FCValidator** is a lightweight, Python-based static analysis tool designed to statically verify Fortran-C interoperability interfaces. It catches subtle stack-smashing bugs, ABI mismatches, and undefined behavior that compilers routinely ignore.

## Features
- **Zero-Compile Verification:** Uses Clang AST for C headers and an intelligent RegEx-based AST for Fortran to statically analyze interfaces without compiling the target codebase.
- **Strict ABI Compliance:** Validates data structures, struct padding, array shapes, string null-termination, and complex number semantics according to Fortran 2003 `ISO_C_BINDING` specifications.
- **Cross-Platform:** Detects platform-dependent data type sizing (`c_long`, `c_long_double`), Harvard architecture callback traps (`c_funptr`), and Windows calling conventions (`__stdcall` vs `__cdecl`).

## Installation

Ensure you have Python 3.10+ and `libclang` installed.

```bash
pip install -e .
```

## Usage

```bash
fcv validate path/to/interface.f90 path/to/header.h --platform lp64
```

Outputs an actionable report directly to the terminal, highlighting missing parameters, unaligned structs, and hidden string length argument mismatches.

## Test Suite
The tool includes an exhaustive suite of the "Hardest Test Cases" mimicking the exact ABI flaws that broke HPC libraries like LAPACK. Run the tests using:
```bash
pytest fcv/tests/test_hard_cases.py -v
```
