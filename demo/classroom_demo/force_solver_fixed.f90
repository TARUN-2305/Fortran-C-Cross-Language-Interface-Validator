subroutine calculate_force(mass, acceleration, force) bind(C, name="calculate_force")
    use iso_c_binding
    real(c_double), value, intent(in) :: mass
    real(c_double), value, intent(in) :: acceleration
    real(c_double), intent(out) :: force

    force = mass * acceleration
end subroutine calculate_force
