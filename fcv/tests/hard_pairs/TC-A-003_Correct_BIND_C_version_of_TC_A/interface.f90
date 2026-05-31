! interface.f90
subroutine dgemm_wrap(transa, transb, m, n, k, alpha, a, lda, &
                       b, ldb, beta, c, ldc) bind(c, name="dgemm_wrap")
  use iso_c_binding
  implicit none
  character(kind=c_char), intent(in), value :: transa, transb
  integer(c_int),  intent(in), value :: m, n, k, lda, ldb, ldc
  real(c_double),  intent(in), value :: alpha, beta
  real(c_double),  intent(in)  :: a(lda, *)
  real(c_double),  intent(in)  :: b(ldb, *)
  real(c_double),  intent(inout) :: c(ldc, *)
end subroutine