! interface.f90
function get_label(code) result(lbl)
  implicit none
  integer, intent(in) :: code
  character(len=32)   :: lbl
  ! ... fills lbl based on code
end function