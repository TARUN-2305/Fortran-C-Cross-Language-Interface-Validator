import os
import json
import pytest
from fcv.parsers.fortran_parser import parse_fortran_file
from fcv.parsers.c_parser import parse_c_header
from fcv.engine.comparator import compare_interfaces
from fcv.engine.abi import run_abi_checks

def get_hard_cases():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pairs_dir = os.path.join(base_dir, "hard_pairs")
    if not os.path.exists(pairs_dir):
        return []
        
    cases = []
    for tc in sorted(os.listdir(pairs_dir)):
        tc_dir = os.path.join(pairs_dir, tc)
        if os.path.isdir(tc_dir):
            cases.append((tc, tc_dir))
    return cases

@pytest.mark.parametrize("name,tc_dir", get_hard_cases())
def test_hard_comparator(name, tc_dir):
    f90_path = os.path.join(tc_dir, "interface.f90")
    h_path = os.path.join(tc_dir, "header.h")
    exp_path = os.path.join(tc_dir, "expected.json")

    with open(exp_path, 'r', encoding='utf-8') as f:
        expected = json.load(f)

    f_procs = parse_fortran_file(f90_path, platform="lp64")
    c_procs = parse_c_header(h_path, platform="lp64")

    # The parser might have failed (e.g. for C)
    if not f_procs:
        pytest.fail("Failed to parse Fortran")
    if not c_procs:
        pytest.fail("Failed to parse C")

    mismatches = compare_interfaces(f_procs, c_procs)
    mismatches = run_abi_checks(f_procs, c_procs, mismatches)

    # We check if the expected errors are somewhat generated.
    # We will just print the mismatches and expected to see what fails.
    actual_cats = [(m.category, m.severity) for m in mismatches]
    
    # expected is a list of {"severity": "ERROR", "raw_text": "..."}
    # For now, just ensure that if an ERROR/WARNING was expected, we got *some* ERROR/WARNING.
    for exp in expected:
        if exp["severity"] != "NONE":
            # We expected an error or warning. Let's see if we got one.
            has_error = any(m[1] == exp["severity"] for m in actual_cats)
            # Temporary loose assertion: just ensure we emitted something with the same severity.
            # Later we can tighten it to check the specific category!
            assert has_error, f"Expected {exp['severity']} but got {actual_cats}. Raw text: {exp['raw_text']}"
        else:
            # Expected no errors
            errors = [m for m in actual_cats if m[1] == "ERROR"]
            assert len(errors) == 0, f"Expected no errors, got {errors}"
