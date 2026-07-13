from typing import List, Dict
import sys

from fcv.ir.types import InterfaceProc, ScalarType, ArrayType, StructType, AnyType
from fcv.engine.comparator import Mismatch
from fcv.report.severity import Severity

class ABIChecker:
    def __init__(self):
        pass

    def check_interfaces(self, f_procs: List[InterfaceProc], c_procs: List[InterfaceProc], mismatches: List[Mismatch]) -> List[Mismatch]:
        """
        Performs ABI-specific checks that go beyond structural type comparison.
        Appends to and returns the list of mismatches.
        """
        c_proc_map = {p.name.lower(): p for p in c_procs}
        
        # 1. Complex Number ABI Check
        for f_proc in f_procs:
            if f_proc.name.lower() in c_proc_map:
                c_proc = c_proc_map[f_proc.name.lower()]
                for i, (f_param_name, f_type) in enumerate(f_proc.params):
                    if i < len(c_proc.params):
                        c_param_name, c_type = c_proc.params[i]
                        
                        # Complex number ABI
                        if isinstance(f_type, ScalarType) and f_type.base == "complex":
                            if isinstance(c_type, StructType) and not f_type.is_value:
                                exists = any(m.proc_name == f_proc.name and m.category == "COMPLEX_ABI_MISMATCH" for m in mismatches)
                                if not exists:
                                    mismatches.append(Mismatch(
                                        "COMPLEX_ABI_MISMATCH", Severity.ERROR,
                                        f"Parameter '{f_param_name}' is Fortran COMPLEX but C uses a struct instead of _Complex",
                                        f_proc.name, "complex", "struct"
                                    ))
                                
                        # Array Ordering Warning
                        if isinstance(f_type, ArrayType) and f_type.rank > 1:
                            exists = any(m.proc_name == f_proc.name and m.category == "ARRAY_ORDERING_NOTE" for m in mismatches)
                            if not exists:
                                mismatches.append(Mismatch(
                                    "ARRAY_ORDERING_NOTE", Severity.WARNING,
                                    f"Parameter '{f_param_name}' is a multi-dimensional array. Note that Fortran is column-major while C is row-major.",
                                    f_proc.name, f"array(rank={f_type.rank})", "pointer"
                                ))

        # 2. Symbol Name Mangling Warning
        f_proc_names = {p.name.lower() for p in f_procs}
        for c_proc in c_procs:
            if c_proc.name.endswith("_") and c_proc.name.lower() not in f_proc_names:
                exists = any(m.proc_name == c_proc.name and m.category == "SYMBOL_NAME_MANGLING" for m in mismatches)
                if not exists:
                    mismatches.append(Mismatch(
                        "SYMBOL_NAME_MANGLING", Severity.WARNING,
                        f"C function '{c_proc.name}' ends with an underscore. This usually indicates a mangled Fortran name rather than a proper BIND(C) interface.",
                        c_proc.name
                    ))

        # 3. Calling Convention Mismatch
        for f_proc in f_procs:
            if f_proc.name.lower() in c_proc_map:
                c_proc = c_proc_map[f_proc.name.lower()]
                # Heuristic: Check if the C source file has __stdcall for this procedure
                if c_proc.source_file:
                    try:
                        with open(c_proc.source_file, 'r', encoding='utf-8') as f:
                            c_source = f.read()
                            if "__stdcall" in c_source and f_proc.name in c_source:
                                exists = any(m.proc_name == f_proc.name and m.category == "WINDOWS_CALLING_CONV" for m in mismatches)
                                if not exists:
                                    mismatches.append(Mismatch(
                                        "WINDOWS_CALLING_CONV", Severity.WARNING,
                                        "On 32-bit Windows, Fortran DLLs may use __stdcall convention; C defaults to __cdecl. Stack pointer will be corrupted after each call if conventions differ. BIND(C) mandates C calling convention (__cdecl) but verify your Fortran compiler honours this on Win32.",
                                        f_proc.name
                                    ))
                    except (OSError, IOError) as e:
                        print(f"[Warning] Failed to read source file {c_proc.source_file} for ABI stdcall check: {e}", file=sys.stderr)

        return mismatches

def run_abi_checks(f_procs: List[InterfaceProc], c_procs: List[InterfaceProc], mismatches: List[Mismatch]) -> List[Mismatch]:
    checker = ABIChecker()
    return checker.check_interfaces(f_procs, c_procs, mismatches)
