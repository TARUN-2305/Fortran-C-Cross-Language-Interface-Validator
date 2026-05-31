from typing import Tuple, Optional

# Base platform defaults for LP64
_BASE_MAPPINGS = {
    "c_int": ("integer", 4),
    "c_short": ("integer", 2),
    "c_long": ("integer", 8),
    "c_long_long": ("integer", 8),
    "c_signed_char": ("integer", 1),
    "c_size_t": ("integer", 8),
    "c_int8_t": ("integer", 1),
    "c_int16_t": ("integer", 2),
    "c_int32_t": ("integer", 4),
    "c_int64_t": ("integer", 8),
    "c_int_least8_t": ("integer", 1),
    "c_int_least16_t": ("integer", 2),
    "c_int_least32_t": ("integer", 4),
    "c_int_least64_t": ("integer", 8),
    "c_int_fast8_t": ("integer", 1),
    "c_int_fast16_t": ("integer", 2),
    "c_int_fast32_t": ("integer", 4),
    "c_int_fast64_t": ("integer", 8),
    "c_intmax_t": ("integer", 8),
    "c_intptr_t": ("integer", 8),
    "c_float": ("real", 4),
    "c_double": ("real", 8),
    "c_long_double": ("real", 16),
    "c_float_complex": ("complex", 4),
    "c_double_complex": ("complex", 8),
    "c_long_double_complex": ("complex", 16),
    "c_bool": ("logical", 1),
    "c_char": ("character", 1),
    "c_ptr": ("integer", 8),
    "c_funptr": ("integer", 8),
}

def get_fortran_iso_type(name: str, platform: str = "lp64") -> Optional[Tuple[str, int]]:
    """
    Returns (base_type, kind_bytes) for a given ISO_C_BINDING type name.
    Adjusts sizes based on the specified platform model.
    """
    name = name.lower()
    if name not in _BASE_MAPPINGS:
        return None

    base, kind = _BASE_MAPPINGS[name]
    
    if platform == "ilp64":
        if name == "c_int":
            return ("integer", 8)
        if name == "c_long":
            return ("integer", 8)
        if name == "c_size_t":
            return ("integer", 8)

    return base, kind

def get_c_type_mapping(c_type_name: str, platform: str = "lp64") -> Optional[Tuple[str, int]]:
    """
    Maps standard C type names directly to (base_type, size_in_bytes)
    """
    c_type_name = c_type_name.strip().replace(" ", "_")
    mapping = {
        "int": ("integer", 4 if platform != "ilp64" else 8),
        "short": ("integer", 2),
        "long": ("integer", 8),
        "long_long": ("integer", 8),
        "char": ("integer", 1),
        "signed_char": ("integer", 1),
        "unsigned_char": ("integer", 1),
        "size_t": ("integer", 8),
        "float": ("real", 4),
        "double": ("real", 8),
        "long_double": ("real", 16),
        "_Bool": ("logical", 1),
        "bool": ("logical", 1),
        "float__Complex": ("complex", 4),
        "_Complex_float": ("complex", 4),
        "double__Complex": ("complex", 8),
        "_Complex_double": ("complex", 8),
        "long_double__Complex": ("complex", 16),
        "_Complex_long_double": ("complex", 16),
    }
    
    return mapping.get(c_type_name)
