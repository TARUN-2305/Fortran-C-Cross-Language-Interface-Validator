import re
from typing import List, Optional, Tuple, Dict, Any

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, AnyType
from fcv.ir.type_map import get_fortran_iso_type

class FortranParser:
    def __init__(self, platform: str = "lp64"):
        self.platform = platform
        self.symbol_table: Dict[str, int] = {
            "c_int": 4 if platform != "ilp64" else 8,
            "c_short": 2,
            "c_long": 8,
            "c_long_long": 8,
            "c_signed_char": 1,
            "c_size_t": 8,
            "c_int8_t": 1,
            "c_int16_t": 2,
            "c_int32_t": 4,
            "c_int64_t": 8,
            "c_float": 4,
            "c_double": 8,
            "c_long_double": 16,
            "c_bool": 1,
            "c_char": 1,
            "c_ptr": 8,
            "c_funptr": 8,
        }
        self.derived_types: Dict[str, StructType] = {}

    def _join_continuations(self, lines: List[str]) -> List[Tuple[int, str]]:
        """Joins Fortran continuation lines (&) and returns a list of (line_num, text)."""
        result = []
        current_line = ""
        current_start_num = -1
        
        for i, raw_line in enumerate(lines):
            line_num = i + 1
            # Remove comments (while keeping literal quotes safe, simple splitting is fine for our interfaces)
            line = raw_line.split("!")[0].strip()
            if not line:
                continue
            
            if current_start_num == -1:
                current_start_num = line_num
            
            if line.endswith("&"):
                current_line += " " + line[:-1].strip()
            else:
                current_line += " " + line
                # Fortran uses & at the start of continued lines too sometimes, strip it
                clean_line = current_line.strip()
                if clean_line.startswith("&"):
                    clean_line = clean_line[1:].strip()
                result.append((current_start_num, clean_line))
                current_line = ""
                current_start_num = -1
                
        return result

    def _calculate_struct_layout(self, fields: List[Tuple[str, AnyType]]) -> Tuple[List[Tuple[str, AnyType, int]], int, int]:
        current_offset = 0
        max_align = 1
        aligned_fields = []
        
        for f_name, f_type in fields:
            if isinstance(f_type, ScalarType):
                f_size = f_type.kind_bytes
                f_align = f_type.kind_bytes
                if f_type.pointer_depth > 0:
                    f_size = 8
                    f_align = 8
            elif isinstance(f_type, ArrayType):
                if isinstance(f_type.element, ScalarType):
                    f_align = f_type.element.kind_bytes
                    if f_type.element.pointer_depth > 0:
                        f_align = 8
                else:
                    f_align = 8
                elem_size = f_type.element.kind_bytes if isinstance(f_type.element, ScalarType) else 8
                if isinstance(f_type.element, ScalarType) and f_type.element.pointer_depth > 0:
                    elem_size = 8
                shape_mul = 1
                for s in f_type.shape:
                    if s is not None:
                        shape_mul *= s
                f_size = shape_mul * elem_size
            elif isinstance(f_type, StructType):
                f_size = f_type.size_bytes
                f_align = f_type.alignment
            else:
                f_size = 4
                f_align = 4
                
            if current_offset % f_align != 0:
                current_offset += f_align - (current_offset % f_align)
                
            aligned_fields.append((f_name, f_type, current_offset))
            current_offset += f_size
            if f_align > max_align:
                max_align = f_align
                
        total_size = current_offset
        if total_size % max_align != 0:
            total_size += max_align - (total_size % max_align)
            
        return aligned_fields, total_size, max_align

    def _parse_type_spec(self, type_str: str) -> Optional[AnyType]:
        """Parses a type spec like 'integer(c_int)', 'type(c_ptr)', 'type(gridpoint)', etc."""
        type_str = type_str.strip().lower()
        
        # c_funptr / c_ptr
        if "c_funptr" in type_str:
            return ScalarType(base="integer", kind_bytes=8, pointer_depth=1, iso_name="c_funptr")
        if "c_ptr" in type_str:
            return ScalarType(base="integer", kind_bytes=8, pointer_depth=1, iso_name="c_ptr")
            
        # Derived type
        m_struct = re.match(r"type\s*\(\s*([a-z0-9_]+)\s*\)", type_str)
        if m_struct:
            name = m_struct.group(1)
            if name in self.derived_types:
                return self.derived_types[name]
            return StructType(name=name, fields=[], is_bind_c=True)
            
        m = re.match(r"(integer|real|complex|logical|character)(?:\s*\(\s*(kind\s*=\s*)?([a-z_0-9]+)\s*\))?", type_str)
        if m:
            base = m.group(1)
            kind_name = m.group(3)
            if kind_name:
                # Lookup in symbol table first
                if kind_name in self.symbol_table:
                    kind_bytes = self.symbol_table[kind_name]
                    return ScalarType(base=base, kind_bytes=kind_bytes, is_pointer=False, iso_name=kind_name)
                iso_info = get_fortran_iso_type(kind_name, self.platform)
                if iso_info:
                    return ScalarType(base=iso_info[0], kind_bytes=iso_info[1], is_pointer=False, iso_name=kind_name)
            
            # Default fallback sizes
            default_sizes = {"integer": 4, "real": 4, "complex": 8, "logical": 4, "character": 1}
            return ScalarType(base=base, kind_bytes=default_sizes[base], is_pointer=False, iso_name=kind_name)
        
        return None

    def _split_respect_parens(self, s: str, sep: str = ',') -> List[str]:
        parts = []
        curr = []
        depth = 0
        for char in s:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            if char == sep and depth == 0:
                parts.append("".join(curr).strip())
                curr = []
            else:
                curr.append(char)
        if curr:
            parts.append("".join(curr).strip())
        return parts

    def parse_file(self, filepath: str) -> List[InterfaceProc]:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        joined_lines = self._join_continuations(lines)
        
        # Pass 1: Parse parameter variables and structures
        self._parse_constants_and_structs(joined_lines)
        
        procs = []
        in_interface = False
        current_proc: Optional[InterfaceProc] = None
        current_args_order: List[str] = []
        current_args_types: Dict[str, AnyType] = {}
        
        proc_re = re.compile(r"(?:([a-z0-9_\(\)\s]+)\s+)?(subroutine|function)\s+([a-z0-9_]+)\s*\((.*?)\)", re.IGNORECASE)
        bind_c_re = re.compile(r"bind\s*\(\s*c\s*(?:,\s*name\s*=\s*['\"](.*?)['\"])?\s*\)", re.IGNORECASE)
        
        for line_num, line in joined_lines:
            line_lower = line.lower()
            if "interface" in line_lower and not "end interface" in line_lower:
                in_interface = True
                continue
            if "end interface" in line_lower:
                in_interface = False
                continue
                
            if "end subroutine" in line_lower or "end function" in line_lower:
                if current_proc:
                    params = []
                    for arg in current_args_order:
                        if arg in current_args_types:
                            params.append((arg, current_args_types[arg]))
                    current_proc.params = params
                    procs.append(current_proc)
                    current_proc = None
                continue
                
            m_proc = proc_re.search(line)
            if m_proc:
                ret_type_str = m_proc.group(1)
                proc_type = m_proc.group(2)
                proc_name = m_proc.group(3)
                args_str = m_proc.group(4)
                
                m_bind = bind_c_re.search(line)
                bind_name = proc_name
                if m_bind and m_bind.group(1):
                    bind_name = m_bind.group(1)
                elif not m_bind:
                    bind_name = proc_name + "_"
                    
                is_function = (proc_type.lower() == "function")
                return_type = None
                if is_function and ret_type_str:
                    return_type = self._parse_type_spec(ret_type_str)
                    
                result_var = None
                if is_function:
                    res_m = re.search(r"result\s*\(\s*([a-z0-9_]+)\s*\)", line, re.IGNORECASE)
                    if res_m:
                        result_var = res_m.group(1).lower()
                    else:
                        result_var = proc_name.lower()
                        
                current_proc = InterfaceProc(
                    name=bind_name,
                    source_file=filepath,
                    source_line=line_num,
                    return_type=return_type,
                    params=[],
                    is_function=is_function
                )
                current_proc.fortran_name = proc_name
                current_proc.result_var = result_var
                current_proc.is_bind_c = (m_bind is not None)
                
                if args_str:
                    current_args_order = [a.strip() for a in args_str.split(",") if a.strip()]
                else:
                    current_args_order = []
                current_args_types = {}
                continue
                
            if current_proc:
                # Check for hidden strlen
                if "character" in line_lower:
                    left_spec = line.split("::", 1)[0] if "::" in line else line
                    if "(*)" in left_spec or "len=*" in left_spec or not getattr(current_proc, 'is_bind_c', False):
                        current_proc.has_hidden_strlen = True
                
                if "::" in line:
                    left, right = line.split("::", 1)
                    attrs = [a.strip().lower() for a in self._split_respect_parens(left)]
                    type_str = attrs[0]
                    is_value = "value" in attrs
                    is_pointer = "pointer" in attrs
                    is_optional = "optional" in attrs
                    is_const = any("intent(in)" in a for a in attrs)
                    
                    parsed_type = self._parse_type_spec(type_str)
                    if parsed_type:
                        # Copy/set attributes
                        if isinstance(parsed_type, ScalarType):
                            # Create copy so we don't pollute global definition
                            parsed_type = ScalarType(
                                base=parsed_type.base,
                                kind_bytes=parsed_type.kind_bytes,
                                is_pointer=is_pointer or parsed_type.pointer_depth > 0,
                                pointer_depth=1 if is_pointer else parsed_type.pointer_depth,
                                is_value=is_value,
                                is_optional=is_optional,
                                iso_name=parsed_type.iso_name,
                                is_const=is_const
                            )
                        elif isinstance(parsed_type, StructType):
                            # Pass structural copy
                            parsed_type = StructType(
                                name=parsed_type.name,
                                fields=parsed_type.fields,
                                size_bytes=parsed_type.size_bytes,
                                alignment=parsed_type.alignment,
                                is_bind_c=parsed_type.is_bind_c,
                                is_optional=is_optional
                            )
                        
                        dim_match = re.search(r'dimension\s*\((.*?)\)', left, re.IGNORECASE)
                        is_array = False
                        rank = 1
                        is_assumed = False
                        if dim_match:
                            is_array = True
                            is_assumed = (":" in dim_match.group(1))
                            rank = dim_match.group(1).count(",") + 1
                        elif "dimension" in left.lower():
                            is_array = True
                        
                        vars_decl = self._split_respect_parens(right)
                        for v in vars_decl:
                            v_name = v.split("(")[0].strip()
                            if "(" in v:
                                is_array = True
                                is_assumed = (":" in v)
                                rank = v.split("(")[1].split(")")[0].count(",") + 1
                            
                            # Check if this variable is the return variable of a function
                            v_name_lower = v_name.lower()
                            is_ret = False
                            if getattr(current_proc, 'is_function', False) and (
                                v_name_lower == getattr(current_proc, 'result_var', '') or
                                v_name_lower == getattr(current_proc, 'fortran_name', '').lower()
                            ):
                                is_ret = True
                                
                            if is_ret:
                                if is_array:
                                    current_proc.return_type = ArrayType(
                                        element=parsed_type,
                                        rank=rank,
                                        shape=[None] * rank,
                                        is_assumed_shape=is_assumed,
                                        is_optional=is_optional
                                    )
                                else:
                                    current_proc.return_type = parsed_type
                            else:
                                if is_array:
                                    current_args_types[v_name] = ArrayType(
                                        element=parsed_type,
                                        rank=rank,
                                        shape=[None] * rank,
                                        is_assumed_shape=is_assumed,
                                        is_optional=is_optional
                                    )
                                else:
                                    current_args_types[v_name] = parsed_type

        return procs

    def _parse_constants_and_structs(self, joined_lines: List[Tuple[int, str]]):
        """Pass 1: Scan for constants and derived type layouts."""
        in_struct = False
        struct_name = ""
        struct_fields = []
        struct_is_bind_c = False
        
        # Matches: integer, parameter :: dp = 8
        param_re = re.compile(r"integer\s*,\s*parameter\s*::\s*([a-z0-9_]+)\s*=\s*(.*)", re.IGNORECASE)
        # Matches: type, bind(c) :: gridpoint (or type :: mesh_config)
        type_re = re.compile(r"type\s*(?:,\s*bind\s*\(\s*c\s*\)\s*)?(?:::\s*)?([a-z0-9_]+)", re.IGNORECASE)
        
        for line_num, line in joined_lines:
            line_lower = line.lower()
            
            # Constant parameter
            m_param = param_re.search(line)
            if m_param:
                name = m_param.group(1).lower()
                val_expr = m_param.group(2).strip().lower()
                # Basic constant folding
                if "kind" in val_expr:
                    if "d0" in val_expr or "double" in val_expr or "0.0d0" in val_expr:
                        self.symbol_table[name] = 8
                    else:
                        self.symbol_table[name] = 4
                else:
                    try:
                        self.symbol_table[name] = int(val_expr)
                    except ValueError:
                        self.symbol_table[name] = 4
                continue
                
            # Derived type start
            m_type = type_re.search(line)
            if m_type:
                # Distinguish from "end type" or "type(foo)"
                if "end type" in line_lower or "type(" in line_lower:
                    pass
                else:
                    in_struct = True
                    struct_name = m_type.group(1).lower()
                    struct_fields = []
                    struct_is_bind_c = "bind(c)" in line_lower
                    continue
                
            if in_struct:
                if "end type" in line_lower:
                    # Calculate layout, padding and store
                    aligned_fields, size_bytes, alignment = self._calculate_struct_layout(struct_fields)
                    self.derived_types[struct_name] = StructType(
                        name=struct_name,
                        fields=aligned_fields,
                        size_bytes=size_bytes,
                        alignment=alignment,
                        is_bind_c=struct_is_bind_c
                    )
                    in_struct = False
                    continue
                    
                if "::" in line:
                    left, right = line.split("::", 1)
                    attrs = [a.strip().lower() for a in self._split_respect_parens(left)]
                    type_str = attrs[0]
                    parsed_type = self._parse_type_spec(type_str)
                    
                    if parsed_type:
                        dim_match = re.search(r'dimension\s*\((.*?)\)', left, re.IGNORECASE)
                        is_array = False
                        rank = 1
                        if dim_match:
                            is_array = True
                            rank = dim_match.group(1).count(",") + 1
                            
                        vars_decl = self._split_respect_parens(right)
                        for v in vars_decl:
                            v_name = v.split("(")[0].strip()
                            is_array_local = is_array
                            rank_local = rank
                            if "(" in v:
                                is_array_local = True
                                rank_local = v.split("(")[1].split(")")[0].count(",") + 1
                                
                            if is_array_local:
                                struct_fields.append((v_name, ArrayType(
                                    element=parsed_type,
                                    rank=rank_local,
                                    shape=[None] * rank_local
                                )))
                            else:
                                struct_fields.append((v_name, parsed_type))

def parse_fortran_file(filepath: str, platform: str = "lp64") -> List[InterfaceProc]:
    parser = FortranParser(platform)
    return parser.parse_file(filepath)
