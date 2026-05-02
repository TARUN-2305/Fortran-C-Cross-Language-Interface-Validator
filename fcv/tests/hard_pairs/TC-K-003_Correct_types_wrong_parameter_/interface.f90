! interface.f90
subroutine blocked_copy(src, dst, rows, cols, src_ld, dst_ld) &
    bind(c, name="blocked_copy")
  use iso_c_binding
  implicit none
  real(c_double), intent(in)  :: src(src_ld, cols)
  real(c_double), intent(out) :: dst(dst_ld, cols)
  integer(c_int), intent(in), value :: rows, cols, src_ld, dst_ld
end subroutine