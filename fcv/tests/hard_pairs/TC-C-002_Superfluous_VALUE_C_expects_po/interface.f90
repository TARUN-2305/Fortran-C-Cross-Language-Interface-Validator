! interface.f90
subroutine update_counter(count) bind(c, name="update_counter")
  use iso_c_binding
  implicit none
  integer(c_int), intent(inout), value :: count   ! VALUE: gets a copy
end subroutine