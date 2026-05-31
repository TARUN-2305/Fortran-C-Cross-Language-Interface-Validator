/* header.h */
void blocked_copy(const double *src, double *dst,
                  int rows, int cols,
                  int dst_ld,    /* was src_ld in Fortran */
                  int src_ld);   /* was dst_ld in Fortran */