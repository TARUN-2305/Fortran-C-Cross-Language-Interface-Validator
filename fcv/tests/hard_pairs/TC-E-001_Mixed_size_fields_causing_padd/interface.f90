! interface.f90
module grid_types
  use iso_c_binding
  implicit none

  type, bind(c) :: grid_params
    integer(c_signed_char) :: method     ! 1 byte @ offset 0
    ! compiler inserts 7 bytes of padding here!
    real(c_double)         :: tolerance  ! 8 bytes @ offset 8
    integer(c_int)         :: max_iter   ! 4 bytes @ offset 16
    ! compiler inserts 4 bytes of padding here!
    real(c_double)         :: relax      ! 8 bytes @ offset 24
  end type
end module
  interface
    subroutine dummy_proc(x) bind(c)
      import :: grid_params
      type(grid_params), intent(in) :: x
    end subroutine
  end interface
