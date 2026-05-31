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

    def _parse_type_spec(self, type_str: str) -> Optional[ScalarType]:
        """Parses a type spec like 'integer(c_int)', 'type(c_ptr)', etc."""
        type_str = type_str.strip()
        
        # type(c_ptr) or type(c_funptr)
        if "c_funptr" in type_str:
            return ScalarType(base="integer", kind_bytes=8, is_pointer=True, iso_name="c_funptr")
        if "c_ptr" in type_str:
            return ScalarType(base="integer", kind_bytes=8, is_pointer=True, iso_name="c_ptr")
            
        m = re.match(r"(integer|real|complex|logical|character)(?:\s*\(\s*(kind\s*=\s*)?([a-z_0-9]+)\s*\))?", type_str)
        if m:
            base = m.group(1)
            kind_name = m.group(3)
            if kind_name:
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
        
        procs = []
        
        in_interface = False
        in_module = False
        current_proc: Optional[InterfaceProc] = None
        current_args_order: List[str] = []
        current_args_types: Dict[str, AnyType] = {}
        
        # Very basic regex for subroutines and functions
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
                    # Construct parameters
                    params = []
                    for arg in current_args_order:
                        if arg in current_args_types:
                            params.append((arg, current_args_types[arg]))
                        else:
                            # Unknown type
                            pass
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
                    bind_name = proc_name + "_" # Simple mangling simulation
                    
                is_function = (proc_type == "function")
                return_type = None
                if is_function and ret_type_str:
                    return_type = self._parse_type_spec(ret_type_str)
                    
                current_proc = InterfaceProc(
                    name=bind_name,
                    source_file=filepath,
                    source_line=line_num,
                    return_type=return_type,
                    params=[],
                    is_function=is_function
                )
                current_proc.fortran_name = proc_name # Save internal name for fallback parsing
                
                if args_str:
                    current_args_order = [a.strip() for a in args_str.split(",") if a.strip()]
                else:
                    current_args_order = []
                current_args_types = {}
                continue
                
            if current_proc:
                # Parameter declarations
                # e.g., type(c_ptr), value :: ptr
                # integer(c_int), intent(in) :: n
                # character(kind=c_char), dimension(*) :: str
                
                # Check for hidden strlen
                if "character" in line and "(*)" in line and not "bind(c" in line:
                    current_proc.has_hidden_strlen = True
                
                if "::" in line:
                    left, right = line.split("::", 1)
                    attrs = [a.strip() for a in left.split(",")]
                    type_str = attrs[0]
                    is_value = "value" in left
                    is_pointer = "pointer" in left
                    is_optional = "optional" in left
                    
                    parsed_type = self._parse_type_spec(type_str)
                    if parsed_type:
                        parsed_type.is_value = is_value
                        parsed_type.is_pointer = is_pointer or ("type(c_ptr)" in type_str)
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
                            # if array is declared with parenthesis on the right
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
                         # Sometimes function return type is declared in the body
                         v_names = [v.strip() for v in right.split(",")]
                         if current_proc.name in v_names or getattr(current_proc, 'fortran_name', '') in v_names:
                             current_proc.return_type = self._parse_type_spec(type_str)

        return procs

def parse_fortran_file(filepath: str, platform: str = "lp64") -> List[InterfaceProc]:
    parser = FortranParser(platform)
    return parser.parse_file(filepath)
