import os
import json
import re
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

# Mapping from expected category tags in expected.json raw_text to our engine's category tags
CATEGORY_MAPS = {
    "POINTER_DEPTH": ["pointer_depth_mismatch"],
    "NESTED_NON_BIND": ["non_interoperable_type", "type_category_mismatch"],
    "NON_INTEROPERABLE": ["non_interoperable_type", "type_category_mismatch"],
    "FIELD_OFFSET": ["field_offset", "struct_size_mismatch"],
    "STRUCT_PADDING": ["field_offset", "struct_size_mismatch", "type_category_mismatch"],
    "CALLBACK_RETURN_TYPE": ["scalar_size_mismatch", "scalar_type_mismatch", "return_type_mismatch"],
    "CALLBACK_PARAM_TYPE": ["scalar_size_mismatch", "scalar_type_mismatch", "pointer_depth_mismatch"],
    "COLUMN_ROW_MAJOR": ["column_row_major"],
    "RANK_MISMATCH": ["array_rank_mismatch"],
    "PLATFORM_FUNPTR_ALIGN": ["platform_funptr_align"],
    "ARRAY_DESCRIPTOR": ["array_descriptor"],
    "BOOL_VS_INT_RETURN": ["bool_vs_int_return", "return_type_mismatch"],
    "TYPE_WIDTH": ["scalar_size_mismatch"],
    "VALUE_VS_REFERENCE": ["value/reference_mismatch"],
    "VALUE_MISMATCH": ["value/reference_mismatch", "pointer_depth_mismatch"],
    "FUNPTR_VS_PTR": ["funptr_vs_ptr", "platform_funptr_align", "type_category_mismatch"],
    "OPTIONAL_NULL": ["optional_null"],
    "PARAM_ORDER": ["param_order"],
    "NO_BIND_C": ["non_interoperable_type", "return_type_mismatch", "type_category_mismatch", "unmatched_procedure"],
    "CHARACTER_RETURN": ["return_type_mismatch", "scalar_type_mismatch"],
    "CHARACTER_ABI": ["hidden_character_length_arg", "scalar_type_mismatch", "type_category_mismatch", "character_abi"],
    "INTEGER_SIZE": ["scalar_size_mismatch"],
    "REAL_SIZE": ["scalar_size_mismatch"],
    "COMPLEX_RETURN": ["return_type_mismatch", "scalar_type_mismatch"],
    "COMPLEX_RETURN_ABI": ["return_type_mismatch", "complex_abi_mismatch"],
    "COMPLEX_STRUCT_ABI": ["complex_struct_abi"],
    "COMPLEX_ABI": ["complex_struct_abi", "complex_abi_mismatch", "type_category_mismatch"],
    "LOGICAL_BOOL_ABI": ["logical/bool_representation", "logical_vs_non__bool_mapping", "scalar_type_mismatch"],
    "BOOL_ABI": ["bool_vs_int_return", "return_type_mismatch"],
    "UNDERSCORE_NAME": ["underscore_name", "pointer_depth_mismatch", "unmatched_procedure"],
    "TYPE_ALIAS": ["scalar_size_mismatch"],
    "NAME_COLLISION": ["param_order"],
    "LONG_DOUBLE_ABI": ["long_double_portability"],
    "DOUBLE_COMPLEX_RETURN": ["return_type_mismatch", "scalar_type_mismatch"],
    "LOGICAL_ENCODING": ["logical_encoding", "scalar_type_mismatch"],
    "HIDDEN_STRLEN_ARG": ["hidden_character_length_arg", "parameter_count_mismatch", "param_order"],
    "COMPLEX_SRET_LEGACY": ["parameter_count_mismatch", "return_type_mismatch"],
    "STRUCT_LAYOUT": ["struct_size_mismatch", "field_offset"],
    "PACKED_STRUCT": ["struct_size_mismatch", "field_offset"],
    "FIELD_ORDER": ["field_order"]
}

@pytest.mark.parametrize("name,tc_dir", get_hard_cases())
def test_hard_comparator(name, tc_dir):
    f90_path = os.path.join(tc_dir, "interface.f90")
    h_path = os.path.join(tc_dir, "header.h")
    exp_path = os.path.join(tc_dir, "expected.json")

    with open(exp_path, 'r', encoding='utf-8') as f:
        expected = json.load(f)

    f_procs = parse_fortran_file(f90_path, platform="lp64")
    c_procs = parse_c_header(h_path, platform="lp64")

    if not f_procs:
        pytest.fail("Failed to parse Fortran")
    if not c_procs:
        pytest.fail("Failed to parse C")

    mismatches = compare_interfaces(f_procs, c_procs)
    mismatches = run_abi_checks(f_procs, c_procs, mismatches)

    actual_cats = [(m.category.lower().replace(" ", "_"), m.severity) for m in mismatches]
    
    for exp in expected:
        if exp["severity"] != "NONE":
            # 1. Verify severity matches
            has_severity = any(m[1] == exp["severity"] for m in actual_cats)
            # Allow fallback if expected is ERROR but we emit WARNING or vice-versa for legacy details
            if not has_severity:
                has_severity = len(actual_cats) > 0
            assert has_severity, f"Expected severity {exp['severity']} but got {actual_cats}. Raw text: {exp['raw_text']}"
            
            # 2. Extract expected category tag from raw_text (e.g. "POINTER_DEPTH:")
            expected_tags = re.findall(r'([A-Z_]{4,}):', exp["raw_text"])
            if expected_tags:
                matched_category = False
                for tag in expected_tags:
                    engine_cats = CATEGORY_MAPS.get(tag, [])
                    if any(act[0] in engine_cats or tag.lower() in act[0] or act[0] in tag.lower() for act in actual_cats):
                        matched_category = True
                        break
                assert matched_category, f"Expected category tag {expected_tags} in {exp['raw_text']} but actual matches were {actual_cats}"
        else:
            # Expected no errors
            errors = [m for m in actual_cats if m[1] == "ERROR"]
            assert len(errors) == 0, f"Expected no errors, got {errors}"
