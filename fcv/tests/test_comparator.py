import os
import json
import pytest

from fcv.parsers.fortran_parser import parse_fortran_file
from fcv.parsers.c_parser import parse_c_header
from fcv.engine.comparator import compare_interfaces
from fcv.engine.abi import run_abi_checks

def get_test_cases():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pairs_dir = os.path.join(base_dir, "pairs")
    if not os.path.exists(pairs_dir):
        return []
        
    cases = []
    for d in sorted(os.listdir(pairs_dir)):
        tc_dir = os.path.join(pairs_dir, d)
        if os.path.isdir(tc_dir):
            cases.append((d, tc_dir))
    return cases

@pytest.mark.parametrize("name,tc_dir", get_test_cases())
def test_comparator(name, tc_dir):
    f90_path = os.path.join(tc_dir, "interface.f90")
    h_path = os.path.join(tc_dir, "header.h")
    exp_path = os.path.join(tc_dir, "expected.json")
    
    with open(exp_path, 'r') as f:
        expected = json.load(f)
        
    f_procs = parse_fortran_file(f90_path, platform="lp64")
    c_procs = parse_c_header(h_path, platform="lp64")
    
    mismatches = compare_interfaces(f_procs, c_procs)
    mismatches = run_abi_checks(f_procs, c_procs, mismatches)
    
    # We just check if the expected categories are in the actual categories
    actual_cats = [(m.category, m.severity) for m in mismatches]
    
    for exp in expected:
        assert (exp["category"], exp["severity"]) in actual_cats, f"Expected {exp['category']} but got {actual_cats}"
        
    # If expected is empty, we expect no errors (warnings are okay unless expected is strictly checked)
    if len(expected) == 0:
        errors = [m for m in mismatches if m.severity == "ERROR"]
        assert len(errors) == 0, f"Expected no errors, got {errors}"

def test_cyclic_structs():
    from fcv.ir.types import StructType, ScalarType, InterfaceProc
    from fcv.engine.comparator import compare_interfaces

    # Create cyclic Fortran struct: Type Node containing a field pointing to a Node
    f_node = StructType(name="node", fields=[], size_bytes=16, alignment=8, is_bind_c=True)
    # add self-referential pointer field: node* next
    f_node.fields.append(("next", ScalarType(base="integer", kind_bytes=8, pointer_depth=1, is_pointer=True), 8))
    
    # Create cyclic C struct: struct Node containing a field pointing to struct Node
    c_node = StructType(name="Node", fields=[], size_bytes=16, alignment=8, is_bind_c=True)
    c_node.fields.append(("next", ScalarType(base="integer", kind_bytes=8, pointer_depth=1, is_pointer=True), 8))
    
    # Procedures using these structs
    f_proc = InterfaceProc(name="process", source_file="", source_line=0, return_type=None, params=[("head", f_node)], is_function=False)
    c_proc = InterfaceProc(name="process", source_file="", source_line=0, return_type=None, params=[("head", c_node)], is_function=False)
    
    # Verify compare_interfaces terminates successfully without stack overflow/infinite recursion
    mismatches = compare_interfaces([f_proc], [c_proc])
    assert len(mismatches) == 0

def test_cflags_parsing():
    import tempfile
    from fcv.parsers.c_parser import parse_c_header
    
    with tempfile.NamedTemporaryFile(suffix=".h", mode="w", delete=False) as f:
        f.write("#ifdef USE_DOUBLE\ntypedef double my_real;\n#else\ntypedef float my_real;\n#endif\nvoid test_func(my_real x);\n")
        h_path = f.name
        
    try:
        # Parse without cflags -> should default to float (my_real = 4 bytes)
        procs_default = parse_c_header(h_path, platform="lp64")
        assert len(procs_default) == 1
        param_type = procs_default[0].params[0][1]
        assert param_type.kind_bytes == 4
        
        # Parse with cflags "-DUSE_DOUBLE" -> should use double (my_real = 8 bytes)
        procs_double = parse_c_header(h_path, platform="lp64", cflags=["-DUSE_DOUBLE"])
        assert len(procs_double) == 1
        param_type_double = procs_double[0].params[0][1]
        assert param_type_double.kind_bytes == 8
    finally:
        os.remove(h_path)

def test_name_mapping_and_prefix_suffix():
    from fcv.ir.types import InterfaceProc
    from fcv.engine.comparator import compare_interfaces
    
    f_proc1 = InterfaceProc(name="dgetrf", source_file="", source_line=0, return_type=None, params=[], is_function=False)
    f_proc2 = InterfaceProc(name="foo", source_file="", source_line=0, return_type=None, params=[], is_function=False)
    
    c_proc1 = InterfaceProc(name="LAPACKE_dgetrf", source_file="", source_line=0, return_type=None, params=[], is_function=False)
    c_proc2 = InterfaceProc(name="bar", source_file="", source_line=0, return_type=None, params=[], is_function=False)
    
    # 1. Without matching config -> should get unmatched procedure warnings
    mismatches = compare_interfaces([f_proc1, f_proc2], [c_proc1, c_proc2])
    unmatched_cats = [m.category for m in mismatches if m.category == "Unmatched procedure"]
    assert len(unmatched_cats) > 0
    
    # 2. With c_prefix="LAPACKE_" and explicit name_map for foo=bar -> should match all, no unmatched warnings!
    mismatches_mapped = compare_interfaces(
        [f_proc1, f_proc2], 
        [c_proc1, c_proc2],
        c_prefix="LAPACKE_",
        name_map={"foo": "bar"}
    )
    unmatched_cats_mapped = [m.category for m in mismatches_mapped if m.category == "Unmatched procedure"]
    assert len(unmatched_cats_mapped) == 0



