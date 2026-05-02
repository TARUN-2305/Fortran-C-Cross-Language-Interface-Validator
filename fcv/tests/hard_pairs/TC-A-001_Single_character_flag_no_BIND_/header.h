/* header.h */
void dgemm_core_(char *transa, char *transb,
                 int *m, int *n, int *k,
                 double *alpha, double *a, int *lda,
                 double *b, int *ldb,
                 double *beta, double *c, int *ldc);