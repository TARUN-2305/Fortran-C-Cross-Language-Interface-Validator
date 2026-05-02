# Fortran to C Type Mapping Reference

The following outlines the baseline canonical mappings of Fortran 2003 `ISO_C_BINDING` constants to their C equivalents using the LP64 data model.

| Fortran ISO_C_BINDING | C Type | Base IR | Bytes |
| :--- | :--- | :--- | :--- |
| `c_int` | `int` | `integer` | 4 |
| `c_short` | `short` | `integer` | 2 |
| `c_long` | `long` | `integer` | 8 |
| `c_float` | `float` | `real` | 4 |
| `c_double` | `double` | `real` | 8 |
| `c_bool` | `_Bool` | `logical` | 1 |
| `c_float_complex` | `float _Complex` | `complex` | 4 |
| `c_ptr` | `void*` | `integer` (ptr) | 8 |

*Note: In ILP64 mode, `c_int` becomes 8 bytes.*
