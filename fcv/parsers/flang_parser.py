import subprocess
import os
import re
import sys
import tempfile
from typing import List, Optional, Tuple, Dict, Any

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, AnyType
from fcv.ir.type_map import get_fortran_iso_type
from fcv.parsers.fortran_parser import FortranParser, parse_fortran_file
from fcv.parsers.gfortran_parser import GfortranParser, _gfortran_binary


def _flang_binary() -> Optional[str]:
    """Return path to flang executable if available, else None."""
    for name in ("flang-new", "flang-21", "flang-20", "flang-19", "flang-18", "flang-17", "flang"):
        try:
            result = subprocess.run(["which", name], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
        except FileNotFoundError:
            pass
    return None


def fortran_parser_backend_name() -> str:
    """Return a human-readable name for the Fortran parser backend that will be used."""
    flang = _flang_binary()
    if flang:
        return f"flang ({flang}) LLVM compiler frontend"
    if _gfortran_binary():
        return f"gfortran ({_gfortran_binary()}) compiler frontend"
    return "regex-based Fortran parser (no compiler available — install gfortran or flang-new for compiler-grade accuracy)"

class FlangASTNode:
    def __init__(self, name: str, value: str = ""):
        self.name = name.strip()
        self.value = value.strip()
        self.children: List['FlangASTNode'] = []

    def find_all(self, name: str) -> List['FlangASTNode']:
        result = []
        parts = [p.strip().lower() for p in self.name.split("->")]
        if name.lower() in parts:
            result.append(self)
        for child in self.children:
            result.extend(child.find_all(name))
        return result

    def find_first(self, name: str) -> Optional['FlangASTNode']:
        parts = [p.strip().lower() for p in self.name.split("->")]
        if name.lower() in parts:
            return self
        for child in self.children:
            found = child.find_first(name)
            if found:
                return found
        return None

class FlangParser:
    def __init__(self, platform: str = "lp64"):
        self.platform = platform

    def parse_file(self, filepath: str, raise_on_error: bool = False) -> List[InterfaceProc]:
        # Read file content to see if it needs wrapping to be a valid Fortran program unit
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Clean comments and whitespace to check first statement
        content_clean = ""
        for line in content.splitlines():
            line_strip = line.strip()
            if line_strip and not line_strip.startswith("!"):
                content_clean += line_strip.lower() + "\n"

        needs_wrap = False
        if content_clean.strip().startswith("interface"):
            needs_wrap = True

        # Attempt to run flang to get the parse tree
        flang = _flang_binary()
        if flang:
            temp_file = None
            try:
                if needs_wrap:
                    ext = os.path.splitext(filepath)[1] or ".f90"
                    fd, temp_path = tempfile.mkstemp(suffix=ext)
                    with os.fdopen(fd, 'w', encoding='utf-8') as tf:
                        tf.write(f"module temp_wrapper_mod\n  use iso_c_binding\n{content}\nend module temp_wrapper_mod")
                    target_path = temp_path
                    temp_file = temp_path
                else:
                    target_path = filepath

                result = subprocess.run(
                    [flang, "-fc1", "-fdebug-dump-parse-tree", target_path],
                    capture_output=True,
                    text=True,
                    check=True
                )
                output = result.stdout
                return self._parse_flang_ast(output, filepath)
            except subprocess.CalledProcessError as e:
                if raise_on_error:
                    raise RuntimeError(
                        f"Error: flang compiler failed to parse {filepath}.\nDetails: {e.stderr}"
                    )
            finally:
                if temp_file and os.path.exists(temp_file):
                    try:
                        os.remove(temp_file)
                    except Exception:
                        pass
        else:
            if raise_on_error:
                raise RuntimeError(
                    f"Error: flang compiler is not installed or available in your PATH, "
                    f"but --use-flang was explicitly requested."
                )

        # Fallback 1: gfortran (real compiler, better than regex)
        gfortran = GfortranParser(self.platform)
        if gfortran.available:
            print(
                "INFO: flang not found. Using gfortran compiler frontend.",
                file=sys.stderr
            )
            return gfortran.parse_file(filepath)
            # Fallback 2: regex parser
            print(
                "WARNING: No Fortran compiler (flang-new or gfortran) found in PATH. "
                "Falling back to regex-based Fortran parser. "
                "Install gfortran for compiler-grade accuracy: sudo apt-get install gfortran",
                file=sys.stderr
            )
            fallback = FortranParser(self.platform)
            return fallback.parse_file(filepath)

    def _parse_flang_ast(self, ast_text: str, filepath: str) -> List[InterfaceProc]:
        # Parse indentation tree
        root = self._build_ast_tree(ast_text)
        procs = []

        # Find SubroutineSubprogram, FunctionSubprogram, Subroutine, and Function nodes
        subprogram_nodes = (
            root.find_all("SubroutineSubprogram") + 
            root.find_all("FunctionSubprogram") +
            root.find_all("Subroutine") +
            root.find_all("Function")
        )

        for sub_node in subprogram_nodes:
            proc = self._extract_procedure(sub_node, filepath)
            if proc:
                procs.append(proc)

        return procs

    def _build_ast_tree(self, text: str) -> FlangASTNode:
        lines = text.splitlines()
        root = FlangASTNode("Root")
        stack = [(-1, root)]
        
        for line in lines:
            if not line.strip() or "Flang: parse tree dump" in line:
                continue
            
            depth = line.count("|")
            content = line.replace("|", "").strip()
            if not content:
                continue
            
            if "=" in content:
                name, val = content.split("=", 1)
                node = FlangASTNode(name, val)
            else:
                node = FlangASTNode(content)
                
            while stack and stack[-1][0] >= depth:
                stack.pop()
                
            if stack:
                stack[-1][1].children.append(node)
                
            stack.append((depth, node))
            
        return root

    def _extract_procedure(self, node: FlangASTNode, filepath: str) -> Optional[InterfaceProc]:
        # SubroutineStmt or FunctionStmt
        stmt_node = node.find_first("SubroutineStmt") or node.find_first("FunctionStmt")
        if not stmt_node:
            return None

        # Extract Fortran procedure name
        name_node = stmt_node.find_first("Name")
        fortran_name = name_node.value.replace("'", "") if name_node else "unknown"

        # Check LanguageBindingSpec for bind(c) and binding name
        binding_spec = stmt_node.find_first("LanguageBindingSpec")
        is_bind_c = (binding_spec is not None)
        binding_name = fortran_name
        
        if binding_spec:
            # Check for name literal inside ScalarCharConstantExpr
            char_expr = binding_spec.find_first("ScalarCharConstantExpr")
            if char_expr:
                binding_name = char_expr.value.replace("'", "").strip()

        is_function = (node.name in ["FunctionSubprogram", "Function"])

        # Collect dummy args
        args_order = []
        for child in stmt_node.children:
            if "dummyarg" in child.name.lower() or child.name == "Name":
                if child.name == "Name" and child == name_node:
                    continue  # Subroutine name itself
                val = child.value.replace("'", "").strip()
                if val:
                    args_order.append(val)

        # Parse type declaration statements under this subprogram
        # To map types to arguments, we collect TypeDeclarationStmt nodes
        type_decls = node.find_all("TypeDeclarationStmt")
        args_types = {}
        has_hidden_strlen = False

        for decl in type_decls:
            # 1. Parse base type spec
            type_spec_node = decl.find_first("DeclarationTypeSpec")
            if not type_spec_node:
                continue

            base_type = "unknown"
            kind_bytes = 4
            iso_name = None

            # Check TypeSpec kind
            int_spec = type_spec_node.find_first("IntegerTypeSpec") or type_spec_node.find_first("Integer")
            real_spec = type_spec_node.find_first("RealTypeSpec") or type_spec_node.find_first("Real")
            complex_spec = type_spec_node.find_first("ComplexTypeSpec") or type_spec_node.find_first("Complex")
            logical_spec = type_spec_node.find_first("LogicalTypeSpec") or type_spec_node.find_first("Logical")
            char_spec = type_spec_node.find_first("CharacterTypeSpec") or type_spec_node.find_first("Character")

            double_spec = type_spec_node.find_first("DoublePrecision")
            double_complex_spec = type_spec_node.find_first("DoubleComplex")

            pointer_depth = 0

            if int_spec:
                base_type = "integer"
            elif real_spec:
                base_type = "real"
            elif double_spec:
                base_type = "real"
                kind_bytes = 8
            elif complex_spec:
                base_type = "complex"
                kind_bytes = 8
            elif double_complex_spec:
                base_type = "complex"
                kind_bytes = 16
            elif logical_spec:
                base_type = "logical"
            elif char_spec:
                base_type = "character"
                kind_bytes = 1
            else:
                derived_spec = type_spec_node.find_first("DerivedTypeSpec")
                if derived_spec:
                    name_node = derived_spec.find_first("Name")
                    if name_node:
                        iso_name = name_node.value.replace("'", "").strip()
                        if iso_name in ["c_ptr", "c_funptr"]:
                            base_type = "integer"
                            kind_bytes = 8
                            pointer_depth = 1
                        else:
                            base_type = "struct"

            # Check if there is a Kind expression
            kind_node = type_spec_node.find_first("KindSelector") or type_spec_node.find_first("Kind") or type_spec_node.find_first("CharSelector")
            if kind_node:
                # Value could be c_int, c_double, etc.
                val_node = kind_node.find_first("Name") or kind_node.find_first("Constant")
                if val_node:
                    iso_name = val_node.value.replace("'", "").strip()
                    iso_info = get_fortran_iso_type(iso_name, self.platform)
                    if iso_info:
                        base_type, kind_bytes = iso_info

            # 2. Parse AttrSpecs (Value, Intent, Pointer, Optional, Dimension)
            attr_nodes = decl.find_all("AttrSpec")
            is_value = any("value" in a.name.lower() for a in attr_nodes)
            is_pointer = any("pointer" in a.name.lower() for a in attr_nodes)
            is_optional = any("optional" in a.name.lower() for a in attr_nodes)
            is_const = any("intent(in)" in a.name.lower() or ("in" in a.name.lower() and "out" not in a.name.lower()) for a in attr_nodes)
            
            # 3. EntityDecl representing variables
            entities = decl.find_all("EntityDecl")
            for ent in entities:
                ent_name_node = ent.find_first("Name")
                if not ent_name_node:
                    continue
                ent_name = ent_name_node.value.replace("'", "").strip()

                # Determine if it is an array
                is_array = any("dimension" in a.name.lower() or "arrayspec" in a.name.lower() for a in attr_nodes)
                rank = 1
                is_assumed = False
                array_spec = ent.find_first("ArraySpec") or decl.find_first("ArraySpec")
                if array_spec:
                    is_array = True
                    rank_node = array_spec.find_first("int")
                    if rank_node:
                        val = rank_node.value.replace("'", "").strip()
                        if val.isdigit():
                            rank = int(val)
                        else:
                            rank = len(array_spec.find_all("Dimension")) or 1
                    else:
                        rank = len(array_spec.find_all("Dimension")) or 1
                    is_assumed = ":" in str(array_spec.find_all("Dimension")) or "deferred" in array_spec.name.lower()

                # Set parameters
                if base_type == "struct":
                    param_type = StructType(
                        name=iso_name,
                        fields=[],
                        is_bind_c=is_bind_c,
                        is_optional=is_optional
                    )
                else:
                    param_type = ScalarType(
                        base=base_type,
                        kind_bytes=kind_bytes,
                        is_pointer=is_pointer or pointer_depth > 0,
                        pointer_depth=1 if is_pointer else pointer_depth,
                        is_value=is_value,
                        is_optional=is_optional,
                        iso_name=iso_name,
                        is_const=is_const
                    )

                if is_array:
                    args_types[ent_name] = ArrayType(
                        element=param_type,
                        rank=rank,
                        shape=[None] * rank,
                        is_assumed_shape=is_assumed,
                        is_optional=is_optional
                    )
                else:
                    args_types[ent_name] = param_type

                # Check character length hidden argument
                is_star = (type_spec_node.find_first("Star") is not None)
                if base_type == "character" and (is_star or not is_bind_c):
                    has_hidden_strlen = True

        params = []
        for arg in args_order:
            if arg in args_types:
                params.append((arg, args_types[arg]))

        # Return type for function
        return_type = None
        if is_function:
            # Return type is often declared with the same name as the function
            if fortran_name.lower() in args_types:
                return_type = args_types[fortran_name.lower()]
            else:
                m_res = re.search(r"result\s*\(\s*([a-z0-9_]+)\s*\)", stmt_node.value, re.IGNORECASE)
                if m_res:
                    res_name = m_res.group(1).lower()
                    if res_name in args_types:
                        return_type = args_types[res_name]

        proc = InterfaceProc(
            name=binding_name,
            source_file=filepath,
            source_line=stmt_node.find_first("Line") or 0,
            return_type=return_type,
            params=params,
            is_function=is_function
        )
        proc.fortran_name = fortran_name
        proc.is_bind_c = is_bind_c
        proc.has_hidden_strlen = has_hidden_strlen

        return proc

def parse_fortran_file_flang(filepath: str, platform: str = "lp64", raise_on_error: bool = True) -> List[InterfaceProc]:
    parser = FlangParser(platform)
    return parser.parse_file(filepath, raise_on_error=raise_on_error)
