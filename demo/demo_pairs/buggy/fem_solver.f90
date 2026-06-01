! fem_solver.f90 — Buggy Fortran Solver Interface (No BIND(C))
subroutine compute_displacement(material, nx, ny, load, result)
  implicit none
  character(len=*), intent(in)  :: material  ! ← Injects hidden strlen arg at position 6 (legacy ABI)
  integer,          intent(in)  :: nx, ny    ! ← 4-byte standard integers
  real(8),          intent(in)  :: load
  real(8),          intent(out) :: result

  ! Dummy computation to simulate load analysis
  if (material == "Steel") then
     result = load / 210.0
  else
     result = load / 70.0
  end if
end subroutine compute_displacement
