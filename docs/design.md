# FCValidator Design Document

## Architecture Overview
The `fcvalidator` tool operates on an Intermediate Representation (IR) derived independently from a Fortran parser and a C parser. 

1. **Parsers**: We have two distinct parsers. The Fortran parser uses RegEx heuristics, targeting standard `BIND(C)` interface blocks and `MODULE` structures. The C parser uses `libclang` to achieve compiler-grade precision of C header structs, functions, and definitions.
2. **Intermediate Representation**: Both parsers output a language-neutral structure (`fcv.ir.types.InterfaceProc`), where all variables and types are mapped to their fundamental baseline (Base Type, Kind Bytes, Is Pointer, Is Value, ISO Name).
3. **Comparator Engine**: Compares the two IR streams structurally using strict type-based logic rather than fuzzy string matching.
4. **ABI Engine**: Catches deeper platform-specific logic like Windows calling conventions and column-major array orientation.

## The Type Mapping Strategy
Instead of relying on fuzzy string matching heuristics (e.g. `c_int` == `int`), the tool aggressively maps everything down to bytes via the standard `ISO_C_BINDING` table and strictly matches `iso_name` metadata.
- `INTEGER(c_int)` -> Base: `integer`, Bytes: 4
- `long` (on lp64) -> Base: `integer`, Bytes: 8
When the Comparator sees `integer:4` vs `integer:8`, it throws a deterministic error. It also understands platform specific traps like `type(c_funptr)` vs `type(c_ptr)`.
