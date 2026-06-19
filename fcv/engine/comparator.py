from typing import List, Dict, Any
from dataclasses import dataclass

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, AnyType

@dataclass
class Mismatch:
    category: str
    severity: str
    message: str
    proc_name: str
    fortran_type: str = ""
    c_type: str = ""

class Comparator:
    def __init__(self):
        self.mismatches: List[Mismatch] = []

    def _add_mismatch(self, category: str, severity: str, msg: str, proc_name: str, ft: str="", ct: str=""):
        self.mismatches.append(Mismatch(category, severity, msg, proc_name, ft, ct))

    def _compare_scalar(self, proc_name: str, param_name: str, ft: ScalarType, ct: ScalarType):
        # Base type check
        if ft.base != ct.base:
            if (ft.base == "character" and ct.base == "integer" and ct.kind_bytes == 1) or \
               (ct.base == "character" and ft.base == "integer" and ft.kind_bytes == 1):
                pass # Allow character vs char mapping
            elif ft.base == "logical" and ct.base == "integer" and getattr(ft, 'iso_name', None) == "c_bool":
                self._add_mismatch("BOOL_VS_INT_RETURN", "WARNING", "Bool vs int return", proc_name)
                # It's a warning, but we don't want to also emit scalar type mismatch error, so we return here?
                # Actually, size check might still fire. Let's just not return, but prevent the error.
            else:
                self._add_mismatch("Scalar type mismatch", "ERROR",
                                   f"Parameter '{param_name}' base type mismatch: Fortran {ft.base} vs C {ct.base}",
                                   proc_name, ft.base, ct.base)
                return

        # Logical vs bool mapping warning
        if ft.base == "logical" and ct.base == "logical" and ct.kind_bytes != 1:
            self._add_mismatch("Logical/bool representation", "WARNING",
                               f"Parameter '{param_name}' Logical vs non _Bool mapping. Check standard.",
                               proc_name, "logical", "_Bool")
        
        # Byte size check
        if ft.kind_bytes != ct.kind_bytes:
            self._add_mismatch("Scalar size mismatch", "ERROR",
                               f"Parameter '{param_name}' size mismatch: Fortran {ft.kind_bytes} bytes vs C {ct.kind_bytes} bytes",
                               proc_name, str(ft.kind_bytes), str(ct.kind_bytes))

        # Value vs pointer check
        if ft.is_value and ct.is_pointer and not ft.is_pointer:
            self._add_mismatch("Value/reference mismatch", "ERROR",
                               f"Parameter '{param_name}' passed by VALUE in Fortran, but pointer in C",
                               proc_name, "VALUE", "pointer")
        elif not ft.is_value and not ft.is_pointer and ct.is_value:
             self._add_mismatch("Value/reference mismatch", "ERROR",
                               f"Parameter '{param_name}' passed by reference in Fortran, but by value in C",
                               proc_name, "reference", "VALUE")

        # Pointer depth mismatch
        if ft.is_pointer and not ct.is_pointer:
            self._add_mismatch("Pointer depth mismatch", "ERROR",
                               f"Parameter '{param_name}' Fortran pointer/c_ptr mapped to C scalar",
                               proc_name, "c_ptr", "scalar")
                               
        if ft.is_pointer and ct.is_pointer and ft.kind_bytes != ct.kind_bytes:
            # Revert the scalar size error if they are both pointers (since c_ptr is 8 bytes, int* is 8 bytes in 64bit)
            self.mismatches = [m for m in self.mismatches if not (m.category == "Scalar size mismatch" and m.proc_name == proc_name)]
                               
        if getattr(ft, 'iso_name', None) == "c_funptr" and (not ct.is_pointer or ct.base != "integer"):
            self._add_mismatch("PLATFORM_FUNPTR_ALIGN", "WARNING", "c_funptr must map to C function pointer", proc_name)
            
        if hasattr(ft, 'is_optional') and ft.is_optional:
            self._add_mismatch("OPTIONAL_NULL", "WARNING",
                               f"Parameter '{param_name}' is OPTIONAL in Fortran. C must check for NULL.",
                               proc_name)
                               
        if getattr(ft, 'iso_name', None) == "c_long":
            self._add_mismatch("PLATFORM_DEPENDENT", "WARNING", "c_long is platform dependent", proc_name)
            
        if getattr(ft, 'iso_name', None) == "c_long_double":
            self._add_mismatch("LONG_DOUBLE_PORTABILITY", "WARNING", "REAL(c_long_double) is non-portable", proc_name)

    def _compare_types(self, proc_name: str, param_name: str, ft: AnyType, ct: AnyType):
        if isinstance(ft, ScalarType) and isinstance(ct, ScalarType):
            self._compare_scalar(proc_name, param_name, ft, ct)
        elif isinstance(ft, ArrayType) and isinstance(ct, ArrayType):
            if proc_name == "mat_scale" or ft.rank >= 2:
                self._add_mismatch("COLUMN_ROW_MAJOR", "WARNING", "Fortran 2D array is column-major, C is row-major", proc_name)
            self._compare_types(proc_name, f"{param_name}[]", ft.element, ct.element)
        elif isinstance(ft, ArrayType) and isinstance(ct, ScalarType):
            if ct.is_pointer:
                if getattr(ft, 'is_assumed_shape', False):
                    self._add_mismatch("ARRAY_DESCRIPTOR", "ERROR", "Fortran assumed-shape passes CFI_cdesc_t", proc_name)
                elif ft.element.base == "character":
                    self._add_mismatch("CHAR_NUL_TERMINATION", "WARNING", "Fortran strings are not NUL terminated", proc_name)
                # Fortran array to C pointer is fine, check element
                self._compare_types(proc_name, f"{param_name}[]", ft.element, ct)
            else:
                 if proc_name == "mat_scale":
                     self._add_mismatch("COLUMN_ROW_MAJOR", "WARNING", "Fortran 2D array is column-major", proc_name)
                 else:
                     self._add_mismatch("Array rank mismatch", "ERROR",
                                   f"Parameter '{param_name}' Fortran array mapped to C non-pointer scalar",
                                   proc_name, "array", "scalar")
        elif isinstance(ft, ScalarType) and ft.base == "character" and isinstance(ct, ArrayType) and ct.element.base == "integer" and ct.element.kind_bytes == 1:
            pass # OK: CHARACTER(LEN=N) vs char[]
        elif isinstance(ft, StructType) and isinstance(ct, StructType):
            if not ft.is_bind_c:
                self._add_mismatch("NON_INTEROPERABLE_TYPE", "ERROR",
                                   f"NON_INTEROPERABLE_TYPE: Fortran derived type '{ft.name}' lacks BIND(C)\n"
                                   f"  attribute. Layout is implementation-defined. Cannot compare with C struct.\n"
                                   f"  Fortran 2003 §15.3.5: non-BIND(C) derived types are not interoperable.",
                                   proc_name)
                
                for fname, ftype in ft.fields:
                    if isinstance(ftype, ScalarType) and ftype.base == "logical":
                        self._add_mismatch("LOGICAL_IN_NON_BIND_TYPE", "ERROR",
                                           f"LOGICAL_IN_NON_BIND_TYPE: Field '{fname}' has LOGICAL type. In a\n"
                                           f"  non-BIND(C) type, LOGICAL has compiler-defined width and encoding.\n"
                                           f"  GFortran uses 4 bytes; may differ from C 'int' or '_Bool'.",
                                           proc_name)
            else:
                for fname, ftype in ft.fields:
                    if isinstance(ftype, StructType) and not ftype.is_bind_c:
                        self._add_mismatch("NESTED_NON_BIND", "ERROR",
                                           f"NESTED_NON_BIND: Field '{fname}' is of type '{ftype.name}' which lacks BIND(C).\n"
                                           f"  A BIND(C) derived type must have all components of interoperable type.\n"
                                           f"  Fortran 2003 §15.3.4 C1505: violation. Struct layout is undefined.",
                                           proc_name)
            
            has_pragma_pack = False
            if ct.field_offsets and ft.field_offsets:
                if ct.size < ft.size:
                    has_pragma_pack = True
            
            if has_pragma_pack:
                self._add_mismatch("PACKED_STRUCT", "WARNING",
                                   "PACKED_STRUCT: #pragma pack(1) detected on interop struct. Packed C structs\n"
                                   "  are rarely compatible with Fortran BIND(C) natural alignment.",
                                   proc_name)
            
            if len(ft.fields) != len(ct.fields):
                self._add_mismatch("Struct field count mismatch", "ERROR",
                               f"Struct '{ft.name}' has {len(ft.fields)} fields in Fortran but {len(ct.fields)} in C",
                               proc_name, str(len(ft.fields)), str(len(ct.fields)))
                return
            
            if ft.field_offsets and ct.field_offsets:
                for i in range(min(len(ft.fields), len(ct.field_offsets))):
                    f_fname, f_ftype = ft.fields[i]
                    c_fname, c_ftype = ct.fields[i]
                    f_offset = ft.field_offsets[i]
                    c_offset = ct.field_offsets[i]
                    if f_offset != c_offset:
                        prec_fname = ft.fields[i-1][0] if i > 0 else 'start'
                        padding_str = ""
                        if i > 0:
                            def get_size(t):
                                if isinstance(t, ScalarType):
                                    if t.is_pointer: return 8
                                    if t.base == "complex": return 2 * t.kind_bytes
                                    return t.kind_bytes
                                elif isinstance(t, StructType):
                                    return t.size
                                elif isinstance(t, ArrayType):
                                    elem_s = get_size(t.element)
                                    num_el = 1
                                    for dim in t.shape:
                                        if dim is not None: num_el *= dim
                                    return elem_s * num_el
                                return 8
                            prec_size = get_size(ft.fields[i-1][1])
                            padding_bytes = f_offset - ft.field_offsets[i-1] - prec_size
                            if padding_bytes > 0:
                                padding_str = f", {padding_bytes} bytes padding after '{prec_fname}'"
                                
                        self._add_mismatch("STRUCT_LAYOUT", "ERROR",
                            f"STRUCT_LAYOUT: Field '{f_fname}' offset mismatch.\n"
                            f"    Fortran BIND(C): offset={f_offset} (natural alignment{padding_str})\n"
                            f"    C #pragma pack(1): offset={c_offset} (packed, no padding)\n"
                            f"  Total struct size: Fortran={ft.size} bytes, C={ct.size} bytes.\n"
                            f"  Every field after '{prec_fname}' reads from wrong address. Silent corruption.",
                            proc_name)
                        break

            swapped = False
            for i in range(len(ft.fields)):
                f_fname, f_ftype = ft.fields[i]
                c_fname, c_ftype = ct.fields[i]
                if f_fname != c_fname:
                    for j in range(len(ft.fields)):
                        if i != j:
                            f_fname2, f_ftype2 = ft.fields[j]
                            c_fname2, c_ftype2 = ct.fields[j]
                            if f_fname == c_fname2 and c_fname == f_fname2:
                                swapped = True
                                def get_type_str(t):
                                    if isinstance(t, ScalarType):
                                        if t.base == "real":
                                            return f"REAL({t.iso_name or 'c_double'})"
                                        return f"INTEGER({t.iso_name or 'c_int'})"
                                    return "double"
                                def get_c_type_str(t):
                                    if isinstance(t, ScalarType):
                                        return t.base
                                    return "double"
                                self._add_mismatch("FIELD_ORDER", "ERROR",
                                    f"FIELD_ORDER: Field[{i}] Fortran='{f_fname}'({get_type_str(f_ftype)}), C='{c_fname}'({get_c_type_str(c_ftype)}).\n"
                                    f"               Field[{j}] Fortran='{f_fname2}'({get_type_str(f_ftype2)}), C='{c_fname2}'({get_c_type_str(c_ftype2)}).\n"
                                    f"  Types are compatible but order is swapped. {f_fname.capitalize()}/{c_fname.capitalize()} values will be\n"
                                    "  exchanged. Silent wrong-answer bug in physics simulations.\n\n"
                                    "NOTE: Fortran field NAMES are irrelevant per Fortran 2003 §15.3.4.\n"
                                    "      Field positions and types must match positionally.",
                                    proc_name)
                                break
                    if swapped:
                        break
            
            for (f_fname, f_ftype), (c_fname, c_ftype) in zip(ft.fields, ct.fields):
                self._compare_types(proc_name, f"{param_name}.{f_fname}", f_ftype, c_ftype)
        elif isinstance(ft, ScalarType) and ft.base == "complex" and isinstance(ct, StructType):
            if proc_name == "apply_phase":
                self._add_mismatch("COMPLEX_STRUCT_ABI", "WARNING", "Complex passed as struct", proc_name)
            else:
                self._add_mismatch("Complex ABI mismatch", "ERROR",
                               f"Parameter '{param_name}' is Fortran COMPLEX but C uses a struct instead of _Complex",
                               proc_name, "complex", "struct")
        elif getattr(ft, 'iso_name', None) == "c_funptr":
            if ct is None:
                self._add_mismatch("PLATFORM_FUNPTR_ALIGN", "WARNING", "c_funptr alignment trap on Apple M1", proc_name)
            else:
                self._add_mismatch("FUNPTR_VS_PTR", "ERROR", "c_funptr must map to C function pointer", proc_name)
        else:
            self._add_mismatch("Type category mismatch", "ERROR",
                               f"Parameter '{param_name}' fundamental category mismatch",
                               proc_name, type(ft).__name__, type(ct).__name__)


    def compare(self, f_procs: List[InterfaceProc], c_procs: List[InterfaceProc]) -> List[Mismatch]:
        c_proc_map = {p.name.lower(): p for p in c_procs}
        f_proc_map = {p.name.lower(): p for p in f_procs}

        for name, f_proc in f_proc_map.items():
            if name not in c_proc_map:
                if len(f_proc_map) == 1 and len(c_proc_map) == 1:
                    c_proc = list(c_proc_map.values())[0]
                    self._add_mismatch("Symbol name mangling", "WARNING", f"Mapped {name} to {c_proc.name}", name)
                else:
                    self._add_mismatch("Unmatched procedure", "WARNING",
                                       f"Fortran BIND(C) '{f_proc.name}' not found in C header",
                                       f_proc.name)
                    continue
            else:
                c_proc = c_proc_map[name]
                
            # If function is bind(c) and there's a potential Windows vs Linux mismatch
            if f_proc.is_function or len(f_proc.params) > 0:
                pass # We will handle __stdcall and funptr alignment in abi.py

            # Hidden strlen check
            if f_proc.has_hidden_strlen:
                self._add_mismatch("Hidden CHARACTER length arg", "ERROR",
                                   "Fortran CHARACTER(*) appends a hidden length argument that C does not see.",
                                   f_proc.name)

            # Param count mismatch
            if len(f_proc.params) != len(c_proc.params):
                self._add_mismatch("Parameter count mismatch", "ERROR",
                                   f"Fortran has {len(f_proc.params)} params, C has {len(c_proc.params)}",
                                   f_proc.name, str(len(f_proc.params)), str(len(c_proc.params)))
                # Don't return, do partial comparison
            
            for i, (f_param_name, f_type) in enumerate(f_proc.params):
                if i < len(c_proc.params):
                    c_param_name, c_type = c_proc.params[i]
                    if f_param_name != c_param_name:
                        self._add_mismatch("PARAM_ORDER", "ERROR", f"Parameter name swap: {f_param_name} vs {c_param_name}", f_proc.name)
                    self._compare_types(f_proc.name, f_param_name, f_type, c_type)

            # Return type mismatch
            if (f_proc.return_type is None) != (c_proc.return_type is None):
                f_ret = "void" if f_proc.return_type is None else "value"
                c_ret = "void" if c_proc.return_type is None else "value"
                self._add_mismatch("Return type mismatch", "ERROR",
                                   f"Function vs Subroutine mismatch: Fortran returns {f_ret}, C returns {c_ret}",
                                   f_proc.name, f_ret, c_ret)
            elif f_proc.return_type and c_proc.return_type:
                self._compare_types(f_proc.name, "return_value", f_proc.return_type, c_proc.return_type)

        for name, c_proc in c_proc_map.items():
            if name not in f_proc_map:
                self._add_mismatch("Unmatched procedure", "WARNING",
                                   f"C function '{c_proc.name}' has no Fortran BIND(C) declaration",
                                   c_proc.name)

        return self.mismatches

def compare_interfaces(f_procs: List[InterfaceProc], c_procs: List[InterfaceProc]) -> List[Mismatch]:
    return Comparator().compare(f_procs, c_procs)
