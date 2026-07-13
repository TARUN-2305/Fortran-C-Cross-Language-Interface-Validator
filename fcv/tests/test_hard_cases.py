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

    actual_cats = [(m.category, m.severity) for m in mismatches]
    
    for exp in expected:
        if exp["severity"] != "NONE":
            matching_mismatches = [m for m in mismatches if m.severity == exp["severity"]]
            assert len(matching_mismatches) > 0, f"Expected severity {exp['severity']} but got none: {mismatches}"
            
            raw_text_upper = exp["raw_text"].upper()
            possible_categories = [
                "STRUCT_LAYOUT", "FIELD_ORDER", "NESTED_NON_BIND", 
                "NON_INTEROPERABLE_TYPE", "LOGICAL_IN_NON_BIND_TYPE",
                "PACKED_STRUCT", "HIDDEN_STRLEN_ARG", "PLATFORM_FUNPTR_ALIGN",
                "WINDOWS_CALLING_CONV", "BOOL_VS_INT_RETURN"
            ]
            for cat in possible_categories:
                if cat in raw_text_upper:
                    actual_cats_upper = [m.category.upper() for m in mismatches]
                    if cat == "HIDDEN_STRLEN_ARG":
                        has_cat = any(x in c for c in actual_cats_upper for x in ["HIDDEN_STRLEN_ARG", "HIDDEN_CHARACTER_LENGTH_ARG", "HIDDEN CHARACTER LENGTH ARG"])
                    else:
                        has_cat = any(cat in c or cat in m.message.upper() for m, c in zip(mismatches, actual_cats_upper))
                    assert has_cat, f"Expected mismatch category {cat} in actual mismatches, but it was not reported. Actual mismatches: {[(m.category, m.message) for m in mismatches]}"
        else:
            errors = [m for m in actual_cats if m[1] == "ERROR"]
            assert len(errors) == 0, f"Expected no errors, got {errors}"
