! interface.f90
module callbacks
  use iso_c_binding
  implicit none

  abstract interface
    real(c_float) function float_cb(x) bind(c)   ! WRONG: float, not double
      import c_float
      real(c_float), value :: x
    end function
  end interface

  subroutine register_integrand(cb) bind(c, name="register_integrand")
    type(c_funptr), value :: cb
  end subroutine
end module