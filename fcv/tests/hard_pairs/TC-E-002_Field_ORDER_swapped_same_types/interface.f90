! interface.f90
type, bind(c) :: particle
  real(c_double)  :: mass      ! field 0
  real(c_double)  :: charge    ! field 1
  integer(c_int)  :: id        ! field 2
end type
  interface
    subroutine dummy_proc(x) bind(c)
      import :: particle
      type(particle), intent(in) :: x
    end subroutine
  end interface
