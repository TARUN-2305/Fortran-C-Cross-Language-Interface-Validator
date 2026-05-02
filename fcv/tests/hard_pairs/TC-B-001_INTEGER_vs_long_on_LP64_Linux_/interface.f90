! interface.f90
subroutine sparse_matvec(n, nnz, vals, col_idx, row_ptr, x, y) &
    bind(c, name="sparse_matvec")
  use iso_c_binding
  implicit none
  integer(c_int),    intent(in), value :: n, nnz
  real(c_double),    intent(in)  :: vals(nnz)
  integer(c_int),    intent(in)  :: col_idx(nnz), row_ptr(n+1)
  real(c_double),    intent(in)  :: x(n)
  real(c_double),    intent(out) :: y(n)
end subroutine