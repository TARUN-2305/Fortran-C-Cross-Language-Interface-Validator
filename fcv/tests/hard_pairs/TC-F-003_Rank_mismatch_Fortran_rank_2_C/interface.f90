! interface.f90
subroutine lu_factor(a, lda, n, ipiv, info) bind(c, name="lu_factor")
  use iso_c_binding
  implicit none
  integer(c_int), intent(in), value :: lda, n
  real(c_double), intent(inout) :: a(lda, n)  ! explicit-shape rank-2
  integer(c_int), intent(out) :: ipiv(n)
  integer(c_int), intent(out) :: info
end subroutine