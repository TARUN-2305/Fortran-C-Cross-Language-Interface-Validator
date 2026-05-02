! interface.f90
subroutine get_values(cproc) bind(c, name="get_values")
  use iso_c_binding
  implicit none
  type(c_funptr), intent(in), value :: cproc
end subroutine