! interface.f90
subroutine dgemm_core(transa, transb, m, n, k, alpha, a, lda, &
                       b, ldb, beta, c, ldc)
  implicit none
  character, intent(in)          :: transa, transb
  integer,   intent(in)          :: m, n, k, lda, ldb, ldc
  double precision, intent(in)   :: alpha, beta
  double precision, intent(in)   :: a(lda, *), b(ldb, *)
  double precision, intent(inout):: c(ldc, *)
end subroutine