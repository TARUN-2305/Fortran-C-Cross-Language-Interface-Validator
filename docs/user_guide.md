# FCValidator User Guide

## Validating an Interface
To validate a Fortran `INTERFACE` against a C header file:
```bash
fcv validate src/interface.f90 include/header.h
```

## Options
* `--format [text|json|sarif]`: Default is `text`. `json` is useful for scripting, while `sarif` integrates directly into GitHub Security/Code Scanning dashboards.
* `--severity [info|warning|error]`: Filters the output. Default is `warning`.
* `--platform [lp64|ilp64]`: Specifies the target integer model.
    * `lp64`: `int` is 4 bytes, `long` is 8 bytes.
    * `ilp64`: `int` is 8 bytes, `long` is 8 bytes.
* `--use-flang`: Uses LLVM Flang parser (experimental) instead of the default RegEx heuristic parser for deeper Fortran AST integration.

## Common Warnings and Errors
* **Hidden CHARACTER length arg (ERROR)**: Passing a `CHARACTER(LEN=*)` into C. Fortran implicitly appends a size variable to the argument list. The C program doesn't expect it, corrupting the stack.
* **Scalar Size Mismatch (ERROR)**: Passing an 8-byte value into a 4-byte argument.
* **Value/Reference Mismatch (ERROR)**: Forgetting `VALUE` inside the Fortran declaration when C expects an unreferenced value.
