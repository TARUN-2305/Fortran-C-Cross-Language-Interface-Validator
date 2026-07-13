subroutine calculate_force(mass, acceleration, force)
    double precision, intent(in) :: mass
    double precision, intent(in) :: acceleration
    double precision, intent(out) :: force

    force = mass * acceleration
end subroutine calculate_force
