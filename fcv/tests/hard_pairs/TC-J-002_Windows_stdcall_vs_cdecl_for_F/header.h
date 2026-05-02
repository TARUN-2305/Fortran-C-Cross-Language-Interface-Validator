/* header.h  — Win32 */
void compute(double *x, int n);   /* defaults to __cdecl */
/* Fortran DLL may use __stdcall. ESP corrupt after call. */