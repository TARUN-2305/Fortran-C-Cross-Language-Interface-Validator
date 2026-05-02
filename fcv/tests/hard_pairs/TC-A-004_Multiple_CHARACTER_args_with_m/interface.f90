! interface.f90
subroutine ilaenv_wrap(ispec, name, opts, n1, n2, n3, n4)
  implicit none
  integer,          intent(in) :: ispec, n1, n2, n3, n4
  character(len=*), intent(in) :: name   ! len hidden arg #1
  character(len=*), intent(in) :: opts   ! len hidden arg #2
end subroutine