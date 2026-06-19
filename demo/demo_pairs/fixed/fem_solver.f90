! fem_solver.f90 — Fixed Fortran solver interface (With BIND(C))
subroutine compute_displacement(material, nx, ny, load, result) bind(c, name="compute_displacement")
  use iso_c_binding
  implicit none
  character(kind=c_char), intent(in)  :: material(*)  ! ← Standard C-string pointer
  integer(c_int), value,  intent(in)  :: nx, ny       ! ← 4-byte standard integers passed by VALUE
  real(c_double), value,  intent(in)  :: load         ! ← 8-byte double passed by VALUE
  real(c_double),         intent(out) :: result       ! ← Returned by reference pointer

  logical :: is_steel

  is_steel = .true.
  if (material(1) == 'A' .or. material(1) == 'a') then
     is_steel = .false.
  end if

  ! Call the actual 1D Finite Element Method Solver
  call solve_fem(is_steel, int(nx), load, result)
end subroutine compute_displacement


subroutine solve_fem(is_steel, nx, load, result)
  implicit none
  logical, intent(in) :: is_steel
  integer, intent(in) :: nx
  real(8), intent(in) :: load
  real(8), intent(out) :: result

  real(8) :: L, b, h, E, Le, inertia
  real(8), allocatable :: K(:,:), F(:), u(:)
  integer :: n_dof, i, j, k_idx, err
  real(8) :: Ke(4,4), factor
  real(8) :: mult
  integer :: center_node

  ! Beam properties
  L = 5.0d0          ! 5 meters long
  b = 0.1d0          ! 10 cm wide
  h = 0.2d0          ! 20 cm deep
  inertia = (b * h**3) / 12.0d0

  if (is_steel) then
     E = 200.0d9     ! Steel: 200 GPa
  else
     E = 70.0d9      ! Aluminum: 70 GPa
  end if

  ! Degrees of freedom: 2 per node (deflection and slope).
  ! With nx elements, we have nx + 1 nodes.
  n_dof = 2 * (nx + 1)

  allocate(K(n_dof, n_dof), F(n_dof), u(n_dof), stat=err)
  if (err /= 0) then
     result = 0.0d0
     return
  end if

  K = 0.0d0
  F = 0.0d0
  u = 0.0d0

  Le = L / dble(nx)
  factor = (E * inertia) / (Le**3)

  ! Local Element Stiffness Matrix Ke
  Ke(1,1) = 12.0d0 * factor
  Ke(1,2) = 6.0d0 * Le * factor
  Ke(1,3) = -12.0d0 * factor
  Ke(1,4) = 6.0d0 * Le * factor

  Ke(2,1) = 6.0d0 * Le * factor
  Ke(2,2) = 4.0d0 * (Le**2) * factor
  Ke(2,3) = -6.0d0 * Le * factor
  Ke(2,4) = 2.0d0 * (Le**2) * factor

  Ke(3,1) = -12.0d0 * factor
  Ke(3,2) = -6.0d0 * Le * factor
  Ke(3,3) = 12.0d0 * factor
  Ke(3,4) = -6.0d0 * Le * factor

  Ke(4,1) = 6.0d0 * Le * factor
  Ke(4,2) = 2.0d0 * (Le**2) * factor
  Ke(4,3) = -6.0d0 * Le * factor
  Ke(4,4) = 4.0d0 * (Le**2) * factor

  ! Global Assembly
  do i = 1, nx
     do j = 1, 4
        do k_idx = 1, 4
           K(2*i - 2 + j, 2*i - 2 + k_idx) = K(2*i - 2 + j, 2*i - 2 + k_idx) + Ke(j, k_idx)
        end do
     end do
  end do

  ! Apply fixed boundary conditions at left support (node 0, DOFs 1 and 2)
  K(1, :) = 0.0d0
  K(2, :) = 0.0d0
  K(:, 1) = 0.0d0
  K(:, 2) = 0.0d0
  K(1, 1) = 1.0d0
  K(2, 2) = 1.0d0
  F(1) = 0.0d0
  F(2) = 0.0d0

  ! Apply fixed boundary conditions at right support (node nx, DOFs 2*nx + 1 and 2*nx + 2)
  K(2*nx + 1, :) = 0.0d0
  K(2*nx + 2, :) = 0.0d0
  K(:, 2*nx + 1) = 0.0d0
  K(:, 2*nx + 2) = 0.0d0
  K(2*nx + 1, 2*nx + 1) = 1.0d0
  K(2*nx + 2, 2*nx + 2) = 1.0d0
  F(2*nx + 1) = 0.0d0
  F(2*nx + 2) = 0.0d0

  ! Apply load at the center node (node nx/2, displacement DOF is 2*(nx/2) + 1)
  center_node = nx / 2
  F(2*center_node + 1) = load

  ! Gaussian Elimination
  do i = 1, n_dof - 1
     if (abs(K(i,i)) < 1.0d-12) cycle
     do j = i + 1, n_dof
        mult = K(j,i) / K(i,i)
        K(j,i) = 0.0d0
        K(j, i+1:n_dof) = K(j, i+1:n_dof) - mult * K(i, i+1:n_dof)
        F(j) = F(j) - mult * F(i)
     end do
  end do

  ! Back Substitution
  do i = n_dof, 1, -1
     if (abs(K(i,i)) > 1.0d-12) then
        u(i) = F(i) / K(i,i)
        do j = 1, i - 1
           F(j) = F(j) - K(j,i) * u(i)
        end do
     end if
  end do

  ! Tip displacement deflection
  result = u(2*center_node + 1)

  deallocate(K, F, u)
end subroutine solve_fem
