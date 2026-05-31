! interface.f90
subroutine set_dims(rows, cols, depth) bind(c, name="set_dims")
  use iso_c_binding
  implicit none
  integer(c_int), intent(in), value :: rows, cols, depth
end subroutine