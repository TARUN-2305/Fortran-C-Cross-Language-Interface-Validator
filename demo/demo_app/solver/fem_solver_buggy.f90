! fem_solver_buggy.f90 — Buggy legacy Fortran interface (No BIND(C))
subroutine compute_displacement(material, nx, ny, load, result)
  implicit none
  character(len=*), intent(in)  :: material  ! ← Injects hidden strlen arg
  integer,          intent(in)  :: nx, ny    ! ← 4-byte standard integers
  real(8),          intent(in)  :: load
  real(8),          intent(out) :: result

  ! Dummy computation: simple fake FEM logic
  if (material == "Steel") then
     result = load / (210.0 * 0.001)
  else if (material == "Aluminum") then
     result = load / (70.0 * 0.001)
  else
     result = load / (100.0 * 0.001)
  end if
end subroutine compute_displacement
