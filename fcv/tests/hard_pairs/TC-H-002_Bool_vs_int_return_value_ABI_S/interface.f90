! interface.f90
logical(c_bool) function is_valid(x) bind(c, name="is_valid")
  use iso_c_binding
  implicit none
  real(c_double), intent(in), value :: x
  is_valid = (x > 0.0_c_double)
end function