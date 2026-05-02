! interface.f90
subroutine mat_scale(a, m, n, alpha) bind(c, name="mat_scale")
  use iso_c_binding
  implicit none
  integer(c_int), intent(in), value :: m, n
  real(c_double), intent(inout) :: a(m, n)   ! column-major: a(i,j) at (j-1)*m+(i-1)
  real(c_double), intent(in), value :: alpha
end subroutine