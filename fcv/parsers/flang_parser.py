import subprocess
import os
import re
import sys
from typing import List, Optional, Tuple, Dict, Any

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, AnyType
from fcv.ir.type_map import get_fortran_iso_type
from fcv.parsers.fortran_parser import FortranParser, parse_fortran_file
from fcv.parsers.gfortran_parser import GfortranParser, _gfortran_binary


def fortran_parser_backend_name() -> str:
    """Return a human-readable name for the Fortran parser backend that will be used."""
    try:
        result = subprocess.run(
            ["flang-new", "--version"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return "flang-new (LLVM Flang compiler frontend)"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
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
        if self.name.lower() == name.lower():
            result.append(self)
        for child in self.children:
            result.extend(child.find_all(name))
        return result

    def find_first(self, name: str) -> Optional['FlangASTNode']:
        if self.name.lower() == name.lower():
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
        # Attempt to run flang-new to get the parse tree
        try:
            result = subprocess.run(
                ["flang-new", "-fc1", "-fdebug-dump-parse-tree", filepath],
                capture_output=True,
                text=True,
                check=True
            )
            output = result.stdout
            return self._parse_flang_ast(output, filepath)
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            if raise_on_error:
                raise RuntimeError(
                    f"Error: flang-new is not installed or failed to run, "
                    f"but --use-flang was explicitly requested.\n"
                    f"Please make sure flang-new is available in your PATH.\nDetails: {e}"
                )
            # Fallback 1: gfortran (real compiler, better than regex)
            gfortran = GfortranParser(self.platform)
            if gfortran.available:
                print(
                    "INFO: flang-new not found. Using gfortran compiler frontend.",
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

        # Find SubroutineSubprogram and FunctionSubprogram nodes
        subprogram_nodes = root.find_all("SubroutineSubprogram") + root.find_all("FunctionSubprogram")

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
            if not line.strip():
                continue
            leading_spaces = len(line) - len(line.lstrip())
            content = line.strip()
            
            if "=" in content:
                name, val = content.split("=", 1)
                node = FlangASTNode(name, val)
            else:
                node = FlangASTNode(content)
                
            while stack and stack[-1][0] >= leading_spaces:
                stack.pop()
                
            if stack:
                stack[-1][1].children.append(node)
                
            stack.append((leading_spaces, node))
            
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

        is_function = (node.name == "FunctionSubprogram")

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
            int_spec = type_spec_node.find_first("IntegerTypeSpec")
            real_spec = type_spec_node.find_first("RealTypeSpec")
            complex_spec = type_spec_node.find_first("ComplexTypeSpec")
            logical_spec = type_spec_node.find_first("LogicalTypeSpec")
            char_spec = type_spec_node.find_first("CharacterTypeSpec")

            if int_spec:
                base_type = "integer"
            elif real_spec:
                base_type = "real"
            elif complex_spec:
                base_type = "complex"
            elif logical_spec:
                base_type = "logical"
            elif char_spec:
                base_type = "character"
                kind_bytes = 1

            # Check if there is a Kind expression
            kind_node = type_spec_node.find_first("Kind")
            if kind_node:
                # Value could be c_int, c_double, etc.
                val_node = kind_node.find_first("Name") or kind_node.find_first("Constant")
                if val_node:
                    iso_name = val_node.value.replace("'", "").strip()
                    iso_info = get_fortran_iso_type(iso_name, self.platform)
                    if iso_info:
                        base_type, kind_bytes = iso_info

            # 2. Parse AttrSpecs (Value, Intent, Pointer, Optional, Dimension)
            attrs = [a.name.lower() for a in decl.find_all("AttrSpec")]
            is_value = "value" in attrs
            is_pointer = "pointer" in attrs
            is_optional = "optional" in attrs
            is_const = any("intent(in)" in a or ("in" in a and "out" not in a) for a in attrs)
            
            # 3. EntityDecl representing variables
            entities = decl.find_all("EntityDecl")
            for ent in entities:
                ent_name_node = ent.find_first("Name")
                if not ent_name_node:
                    continue
                ent_name = ent_name_node.value.replace("'", "").strip()

                # Determine if it is an array
                is_array = "dimension" in attrs
                rank = 1
                is_assumed = False
                array_spec = ent.find_first("ArraySpec")
                if array_spec:
                    is_array = True
                    # Rank is determined by number of dimensions
                    rank = len(array_spec.find_all("Dimension")) or 1
                    is_assumed = ":" in str(array_spec.find_all("Dimension"))

                # Set parameters
                param_type = ScalarType(
                    base=base_type,
                    kind_bytes=kind_bytes,
                    is_pointer=is_pointer,
                    pointer_depth=1 if is_pointer else 0,
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
                if base_type == "character" and not is_bind_c:
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
