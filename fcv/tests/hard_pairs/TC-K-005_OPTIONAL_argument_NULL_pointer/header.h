/* header.h */
void solve_opts(double *a, int n, double *tol, int *max_iter);
/* Internal code: double t = *tol; — CRASH if tol is NULL */