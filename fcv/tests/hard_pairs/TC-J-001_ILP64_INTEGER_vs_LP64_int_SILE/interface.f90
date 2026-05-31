! interface.f90 — compiled with -fdefault-integer-8
subroutine dgetrf_ilp64(m, n, a, lda, ipiv, info) bind(c, name="dgetrf_ilp64")
  use iso_c_binding
  implicit none
  integer(c_int64_t), intent(in), value  :: m, n, lda   ! 8 bytes each
  real(c_double),     intent(inout)      :: a(lda, n)
  integer(c_int64_t), intent(out)        :: ipiv(min(m,n))
  integer(c_int64_t), intent(out)        :: info
end subroutine