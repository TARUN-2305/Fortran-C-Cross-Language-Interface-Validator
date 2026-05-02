! interface.f90
subroutine memset_f(ptr, val, count) bind(c, name="memset_f")
  use iso_c_binding
  implicit none
  type(c_ptr),    intent(in), value :: ptr
  integer(c_int), intent(in), value :: val
  integer(c_int), intent(in), value :: count   ! WRONG: should be c_size_t
end subroutine