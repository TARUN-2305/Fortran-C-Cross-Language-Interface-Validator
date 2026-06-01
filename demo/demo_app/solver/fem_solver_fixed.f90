! fem_solver_fixed.f90 — Fixed Fortran solver interface (With BIND(C))
subroutine compute_displacement(material, nx, ny, load, result) bind(c, name="compute_displacement")
  use iso_c_binding
  implicit none
  character(kind=c_char), intent(in)  :: material(*)  ! ← Standard C-string pointer
  integer(c_int), value,  intent(in)  :: nx, ny       ! ← 4-byte standard integers passed by VALUE
  real(c_double), value,  intent(in)  :: load         ! ← 8-byte double passed by VALUE
  real(c_double),         intent(out) :: result       ! ← Returned by reference pointer

  ! Dummy computation: simple fake FEM logic
  if (material(1) == 'S' .or. material(1) == 's') then
     result = load / (210.0 * 1000.0)
  else if (material(1) == 'A' .or. material(1) == 'a') then
     result = load / (70.0 * 1000.0)
  else
     result = load / (100.0 * 1000.0)
  end if
end subroutine compute_displacement
