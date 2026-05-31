! interface.f90
subroutine apply_phase(data, n, phase) bind(c, name="apply_phase")
  use iso_c_binding
  implicit none
  complex(c_double_complex), intent(inout) :: data(n)
  integer(c_int), intent(in), value :: n
  complex(c_double_complex), intent(in), value :: phase
end subroutine