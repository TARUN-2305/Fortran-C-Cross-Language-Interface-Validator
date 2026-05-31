! interface.f90
subroutine set_flag(flag) bind(c, name="set_flag")
  use iso_c_binding
  implicit none
  logical, intent(out) :: flag   ! default LOGICAL: not c_bool!
end subroutine