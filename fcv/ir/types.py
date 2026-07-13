from dataclasses import dataclass
from typing import Union, List, Tuple, Any

@dataclass
class ScalarType:
    base: str          # "integer", "real", "complex", "logical", "character"
    kind_bytes: int    # 4, 8, etc.
    is_pointer: bool = False
    is_value: bool = False     # Fortran VALUE attribute / C pass-by-value
    is_optional: bool = False
    iso_name: str = None       # e.g. "c_long", "c_int"
    pointer_depth: int = 0     # e.g. 1 for *, 2 for **
    is_const: bool = False
    is_unsigned: bool = False

    def __post_init__(self):
        if self.pointer_depth > 0:
            self.is_pointer = True

@dataclass
class ArrayType:
    element: ScalarType
    rank: int
    shape: List[Union[int, None]]   # None = assumed-size/deferred
    is_assumed_shape: bool = False
    is_optional: bool = False

@dataclass
class StructType:
    name: str
    fields: List[Tuple[str, Any, int]]   # (field_name, type, offset_bytes)
    size_bytes: int = 0
    alignment: int = 1
    is_bind_c: bool = False
    is_optional: bool = False

@dataclass
class FunctionPointerType:
    return_type: Any
    params: List[Tuple[str, Any]]
    is_optional: bool = False

AnyType = Union[ScalarType, ArrayType, StructType, FunctionPointerType]

@dataclass
class InterfaceProc:
    name: str                  # binding name (lowercase, no underscore mangling)
    source_file: str
    source_line: int
    return_type: Union[AnyType, None]
    params: List[Tuple[str, AnyType]]   # (param_name, type)
    has_hidden_strlen: bool = False    # detected hidden CHARACTER length arg
    is_function: bool = False # Needed to distinguish SUBROUTINE from FUNCTION
