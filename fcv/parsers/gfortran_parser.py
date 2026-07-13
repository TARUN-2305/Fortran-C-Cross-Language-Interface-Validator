"""
GfortranParser: Uses `gfortran -fdump-fortran-original` to extract a compiler-native
AST for Fortran source files (including fixed-form Fortran 77 and free-form Fortran 90/95/2003/2008),
then maps it to FCValidator IR.
"""

import subprocess
import os
import re
import tempfile
import sys
from typing import List, Optional, Dict, Tuple

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, AnyType
from fcv.parsers.fortran_parser import FortranParser


def _gfortran_binary() -> Optional[str]:
    """Return path to gfortran if available, else None."""
    for name in ("gfortran", "gfortran-15", "gfortran-14", "gfortran-13", "gfortran-12", "gfortran-11"):
        try:
            result = subprocess.run(["which", name], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
        except FileNotFoundError:
            pass
    return None


def _type_from_gfortran_spec(spec_str: str) -> Tuple[str, int]:
    if not spec_str:
        return "integer", 4
    spec_str = spec_str.upper()
    if "REAL" in spec_str:
        base = "real"
    elif "INTEGER" in spec_str:
        base = "integer"
    elif "COMPLEX" in spec_str:
        base = "complex"
    elif "LOGICAL" in spec_str:
        base = "logical"
    elif "CHARACTER" in spec_str:
        base = "character"
    else:
        base = "integer"
        
    parts = spec_str.split()
    kind = 4
    if len(parts) > 1:
        try:
            kind = int(parts[1])
        except ValueError:
            pass
            
    return base, kind


class GfortranParser:
    """
    Invokes gfortran's Fortran front-end to get a compiler-native parse tree,
    then extracts procedure interfaces from it.
    """

    def __init__(self, platform: str = "lp64"):
        self.platform = platform
        self._gfortran = _gfortran_binary()

    @property
    def available(self) -> bool:
        return self._gfortran is not None

    def parse_file(self, filepath: str, raise_on_error: bool = False) -> List[InterfaceProc]:
        if not self.available:
            if raise_on_error:
                raise RuntimeError(
                    "gfortran is not installed. Install it with: sudo apt-get install gfortran"
                )
            print(
                "WARNING: gfortran not found in PATH. Falling back to regex Fortran parser.",
                file=sys.stderr
            )
            return FortranParser(self.platform).parse_file(filepath)

        # Run gfortran with -fdump-fortran-original
        # Note: gfortran prints the dump output directly to stdout when combined with -fsyntax-only
        ext = os.path.splitext(filepath)[1].lower()
        cmd = [
            self._gfortran,
            "-fsyntax-only",
            "-fdump-fortran-original",
            "-fno-second-underscore"
        ]
        if ext in (".f", ".for", ".ftn"):
            cmd.append("-ffixed-form")
        else:
            cmd.append("-ffree-form")
        cmd.append(filepath)

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        # If gfortran failed to parse, fall back to regex parser unless raise_on_error is True
        if result.returncode != 0 or not result.stdout.strip():
            if raise_on_error:
                raise RuntimeError(
                    f"gfortran failed to parse {filepath}.\nStderr: {result.stderr}"
                )
            print(
                f"WARNING: gfortran failed to compile/dump {filepath} (code {result.returncode}). "
                f"Falling back to regex parser.",
                file=sys.stderr
            )
            return FortranParser(self.platform).parse_file(filepath)

        return self._parse_dump(result.stdout, filepath)

    def _parse_dump(self, dump: str, filepath: str) -> List[InterfaceProc]:
        blocks = re.split(r'procedure name =', dump)
        procs: List[InterfaceProc] = []
        
        for block in blocks[1:]:
            lines = block.splitlines()
            if not lines:
                continue
            proc_name = lines[0].strip()
            
            # Parse symtrees within this procedure block
            symtrees = {}
            current_sym = None
            current_data = {"attributes": "", "type": None, "array_spec": None, "formal_args": []}
            
            # Estimate line number in the dump
            line_no = dump[:dump.find(block)].count("\n") + 1
            
            for line in lines[1:]:
                line_strip = line.strip()
                m_sym = re.match(r"symtree:\s*'([^']+)'\s+\|\|\s+symbol:\s*'([^']+)'", line_strip)
                if m_sym:
                    if current_sym:
                        symtrees[current_sym] = current_data
                    current_sym = m_sym.group(1)
                    current_data = {"attributes": "", "type": None, "array_spec": None, "formal_args": []}
                    continue
                
                if current_sym:
                    if "type spec :" in line_strip:
                        m_type = re.search(r"type spec\s*:\s*\(([^)]+)\)", line_strip)
                        if m_type:
                            current_data["type"] = m_type.group(1).strip()
                    elif "attributes:" in line_strip:
                        m_attr = re.search(r"attributes\s*:\s*\(([^)]+)\)", line_strip)
                        if m_attr:
                            current_data["attributes"] = m_attr.group(1).strip()
                    elif "Array spec:" in line_strip:
                        m_arr = re.search(r"Array spec\s*:\s*\(([^)]+)\)", line_strip)
                        if m_arr:
                            current_data["array_spec"] = m_arr.group(1).strip()
                    elif "Formal arglist:" in line_strip:
                        args = line_strip.replace("Formal arglist:", "").strip().split()
                        current_data["formal_args"] = args
                        
            if current_sym:
                symtrees[current_sym] = current_data
                
            proc_sym = symtrees.get(proc_name)
            if not proc_sym:
                continue
                
            args = proc_sym.get("formal_args", [])
            is_function = "FUNCTION" in proc_sym.get("attributes", "")
            is_bind_c = "BIND_C" in proc_sym.get("attributes", "") or "BIND(C)" in proc_sym.get("attributes", "")
            
            # Determine name binding
            abi_name = proc_name.lower()
            if not is_bind_c:
                abi_name += "_"
                
            # Parse return type if function
            return_type = None
            if is_function:
                ret_base, ret_kind = _type_from_gfortran_spec(proc_sym.get("type"))
                # Functions in Fortran default to by-value return
                return_type = ScalarType(
                    base=ret_base,
                    kind_bytes=ret_kind,
                    is_pointer=False,
                    pointer_depth=0,
                    is_value=True
                )
                
            params = []
            for arg in args:
                arg_data = symtrees.get(arg)
                if not arg_data:
                    # Fallback to general integer if missing
                    params.append((arg, ScalarType(base="integer", kind_bytes=4, is_pointer=True, pointer_depth=1)))
                    continue
                    
                base, kind = _type_from_gfortran_spec(arg_data["type"])
                attrs = arg_data["attributes"]
                
                # Check value vs reference
                is_value = "VALUE" in attrs
                is_pointer = "POINTER" in attrs
                pointer_depth = 1 if is_pointer else 0
                is_const = "INTENT(IN)" in attrs or "IN" in attrs
                
                # Check array
                is_array = "DIMENSION" in attrs or arg_data["array_spec"] is not None
                if is_array:
                    rank = 1
                    is_assumed = False
                    if arg_data["array_spec"]:
                        m_rank = re.match(r"(\d+)\s+\[", arg_data["array_spec"])
                        if m_rank:
                            rank = int(m_rank.group(1))
                        # Only AS_ASSUMED_SHAPE represents modern BIND(C) descriptor array.
                        # AS_ASSUMED_SIZE representing F77 dummy arrays a(*) are passed as simple pointers.
                        is_assumed = "AS_ASSUMED_SHAPE" in arg_data["array_spec"]
                        
                    elem = ScalarType(base=base, kind_bytes=kind, is_pointer=False, pointer_depth=0, is_const=is_const)
                    arg_type = ArrayType(
                        element=elem,
                        rank=rank,
                        shape=[None] * rank,
                        is_assumed_shape=is_assumed
                    )
                else:
                    arg_type = ScalarType(
                        base=base,
                        kind_bytes=kind,
                        is_pointer=is_pointer,
                        pointer_depth=pointer_depth,
                        is_value=is_value,
                        is_const=is_const
                    )
                params.append((arg, arg_type))
                
            proc = InterfaceProc(
                name=abi_name,
                source_file=filepath,
                source_line=line_no,
                return_type=return_type,
                params=params,
                is_function=is_function
            )
            proc.fortran_name = proc_name
            proc.is_bind_c = is_bind_c
            procs.append(proc)
            
        return procs
