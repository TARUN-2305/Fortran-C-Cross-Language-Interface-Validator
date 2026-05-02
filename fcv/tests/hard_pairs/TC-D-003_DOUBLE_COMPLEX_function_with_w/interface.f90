! interface.f90 — 32-bit SPARC legacy code
double complex function zdot(n, x, incx, y, incy)
  implicit none
  integer n, incx, incy
  double complex x(*), y(*)
end function