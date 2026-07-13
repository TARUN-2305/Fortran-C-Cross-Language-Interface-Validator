subroutine track_particle(name, num_steps, mass)
    character(len=*), intent(in) :: name
    integer, intent(in) :: num_steps
    double precision, intent(in) :: mass
    print *, "Tracking particle: ", name
    print *, "Steps: ", num_steps, " Mass: ", mass
end subroutine track_particle
