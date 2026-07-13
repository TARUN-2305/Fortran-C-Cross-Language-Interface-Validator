# FCValidator (Fortran-C Cross-Language Interface Validator) CLI User Guide

`fcv` is a command-line interface (CLI) tool powered by compiler frontends (**LLVM Flang** and **Clang/libclang**) to parse, analyze, and cross-validate type compatibility, parameter passing, and memory layouts across the Fortran-C language boundary.

---

## 🚀 Setting Up the One-Word command (`fcv`)

To run the validator directly with the single word `fcv` from any location, you must activate the python virtual environment where the package is installed:

```bash
# 1. Provision the environment (installs compilers, libclang and dependencies)
./build.sh

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Use fcv directly!
fcv --help
```

---

## 📖 CLI Reference (`--help`)

### `fcv --help`
```text
Usage: fcv [OPTIONS] COMMAND [ARGS]...

  Fortran-C Cross-Language Interface Validator

Options:
  --help  Show this message and exit.

Commands:
  validate  Validate a Fortran interface against a C header.
  version   Show version info
```

### `fcv validate --help`
```text
Usage: fcv validate [OPTIONS] FORTRAN_FILE C_HEADER

  Validate a Fortran interface against a C header.

Options:
  --format [text|json|sarif]      Output format
  --severity [error|warning|info]
                                  Minimum severity to report
  --platform [lp64|ilp64|llp64]   Integer size model
  --use-flang                     Use Flang for parsing
  --no-color                      Disable terminal colors
  --cflags TEXT                   Additional C compiler preprocessor flags
                                  (e.g. -I/path -DNAME)
  --c-prefix TEXT                 C function prefix
  --c-suffix TEXT                 C function suffix
  --f-prefix TEXT                 Fortran function prefix
  --f-suffix TEXT                 Fortran function suffix
  --name-map TEXT                 Comma-separated name mapping in format
                                  key=value,key2=value2
  --help                          Show this message and exit.
```

---

## 💡 Common Invocation Examples

### 1. Basic Validation
Cross-validate modern BIND(C) definitions in `interface.f90` against prototypes in `header.h`:
```bash
fcv validate interface.f90 header.h
```

### 2. Passing C Preprocessor Macros & Includes
For headers requiring macro definitions (e.g. integer widths) or include search paths, use the `--cflags` option:
```bash
fcv validate dgetrf.f lapack.h --cflags "-Dlapack_int=int -I/usr/include"
```

### 3. Procedure Name Mapping and Suffix Stripping
If your C header declares Fortran ABI wrapper functions mangled with an underscore (e.g. `dgetrf_` in C vs `dgetrf` in Fortran), use the `--c-suffix` option to strip the suffix and match them:
```bash
fcv validate dgetrf.f lapack.h --c-suffix "_"
```

Alternatively, map custom mismatched names manually using `--name-map`:
```bash
fcv validate solver.f90 wrappers.h --name-map "F_SOLVE=c_solver_bridge"
```

### 4. Machine-Readable Outputs (JSON/SARIF)
Generate a JSON report for custom scripting or a SARIF report to integrate with GitHub Code Scanning:
```bash
fcv validate interface.f90 header.h --format json > report.json
```

---

## 🔬 Common Diagnostic Rules

The comparison engine flags the following cross-language discrepancies:
1. **Scalar Size Mismatch (ERROR)**: Passing a type of mismatched width (e.g., 4-byte `int` in C vs 8-byte `REAL*8` in Fortran).
2. **Value/Reference Mismatch (ERROR)**: Forgetting the `VALUE` attribute in Fortran for scalar variables passed by value in C.
3. **Pointer Depth Mismatch (ERROR)**: Mismatched pointer indirection level (e.g., `float**` in C vs a simple reference parameter in Fortran).
4. **Hidden CHARACTER length arg (ERROR)**: Passing non-BIND(C) assumed-length `CHARACTER(*)` strings which implicitly append length parameters to the end of the argument list, corrupting the stack.
5. **Array Descriptor Mismatch (ERROR)**: Mapping an assumed-shape Fortran array (`dimension(:,:)`) to a raw C pointer, which bypasses the required `CFI_cdesc_t` descriptor structure.

