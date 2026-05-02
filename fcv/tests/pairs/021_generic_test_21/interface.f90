interface
          subroutine test(x) bind(c, name="test")
            import :: c_int
            integer(c_int), value :: x
          end subroutine test
        end interface