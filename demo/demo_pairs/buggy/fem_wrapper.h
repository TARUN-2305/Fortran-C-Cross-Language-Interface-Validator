/* fem_wrapper.h — Buggy C Header */
#ifndef FEM_WRAPPER_H
#define FEM_WRAPPER_H

/* Uses BIND(C) name matching but contains type & calling convention mismatches: */
/* - nx is passed by VALUE as 8-byte 'long' (Fortran expects 4-byte int by REFERENCE) */
/* - load is passed by VALUE as 8-byte 'double' (Fortran expects double by REFERENCE) */
void compute_displacement(const char *material, long nx, 
                          double load, double *result);

#endif /* FEM_WRAPPER_H */
