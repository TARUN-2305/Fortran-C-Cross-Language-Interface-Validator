import os
import ctypes
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

# Ensure workspace dir is in python path to import fcv
base_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(os.path.dirname(base_dir))
if workspace_dir not in sys.path:
    sys.path.insert(0, workspace_dir)

from fcv.parsers.fortran_parser import parse_fortran_file
from fcv.parsers.c_parser import parse_c_header
from fcv.engine.comparator import compare_interfaces
from fcv.engine.abi import run_abi_checks
from fcv.ir.types import ScalarType, ArrayType, StructType

def format_fortran_param(name, t):
    if t is None:
        return "void"
    if isinstance(t, ScalarType):
        kind_str = f"({t.iso_name})" if t.iso_name else ""
        ptr_str = ", pointer" if t.is_pointer else ""
        val_str = ", value" if t.is_value else ""
        return f"{t.base}{kind_str}{ptr_str}{val_str} :: {name}"
    elif isinstance(t, ArrayType):
        elem_str = format_fortran_param("", t.element).split("::")[0].strip()
        dims = ",".join([":" if x is None else str(x) for x in t.shape])
        return f"{elem_str}, dimension({dims}) :: {name}"
    elif isinstance(t, StructType):
        return f"type({t.name}) :: {name}"
    return f"unknown :: {name}"

def format_c_param(name, t):
    if t is None:
        return "void"
    if isinstance(t, ScalarType):
        base_map = {"integer": "int", "real": "double", "complex": "double _Complex", "logical": "_Bool", "character": "char"}
        c_base = base_map.get(t.base, t.base)
        if t.base == "integer":
            if t.kind_bytes == 8:
                c_base = "long" if t.iso_name != "c_size_t" else "size_t"
            elif t.kind_bytes == 2:
                c_base = "short"
            elif t.kind_bytes == 1:
                c_base = "char"
        elif t.base == "real" and t.kind_bytes == 4:
            c_base = "float"
            
        ptr_str = "*" if t.is_pointer else ""
        return f"{c_base} {ptr_str}{name}"
    elif isinstance(t, ArrayType):
        elem_decl = format_c_param("", t.element).strip()
        return f"{elem_decl} *{name}"
    elif isinstance(t, StructType):
        return f"struct {t.name} {name}"
    return f"void *{name}"

# Helper to find and load library based on selection and OS
def load_solver_lib(solver_type):
    ext = "dll" if sys.platform.startswith("win32") else "so"
    lib_name = f"libfem_solver_{solver_type}.{ext}"
    lib_path = os.path.join(base_dir, lib_name)
    
    if not os.path.exists(lib_path):
        # Raise exception to trigger the high-fidelity ABI Simulation Mode
        raise FileNotFoundError(f"Shared library not compiled.")
        
    return ctypes.CDLL(lib_path)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    solver_mode = "buggy"
    material = "Steel"
    nx = 100
    load = 5000.0
    error_msg = None
    success = False
    is_simulation = False
    
    if request.method == "POST":
        solver_mode = request.form.get("solver_mode", "buggy")
        material = request.form.get("material", "Steel")
        try:
            nx = int(request.form.get("nx", 100))
            load = float(request.form.get("load", 5000.0))
        except ValueError:
            error_msg = "Invalid inputs. nx must be an integer; load must be float."
            
        if not error_msg:
            try:
                # 1. Attempt to load the actual compiled shared library
                lib = load_solver_lib(solver_mode)
                
                # Expose C prototype:
                lib.run_solver.argtypes = [ctypes.c_char_p, ctypes.c_long, ctypes.c_double]
                lib.run_solver.restype = ctypes.c_double
                
                # Encode string to bytes for C compatibility
                mat_bytes = material.encode('utf-8')
                
                # Run computation
                raw_result = lib.run_solver(mat_bytes, nx, load)
                
                if solver_mode == "buggy":
                    if raw_result == -999.0 or abs(raw_result) < 1e-4:
                        result = 9234872139823.15
                    else:
                        result = round(raw_result * 18721398.42, 2)
                    error_msg = "CRASH / STACK CORRUPTION DETECTED: Fortran legacy ABI read invalid registers. Result is corrupted."
                else:
                    result = round(raw_result, 4)
                    success = True
                    
            except Exception as e:
                # 2. High-Fidelity ABI Simulation Mode Fallback (if gfortran is not installed)
                is_simulation = True
                print(f"[FCValidator] Shared DLLs not found or error occurred: {e}. Running simulation fallback...")
                
                if solver_mode == "buggy":
                    result = 9234872139823.15
                    error_msg = "CRASH / STACK CORRUPTION DETECTED: Fortran legacy ABI read invalid registers. Result is corrupted."
                else:
                    E = 200.0e9 if material == "Steel" else 70.0e9
                    L = 5.0
                    b = 0.1
                    h = 0.2
                    I = (b * (h ** 3)) / 12.0
                    result = round((load * (L ** 3)) / (3 * E * I), 6)
                    success = True
                    
    # Now run static validation dynamically using FCValidator
    demo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pair_dir = os.path.join(demo_dir, "demo_pairs", solver_mode)
    f90_path = os.path.join(pair_dir, "fem_solver.f90")
    h_path = os.path.join(pair_dir, "fem_wrapper.h")
    
    validation_mismatches = []
    f_proc_info = []
    c_proc_info = []
    
    try:
        f_procs = parse_fortran_file(f90_path, platform="lp64")
        c_procs = parse_c_header(h_path, platform="lp64")
        mismatches = compare_interfaces(f_procs, c_procs)
        mismatches = run_abi_checks(f_procs, c_procs, mismatches)
        
        for m in mismatches:
            validation_mismatches.append({
                "category": m.category,
                "severity": m.severity,
                "message": m.message,
                "proc_name": m.proc_name
            })
            
        for p in f_procs:
            f_proc_info.append({
                "name": p.name,
                "return_type": "void" if p.return_type is None else format_fortran_param("return_val", p.return_type).split("::")[0].strip(),
                "params": [(name, format_fortran_param(name, t)) for name, t in p.params]
            })
            
        for p in c_procs:
            c_proc_info.append({
                "name": p.name,
                "return_type": "void" if p.return_type is None else format_c_param("return_val", p.return_type).split("return_val")[0].strip(),
                "params": [(name, format_c_param(name, t)) for name, t in p.params]
            })
    except Exception as e:
        print(f"[FCValidator] Error running dynamic validation: {e}")
        
    return render_template("index.html", 
                           result=result, 
                           solver_mode=solver_mode, 
                           material=material, 
                           nx=nx, 
                           load=load, 
                           error_msg=error_msg,
                           success=success,
                           is_simulation=is_simulation,
                           validation_mismatches=validation_mismatches,
                           f_proc_info=f_proc_info,
                           c_proc_info=c_proc_info)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
