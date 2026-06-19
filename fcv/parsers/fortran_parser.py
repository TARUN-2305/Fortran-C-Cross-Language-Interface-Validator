import re
from typing import List, Optional, Tuple, Dict

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, AnyType
from fcv.ir.type_map import get_fortran_iso_type

class FortranParser:
    def __init__(self, platform: str = "lp64"):
        self.platform = platform

    def _join_continuations(self, lines: List[str]) -> List[Tuple[int, str]]:
        """Joins Fortran continuation lines (&) and returns a list of (line_num, text)."""
        result = []
        current_line = ""
        current_start_num = -1
        
        for i, raw_line in enumerate(lines):
            line_num = i + 1
            # Remove comments
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
                result.append((current_start_num, clean_line.lower()))
                current_line = ""
                current_start_num = -1
                
        return result

    def _get_type_size_and_alignment(self, t: AnyType) -> Tuple[int, int]:
        if isinstance(t, ScalarType):
            if t.is_pointer:
                return 8, 8 # 64-bit pointer
            if t.base == "complex":
                return 2 * t.kind_bytes, t.kind_bytes
            return t.kind_bytes, t.kind_bytes
        elif isinstance(t, ArrayType):
            elem_size, elem_align = self._get_type_size_and_alignment(t.element)
            num_elements = 1
            for dim in t.shape:
                if dim is not None:
                    num_elements *= dim
                else:
                    return 8, 8 # assumed-shape descriptor or pointer (8 bytes)
            return elem_size * num_elements, elem_align
        elif isinstance(t, StructType):
            if t.size > 0:
                max_align = 1
                for _, ftype in t.fields:
                    _, falign = self._get_type_size_and_alignment(ftype)
                    max_align = max(max_align, falign)
                return t.size, max_align
            else:
                offsets, size, align = self._compute_struct_layout(t)
                return size, align
        return 8, 8

    def _compute_struct_layout(self, struct_type: StructType) -> Tuple[List[int], int, int]:
        offsets = []
        current_offset = 0
        max_align = 1
        
        for fname, ftype in struct_type.fields:
            fsize, falign = self._get_type_size_and_alignment(ftype)
            
            # Align current offset to field's alignment
            if current_offset % falign != 0:
                current_offset += falign - (current_offset % falign)
                
            offsets.append(current_offset)
            current_offset += fsize
            max_align = max(max_align, falign)
            
        total_size = current_offset
        if total_size % max_align != 0:
            total_size += max_align - (total_size % max_align)
            
        return offsets, total_size, max_align

    def _parse_type_spec(self, type_str: str, derived_types: dict = None) -> Optional[AnyType]:
        """Parses a type spec like 'integer(c_int)', 'type(c_ptr)', 'type(grid_params)', etc."""
        type_str = type_str.strip().lower()
        
        # type(c_ptr) or type(c_funptr)
        if "c_funptr" in type_str:
            return ScalarType(base="integer", kind_bytes=8, is_pointer=True, iso_name="c_funptr")
        if "c_ptr" in type_str:
            return ScalarType(base="integer", kind_bytes=8, is_pointer=True, iso_name="c_ptr")
            
        m_derived = re.match(r"type\s*\(\s*([a-z0-9_]+)\s*\)", type_str)
        if m_derived:
            typename = m_derived.group(1)
            if derived_types and typename in derived_types:
                info = derived_types[typename]
                return StructType(
                    name=info["name"],
                    fields=info["fields"],
                    is_bind_c=info["is_bind_c"],
                    field_offsets=info.get("field_offsets"),
                    size=info.get("size", 0)
                )
            else:
                return StructType(name=typename, fields=[], is_bind_c=False)

        # Handle double precision
        if type_str.startswith("double precision") or type_str.startswith("doubleprecision"):
            return ScalarType(base="real", kind_bytes=8, is_pointer=False)

        # Handle type*size legacy syntax (e.g. integer*8, real*8, complex*16)
        m_size = re.match(r"([a-z]+)\*([0-9]+)", type_str)
        if m_size:
            base = m_size.group(1)
            size = int(m_size.group(2))
            # In Fortran complex*16, kind is 8 bytes, but total size is 16.
            # ScalarType kind_bytes represents the kind parameter (e.g. 8).
            kind_bytes = size
            if base == "complex":
                kind_bytes = size // 2
            return ScalarType(base=base, kind_bytes=kind_bytes, is_pointer=False)

        m = re.match(r"(integer|real|complex|logical|character)(?:\s*\(\s*(kind\s*=\s*)?([a-z_0-9]+)\s*\))?", type_str)
        if m:
            base = m.group(1)
            kind_name = m.group(3)
            if kind_name:
                if kind_name.isdigit():
                    iso_info = (base, int(kind_name))
                else:
                    iso_info = get_fortran_iso_type(kind_name, self.platform)
            else:
                default_sizes = {"integer": 4, "real": 4, "complex": 8, "logical": 4, "character": 1}
                iso_info = (base, default_sizes[base])
            if iso_info:
                # Character arrays often have length, handled elsewhere
                return ScalarType(base=iso_info[0], kind_bytes=iso_info[1], is_pointer=False, iso_name=kind_name)
        
        return None

    def parse_file(self, filepath: str) -> List[InterfaceProc]:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        joined_lines = self._join_continuations(lines)
        
        # Pre-pass to scan for derived type declarations
        derived_types = {}
        in_type = False
        current_type_name = None
        current_type_bind_c = False
        current_type_fields = []
        
        type_def_start_re = re.compile(r"^\s*type(?!\s*\()\s*(?:,\s*[a-z0-9_\(\)]+)*\s*(?:::\s*)?([a-z0-9_]+)", re.IGNORECASE)
        type_def_end_re = re.compile(r"^\s*end\s+type", re.IGNORECASE)
        
        for line_num, line in joined_lines:
            line_lower = line.strip().lower()
            if not in_type:
                m = type_def_start_re.match(line_lower)
                if m:
                    current_type_name = m.group(1)
                    current_type_bind_c = "bind(c)" in line_lower
                    current_type_fields = []
                    in_type = True
            else:
                if type_def_end_re.match(line_lower):
                    derived_types[current_type_name] = {
                        "name": current_type_name,
                        "is_bind_c": current_type_bind_c,
                        "fields": current_type_fields,
                        "field_offsets": [],
                        "size": 0
                    }
                    in_type = False
                else:
                    if "::" in line_lower:
                        left, right = line_lower.split("::", 1)
                        attrs = [a.strip() for a in left.split(",")]
                        type_str = attrs[0]
                        is_pointer = "pointer" in left
                        is_optional = "optional" in left
                        
                        parsed_type = self._parse_type_spec(type_str, derived_types)
                        if parsed_type:
                            if isinstance(parsed_type, ScalarType):
                                parsed_type.is_pointer = is_pointer or parsed_type.is_pointer
                                parsed_type.is_optional = is_optional
                            
                            dim_match = re.search(r'dimension\s*\((.*?)\)', left, re.IGNORECASE)
                            is_array = False
                            rank = 1
                            is_assumed = False
                            shape_list = []
                            if dim_match:
                                is_array = True
                                dim_spec = dim_match.group(1)
                                is_assumed = (":" in dim_spec) or ("*" in dim_spec)
                                rank = dim_spec.count(",") + 1
                                for bounds in dim_spec.split(","):
                                    bounds = bounds.strip()
                                    if bounds.isdigit():
                                        shape_list.append(int(bounds))
                                    else:
                                        shape_list.append(None)
                            elif "dimension" in left.lower():
                                is_array = True
                                
                            vars_decl = [v.strip() for v in right.split(",")]
                            for v in vars_decl:
                                v_name = v.split("(")[0].strip()
                                v_is_array = is_array
                                v_rank = rank
                                v_is_assumed = is_assumed
                                v_shape = list(shape_list)
                                if "(" in v:
                                    v_is_array = True
                                    dim_spec = v.split("(")[1].split(")")[0]
                                    v_is_assumed = (":" in dim_spec) or ("*" in dim_spec)
                                    v_rank = dim_spec.count(",") + 1
                                    v_shape = []
                                    for bounds in dim_spec.split(","):
                                        bounds = bounds.strip()
                                        if bounds.isdigit():
                                            v_shape.append(int(bounds))
                                        else:
                                            v_shape.append(None)
                                            
                                if v_is_array:
                                    current_type_fields.append((
                                        v_name, 
                                        ArrayType(
                                            element=parsed_type,
                                            rank=v_rank,
                                            shape=v_shape if v_shape else [None]*v_rank,
                                            is_assumed_shape=v_is_assumed,
                                            is_optional=is_optional
                                        )
                                    ))
                                else:
                                    current_type_fields.append((v_name, parsed_type))

        # Post-process out-of-order/empty struct references
        for tname in list(derived_types.keys()):
            tinfo = derived_types[tname]
            for idx, (fname, ftype) in enumerate(tinfo["fields"]):
                if isinstance(ftype, StructType) and not ftype.fields:
                    if ftype.name in derived_types:
                        tinfo["fields"][idx] = (fname, StructType(
                            name=derived_types[ftype.name]["name"],
                            fields=derived_types[ftype.name]["fields"],
                            is_bind_c=derived_types[ftype.name]["is_bind_c"],
                            field_offsets=derived_types[ftype.name]["field_offsets"],
                            size=derived_types[ftype.name]["size"]
                        ))

        # Compute layouts recursively to support nested structs
        def compute_layout_recursive(tname):
            tinfo = derived_types[tname]
            if tinfo["size"] > 0:
                return
            
            for fname, ftype in tinfo["fields"]:
                if isinstance(ftype, StructType):
                    compute_layout_recursive(ftype.name)
                    ftype.fields = derived_types[ftype.name]["fields"]
                    ftype.is_bind_c = derived_types[ftype.name]["is_bind_c"]
                    ftype.field_offsets = derived_types[ftype.name]["field_offsets"]
                    ftype.size = derived_types[ftype.name]["size"]
            
            temp_struct = StructType(name=tname, fields=tinfo["fields"], is_bind_c=tinfo["is_bind_c"])
            offsets, size, align = self._compute_struct_layout(temp_struct)
            tinfo["field_offsets"] = offsets
            tinfo["size"] = size

        for tname in derived_types:
            compute_layout_recursive(tname)
        
        procs = []
        in_interface = False
        in_module = False
        current_proc: Optional[InterfaceProc] = None
        current_args_order: List[str] = []
        current_args_types: Dict[str, AnyType] = {}
        
        proc_re = re.compile(r"(?:([a-z0-9_\(\)\s]+)\s+)?(subroutine|function)\s+([a-z0-9_]+)\s*\((.*?)\)", re.IGNORECASE)
        bind_c_re = re.compile(r"bind\s*\(\s*c\s*(?:,\s*name\s*=\s*['\"](.*?)['\"])?\s*\)", re.IGNORECASE)
        module_re = re.compile(r"^\s*module\s+[a-z0-9_]+", re.IGNORECASE)
        end_module_re = re.compile(r"^\s*end\s+module", re.IGNORECASE)
        
        for line_num, line in joined_lines:
            if "interface" in line and not "end interface" in line:
                in_interface = True
                continue
            if "end interface" in line:
                in_interface = False
                continue
                
            if module_re.search(line):
                in_module = True
                continue
            if end_module_re.search(line):
                in_module = False
                continue
                
            if "end subroutine" in line or "end function" in line:
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
                    
                is_function = (proc_type == "function")
                return_type = None
                if is_function and ret_type_str:
                    return_type = self._parse_type_spec(ret_type_str, derived_types)
                    
                current_proc = InterfaceProc(
                    name=bind_name,
                    source_file=filepath,
                    source_line=line_num,
                    return_type=return_type,
                    params=[],
                    is_function=is_function
                )
                current_proc.fortran_name = proc_name
                current_proc.is_bind_c = (m_bind is not None)
                
                if args_str:
                    current_args_order = [a.strip() for a in args_str.split(",") if a.strip()]
                else:
                    current_args_order = []
                current_args_types = {}
                continue
                
            if current_proc:
                if "character" in line:
                    left_spec = line.split("::", 1)[0] if "::" in line else line
                    if not current_proc.is_bind_c or "(*)" in left_spec or "len=*" in left_spec:
                        current_proc.has_hidden_strlen = True
                
                if "::" in line:
                    left, right = line.split("::", 1)
                    attrs = [a.strip() for a in left.split(",")]
                    type_str = attrs[0]
                    is_value = "value" in left
                    is_pointer = "pointer" in left
                    is_optional = "optional" in left
                    
                    parsed_type = self._parse_type_spec(type_str, derived_types)
                    if parsed_type:
                        if isinstance(parsed_type, ScalarType):
                            parsed_type.is_value = is_value
                            parsed_type.is_pointer = is_pointer or ("type(c_ptr)" in type_str) or parsed_type.is_pointer
                            parsed_type.is_optional = is_optional
                        elif isinstance(parsed_type, StructType):
                            parsed_type.is_optional = is_optional
                        
                        dim_match = re.search(r'dimension\s*\((.*?)\)', left, re.IGNORECASE)
                        is_array = False
                        rank = 1
                        is_assumed = False
                        if dim_match:
                            is_array = True
                            is_assumed = (":" in dim_match.group(1))
                            rank = dim_match.group(1).count(":") or 1
                        elif "dimension" in left.lower():
                            is_array = True
                        
                        vars_decl = [v.strip() for v in right.split(",")]
                        for v in vars_decl:
                            v_name = v.split("(")[0].strip()
                            if "(" in v:
                                is_array = True
                                is_assumed = (":" in v)
                                rank = v.count(":") or 1
                            
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
                                
                    elif is_function and current_proc.return_type is None:
                         v_names = [v.strip() for v in right.split(",")]
                         if current_proc.name in v_names or getattr(current_proc, 'fortran_name', '') in v_names:
                             current_proc.return_type = self._parse_type_spec(type_str, derived_types)

        return procs

def parse_fortran_file(filepath: str, platform: str = "lp64") -> List[InterfaceProc]:
    parser = FortranParser(platform)
    return parser.parse_file(filepath)
