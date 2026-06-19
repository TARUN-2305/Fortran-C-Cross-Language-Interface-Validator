/* fem_wrapper.h — Fixed C Header */
#ifndef FEM_WRAPPER_H
#define FEM_WRAPPER_H

/* Fully interoperable with Fortran BIND(C) version */
/* Standard C-types: char pointer, 4-byte int, and 8-byte double */
void compute_displacement(const char *material, int nx, 
                          double load, double *result);

#endif /* FEM_WRAPPER_H */
