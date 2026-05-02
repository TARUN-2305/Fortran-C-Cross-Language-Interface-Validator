/* header.h */
#ifndef LAPACK_ILP64
typedef int lapack_int;       /* LP64 build: 4 bytes */
#else
typedef int64_t lapack_int;   /* ILP64 build: 8 bytes */
#endif

void lapack_solve(lapack_int n, lapack_int nrhs,
                  double *a, lapack_int lda,
                  double *b, lapack_int ldb,
                  lapack_int *info);