subroutine track_particle(name, num_steps, mass) bind(C, name="track_particle")
    use iso_c_binding
    character(kind=c_char), dimension(*), intent(in) :: name
    integer(c_int), value, intent(in) :: num_steps
    real(c_double), value, intent(in) :: mass
end subroutine track_particle
