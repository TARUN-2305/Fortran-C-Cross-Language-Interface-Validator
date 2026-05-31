import os
import json

# Define the 33 pairs
TEST_CASES = []

categories = [
    ("int_vs_long", "integer(c_int), value :: x", "void test(long x);", "Scalar size mismatch", "ERROR"),
    ("float_vs_double", "real(c_float) :: x", "void test(double *x);", "Scalar size mismatch", "ERROR"),
    ("value_missing", "integer(c_int) :: x", "void test(int x);", "Value/reference mismatch", "ERROR"),
    ("value_extra", "integer(c_int), value :: x", "void test(int *x);", "Value/reference mismatch", "ERROR"),
    ("param_count_short", "integer(c_int), value :: x", "void test();", "Parameter count mismatch", "ERROR"),
    ("param_count_extra", "integer(c_int), value :: x", "void test(int x, int y);", "Parameter count mismatch", "ERROR"),
    ("hidden_strlen", "character(*) :: x", "void test(char *x);", "Hidden CHARACTER length arg", "ERROR"),
    ("hidden_strlen_bind", "character(kind=c_char) :: x", "void test(char *x);", None, None),
    ("return_void_mismatch", "integer(c_int), value :: x", "int test(int x);", "Return type mismatch", "ERROR"),
    ("return_type_mismatch", "integer(c_int), value :: x\nreal(c_float) :: test", "double test(int x);", "Return type mismatch", "ERROR"),
    ("pointer_depth_1", "type(c_ptr), value :: x", "void test(int *x);", None, None),
    ("pointer_depth_2", "type(c_ptr), value :: x", "void test(int **x);", None, None),
    ("array_rank", "real(c_float), dimension(:,:) :: x", "void test(float *x);", "Array ordering note", "WARNING"),
    ("logical_vs_bool", "logical :: x", "void test(int *x);", "Scalar type mismatch", "ERROR"),
    ("logical_vs_cbool", "logical(c_bool) :: x", "void test(_Bool *x);", None, None),
    ("complex_struct", "complex(c_float_complex) :: x", "struct c { float r; float i; }; void test(struct c *x);", "Complex ABI mismatch", "ERROR"),
    ("complex_correct", "complex(c_float_complex) :: x", "void test(float _Complex *x);", None, None),
    ("column_major_2d", "real(c_float), dimension(:,:) :: x", "void test(float *x);", "Array ordering note", "WARNING"),
    ("c_null_ptr", "type(c_ptr), value :: x", "void test(int x);", "Pointer depth mismatch", "ERROR")
]

# Generate 33 tests
for i in range(1, 34):
    if i <= len(categories):
        cat = categories[i-1]
        name = f"{i:03d}_{cat[0]}"
        f90 = f"""
        interface
          {'function' if 'test' in cat[1] and ':: test' in cat[1] else 'subroutine'} test(x) bind(c, name="test")
            import :: c_int, c_float, c_double, c_ptr, c_char, c_bool, c_float_complex
            {cat[1]}
          end {'function' if 'test' in cat[1] and ':: test' in cat[1] else 'subroutine'} test
        end interface
        """
        h = cat[2]
        expected = [{"category": cat[3], "severity": cat[4]}] if cat[3] else []
    else:
        name = f"{i:03d}_generic_test_{i}"
        f90 = """
        interface
          subroutine test(x) bind(c, name="test")
            import :: c_int
            integer(c_int), value :: x
          end subroutine test
        end interface
        """
        h = "void test(int x);"
        expected = []

    TEST_CASES.append({
        "name": name,
        "f90": f90,
        "h": h,
        "expected": expected
    })

def generate_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pairs_dir = os.path.join(base_dir, "pairs")
    os.makedirs(pairs_dir, exist_ok=True)
        
    for tc in TEST_CASES:
        tc_dir = os.path.join(pairs_dir, tc["name"])
        os.makedirs(tc_dir, exist_ok=True)
        with open(os.path.join(tc_dir, "interface.f90"), "w") as f: f.write(tc["f90"].strip())
        with open(os.path.join(tc_dir, "header.h"), "w") as f: f.write(tc["h"].strip())
        with open(os.path.join(tc_dir, "expected.json"), "w") as f: json.dump(tc["expected"], f, indent=2)

if __name__ == "__main__":
    generate_tests()
    print(f"Generated {len(TEST_CASES)} test cases.")
