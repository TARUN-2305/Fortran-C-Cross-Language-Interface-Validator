! interface.f90
real function vector_norm(x, n) bind(c, name="vector_norm")
  use iso_c_binding
  implicit none
  integer(c_int), intent(in), value :: n
  real(c_float),  intent(in)        :: x(n)
  vector_norm = 0.0
end function