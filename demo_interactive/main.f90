program main
  use iso_c_binding
  implicit none

  ! Declare the C function signature inside an interface block
  interface
     subroutine c_add(a, b, result) bind(c, name="c_add")
       import :: c_int, c_float, c_double
       integer(c_int)          :: a       ! ← Removed 'value' to trigger mismatch
       real(c_double), value   :: b       ! ← Changed to double (8 bytes) to trigger mismatch
       real(c_float)           :: result  ! passed by reference
     end subroutine c_add
  end interface

  integer(c_int) :: x
  real(c_float) :: y
  real(c_float) :: res

  x = 10
  y = 3.14159_c_float
  res = 0.0_c_float

  print *, "[Fortran] Initializing inputs: x =", x, ", y =", y
  print *, "[Fortran] Invoking C function 'c_add' via BIND(C)..."
  
  call c_add(x, y, res)

  print *, "[Fortran] Returned from C function. Output result =", res
end program main
