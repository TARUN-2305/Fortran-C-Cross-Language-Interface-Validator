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
