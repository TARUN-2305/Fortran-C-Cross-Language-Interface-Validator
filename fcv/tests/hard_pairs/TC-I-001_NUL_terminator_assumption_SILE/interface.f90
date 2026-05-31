! interface.f90
subroutine get_name(buf, maxlen) bind(c, name="get_name")
  use iso_c_binding
  implicit none
  character(kind=c_char), intent(out) :: buf(maxlen)
  integer(c_int), intent(in), value   :: maxlen
  ! Fills buf with name — no NUL appended!
  buf(1:6) = ['H','e','l','l','o',' ']
end subroutine