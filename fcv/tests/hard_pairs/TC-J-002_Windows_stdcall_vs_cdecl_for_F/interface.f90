! interface.f90 — Win32 DLL
subroutine compute(x, n) bind(c, name="compute")
  use iso_c_binding
  implicit none
  real(c_double), intent(inout) :: x(n)
  integer(c_int), intent(in), value :: n
end subroutine