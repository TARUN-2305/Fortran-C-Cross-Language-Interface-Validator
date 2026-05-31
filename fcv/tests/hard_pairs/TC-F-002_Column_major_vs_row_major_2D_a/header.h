/* header.h */
void mat_scale(double a[][/* n */], int m, int n, double alpha);
/* C sees a[i][j] at i*n+j — the TRANSPOSE of the Fortran layout */