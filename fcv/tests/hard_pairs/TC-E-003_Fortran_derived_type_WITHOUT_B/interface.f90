! interface.f90
type :: mesh_config      ! NO BIND(C)!
  integer :: nx, ny, nz
  real(8) :: dx, dy, dz
  logical :: periodic
end type

subroutine init_mesh(cfg) bind(c, name="init_mesh")
  use iso_c_binding
  implicit none
  type(mesh_config), intent(in) :: cfg   ! WRONG: non-interoperable type
end subroutine