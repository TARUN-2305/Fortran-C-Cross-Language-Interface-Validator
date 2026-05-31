! interface.f90
subroutine solve_opts(a, n, tol, max_iter) bind(c, name="solve_opts")
  use iso_c_binding
  implicit none
  real(c_double), intent(inout) :: a(n, n)
  integer(c_int), intent(in), value :: n
  real(c_double), intent(in), optional :: tol       ! NULL if absent
  integer(c_int), intent(in), optional :: max_iter  ! NULL if absent
end subroutine