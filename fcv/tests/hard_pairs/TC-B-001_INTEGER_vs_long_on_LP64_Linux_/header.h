/* header.h */
void sparse_matvec(long n, long nnz,
                   const double *vals,
                   const long *col_idx,
                   const long *row_ptr,
                   const double *x, double *y);