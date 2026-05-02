! interface.f90
subroutine file_seek(fd, offset) bind(c, name="file_seek")
  use iso_c_binding
  implicit none
  integer(c_int),  intent(in), value :: fd
  integer(c_long), intent(in), value :: offset   ! 4 bytes Windows, 8 bytes Linux
end subroutine