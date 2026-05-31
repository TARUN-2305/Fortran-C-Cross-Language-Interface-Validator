! interface.f90
subroutine high_prec_sum(x, n, result) bind(c, name="high_prec_sum")
  use iso_c_binding
  implicit none
  real(c_long_double), intent(in)  :: x(n)
  integer(c_int), intent(in), value :: n
  real(c_long_double), intent(out) :: result
end subroutine