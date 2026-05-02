! interface.f90
subroutine lapack_solve(n, nrhs, a, lda, b, ldb, info) &
    bind(c, name="lapack_solve")
  use iso_c_binding
  implicit none
  integer(c_int64_t), intent(in), value :: n, nrhs, lda, ldb
  real(c_double), intent(inout) :: a(lda, n), b(ldb, nrhs)
  integer(c_int64_t), intent(out) :: info
end subroutine