! fem_solver.f90 — Fixed Fortran Solver Interface (With BIND(C))
subroutine compute_displacement(material, nx, ny, load, result) bind(c, name="compute_displacement")
  use iso_c_binding
  implicit none
  character(kind=c_char), intent(in)  :: material(*)  ! ← Interoperable C-string pointer (no hidden strlen)
  integer(c_int), value,  intent(in)  :: nx, ny       ! ← Interoperable 4-byte integers passed by VALUE
  real(c_double), value,  intent(in)  :: load         ! ← Interoperable 8-byte double passed by VALUE
  real(c_double),         intent(out) :: result       ! ← Passed by reference to return computation

  ! Correct calculation
  if (material(1) == 'S' .or. material(1) == 's') then
     result = load / 210.0
  else
     result = load / 70.0
  end if
end subroutine compute_displacement
