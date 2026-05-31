! interface.f90
subroutine solver(x, n) bind(c, name="solver_")   ! explicit underscore
  use iso_c_binding
  implicit none
  real(c_double), intent(inout) :: x(n)
  integer(c_int), intent(in), value :: n
end subroutine