! interface.f90
type :: inner_t          ! No BIND(C)
  integer :: a, b
end type

type, bind(c) :: outer_t  ! BIND(C) — but contains non-interoperable inner!
  type(inner_t) :: inner
  real(c_double) :: val
end type
  interface
    subroutine dummy_proc(x) bind(c)
      import :: outer_struct
      type(outer_struct), intent(in) :: x
    end subroutine
  end interface
