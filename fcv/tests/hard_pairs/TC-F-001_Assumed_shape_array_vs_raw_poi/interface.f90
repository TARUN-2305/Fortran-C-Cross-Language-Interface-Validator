! interface.f90
subroutine normalize(x) bind(c, name="normalize")
  use iso_c_binding
  implicit none
  real(c_double), intent(inout) :: x(:)   ! assumed-shape: passes CFI_cdesc_t*
end subroutine