import subprocess
import os
import re
from typing import List

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType
from fcv.ir.type_map import get_fortran_iso_type
from fcv.parsers.fortran_parser import FortranParser

class FlangParser:
    def __init__(self, platform: str = "lp64"):
        self.platform = platform

    def parse_file(self, filepath: str) -> List[InterfaceProc]:
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
        except FileNotFoundError:
            print("[Warning] 'flang-new' not found. Falling back to internal RegEx parser.")
            fallback = FortranParser(self.platform)
            return fallback.parse_file(filepath)
        except subprocess.CalledProcessError as e:
            print(f"[Error] flang-new failed: {e.stderr}")
            return []

    def _parse_flang_ast(self, ast_text: str, filepath: str) -> List[InterfaceProc]:
        # Here we would implement the exact AST traversal of Flang's debug-dump-parse-tree format.
        # Since Flang is not installed on this system, we provide a structured placeholder that 
        # normally walks the JSON/Text AST to extract SubroutineStmt, InterfaceStmt, and TypeDeclarationStmt.
        # For the sake of demonstration without the compiler, we defer to the regex parser if the output is empty or mock.
        
        # In a real environment with flang, we'd regex/parse the nested tree:
        # e.g., finding `SubroutineStmt` -> `Name = 'foo'`, then `LanguageBindingSpec -> 'c'`
        
        fallback = FortranParser(self.platform)
        return fallback.parse_file(filepath)

def parse_fortran_file_flang(filepath: str, platform: str = "lp64") -> List[InterfaceProc]:
    parser = FlangParser(platform)
    return parser.parse_file(filepath)
