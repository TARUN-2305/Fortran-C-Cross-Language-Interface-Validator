! interface.f90
subroutine store_handler(handler) bind(c, name="store_handler")
  use iso_c_binding
  implicit none
  type(c_ptr), value :: handler   ! WRONG: should be c_funptr
end subroutine