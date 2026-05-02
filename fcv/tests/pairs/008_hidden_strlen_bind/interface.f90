interface
          subroutine test(x) bind(c, name="test")
            import :: c_int, c_float, c_double, c_ptr, c_char, c_bool, c_float_complex
            character(kind=c_char) :: x
          end subroutine test
        end interface