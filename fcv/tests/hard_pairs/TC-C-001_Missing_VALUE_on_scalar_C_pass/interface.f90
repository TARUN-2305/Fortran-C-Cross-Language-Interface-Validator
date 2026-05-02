! interface.f90
subroutine scale_array(x, n, alpha) bind(c, name="scale_array")
  use iso_c_binding
  implicit none
  real(c_double), intent(inout) :: x(n)
  integer(c_int), intent(in)    :: n       ! MISSING VALUE — expects pointer
  real(c_double), intent(in)    :: alpha   ! MISSING VALUE — expects pointer
end subroutine