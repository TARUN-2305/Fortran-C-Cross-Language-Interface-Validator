/* fem_wrapper.h — Buggy C Header */
#ifndef FEM_WRAPPER_H
#define FEM_WRAPPER_H

/* Note the trailing underscore due to the lack of Fortran BIND(C) */
/* nx and ny are mismatched long pointers (8 bytes on LP64) vs Fortran 4-byte integer */
void compute_displacement_(char *material, long *nx, long *ny, 
                           double *load, double *result);

#endif /* FEM_WRAPPER_H */
