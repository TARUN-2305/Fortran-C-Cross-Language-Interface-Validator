! interface.f90
function complex_add(a, b) result(c) bind(c, name="complex_add")
  use iso_c_binding
  implicit none
  complex(c_float_complex), intent(in), value :: a, b
  complex(c_float_complex) :: c
  c = a + b
end function