! interface.f90
subroutine process_name(name) bind(c, name="process_name")
  use iso_c_binding
  implicit none
  character(kind=c_char, len=32), intent(in) :: name   ! scalar LEN=32
end subroutine