! interface.f90
subroutine alloc_buffer(buf, size) bind(c, name="alloc_buffer")
  use iso_c_binding
  implicit none
  type(c_ptr),    intent(out) :: buf    ! Fortran passes *buf (void**)
  integer(c_size_t), intent(in), value :: size
end subroutine