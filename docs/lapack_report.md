# LAPACK Validation Report (Actual Run)

## Executive Summary
Running the `fcvalidator` against the official `Reference-LAPACK` repository `LAPACKE/include/lapacke.h` vs `SRC/`.

## Case 1: Paired Example (dgetrf)
A successful validation of a complex paired routine:

**Fortran Interface:**
```fortran
subroutine dgetrf(m, n, a, lda, ipiv, info) bind(c, name="LAPACKE_dgetrf")
  use iso_c_binding
  integer(c_int), value :: m, n, lda
  real(c_double) :: a(lda, *)
  integer(c_int) :: ipiv(*)
  integer(c_int) :: info
end subroutine
```

**C Header:**
```c
void LAPACKE_dgetrf(int m, int n, double* a, int lda, int* ipiv, int* info);
```

**Validator Output:**
```
OK  [LAPACKE_dgetrf]: Explicit-shape Fortran array a(lda,n) with raw
    pointer 'double*' in C. Memory layout identical (column-major, flat
    storage). lda convention correctly handles leading dimension.
```

## Raw Output Log
                          Interface Validation Report                          
+-----------------------------------------------------------------------------+
| Severity | Procedure           | Category            | Message              |
|----------+---------------------+---------------------+----------------------|
| WARNING  | lapack_make_comple… | Unmatched procedure | C function           |
|          |                     |                     | 'lapack_make_comple… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | lapack_make_comple… | Unmatched procedure | C function           |
|          |                     |                     | 'lapack_make_comple… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sbdsdc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sbdsdc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dbdsdc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dbdsdc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sbdsqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sbdsqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dbdsqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dbdsqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cbdsqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cbdsqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zbdsqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zbdsqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sbdsvdx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sbdsvdx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dbdsvdx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dbdsvdx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sdisna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sdisna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ddisna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ddisna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgbbrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbbrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgbbrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbbrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgbbrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbbrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgbbrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbbrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgbequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgbequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgbequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgbequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgbequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgbrfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbrfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbrfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbrfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbrfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbrfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbrfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbrfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgbsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgbsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgbsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgbsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgbsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgbsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgbsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgbsvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbsvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbsvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbsvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbsvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbsvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbsvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbsvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbtrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbtrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgbtrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbtrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgbtrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbtrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgbtrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbtrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgebak      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgebak' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgebak      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgebak' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgebak      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgebak' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgebak      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgebak' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgebal      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgebal' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgebal      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgebal' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgebal      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgebal' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgebal      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgebal' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgebrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgebrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgebrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgebrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgebrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgebrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgebrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgebrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgecon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgecon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgecon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgecon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgecon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgecon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgecon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgecon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgees       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgees' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgees       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgees' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgees       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgees' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgees       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgees' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeesx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeesx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeesx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeesx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeesx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeesx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeesx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeesx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgehrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgehrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgehrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgehrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgehrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgehrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgehrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgehrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgejsv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgejsv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgejsv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgejsv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgejsv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgejsv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgejsv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgejsv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgelq2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelq2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgelq2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelq2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgelq2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelq2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgelq2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelq2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgelqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgelqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgelqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgelqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgels       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgels' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgels       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgels' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgels       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgels' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgels       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgels' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgelsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgelsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgelsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgelsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgelss      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelss' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgelss      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelss' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgelss      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelss' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgelss      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelss' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgelsy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelsy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgelsy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelsy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgelsy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelsy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgelsy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelsy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeqlf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqlf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeqlf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqlf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeqlf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqlf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeqlf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqlf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeqp3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqp3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeqp3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqp3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeqp3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqp3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeqp3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqp3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeqpf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqpf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeqpf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqpf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeqpf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqpf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeqpf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqpf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeqr2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqr2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeqr2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqr2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeqr2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqr2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeqr2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqr2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeqrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeqrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeqrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeqrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeqrfp     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrfp'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqrfp     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrfp'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqrfp     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrfp'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqrfp     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrfp'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgerfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgerfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgerfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgerfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgerfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgerfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgerfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgerfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgerfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgerfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgerfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgerfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgerfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgerfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgerfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgerfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgerqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgerqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgerqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgerqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgerqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgerqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgerqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgerqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgesdd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesdd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgesdd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesdd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgesdd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesdd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgesdd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesdd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgesv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgesv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgesv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgesv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsgesv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsgesv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zcgesv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zcgesv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgesvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgesvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgesvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgesvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgesvdx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvdx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvdx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvdx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvdx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvdx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvdx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvdx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesvdq     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvdq'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvdq     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvdq'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvdq     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvdq'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvdq     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvdq'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesvj      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvj' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgesvj      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvj' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgesvj      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvj' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgesvj      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvj' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgesvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgesvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgesvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgesvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgesvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetf2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetf2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgetf2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetf2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgetf2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetf2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgetf2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetf2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgetrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgetrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgetrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgetrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgetrf2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetrf2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetrf2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetrf2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetrf2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetrf2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetrf2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetrf2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgetri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgetri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgetri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgetrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgetrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgetrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgetrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggbak      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggbak' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggbak      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggbak' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggbak      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggbak' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggbak      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggbak' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggbal      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggbal' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggbal      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggbal' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggbal      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggbal' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggbal      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggbal' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgges       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgges' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgges       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgges' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgges       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgges' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgges       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgges' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgges3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgges3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgges3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgges3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgges3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgges3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgges3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgges3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggesx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggesx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggesx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggesx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggesx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggesx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggesx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggesx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggev3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggev3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggev3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggev3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggev3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggev3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggev3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggev3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggglm      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggglm' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggglm      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggglm' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggglm      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggglm' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggglm      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggglm' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgghrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgghrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgghrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgghrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgghrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgghrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgghrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgghrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgghd3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgghd3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgghd3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgghd3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgghd3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgghd3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgghd3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgghd3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgglse      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgglse' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgglse      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgglse' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgglse      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgglse' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgglse      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgglse' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggqrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggqrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggqrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggqrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggqrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggqrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggqrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggqrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggrqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggrqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggrqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggrqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggrqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggrqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggrqf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggrqf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggsvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggsvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggsvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggsvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggsvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggsvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggsvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggsvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggsvd3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggsvd3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggsvd3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggsvd3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggsvd3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggsvd3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggsvd3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggsvd3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggsvp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggsvp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dggsvp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggsvp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cggsvp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggsvp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zggsvp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggsvp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sggsvp3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggsvp3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggsvp3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggsvp3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggsvp3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggsvp3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggsvp3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggsvp3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgtcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgtcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgtcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgtcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgtcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgtcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgtcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgtcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgtrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgtrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgtrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgtrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgtrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgtrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgtrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgtrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgtsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgtsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgtsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgtsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgtsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgtsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgtsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgtsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgtsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgtsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgtsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgtsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgtsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgtsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgtsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgtsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgttrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgttrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgttrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgttrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgttrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgttrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgttrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgttrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgttrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgttrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgttrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgttrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgttrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgttrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgttrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgttrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chbev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhbev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chbevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhbevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chbevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhbevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chbgst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbgst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhbgst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbgst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chbgv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbgv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhbgv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbgv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chbgvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbgvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhbgvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbgvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chbgvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbgvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhbgvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbgvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chbtrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbtrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhbtrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbtrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_checon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_checon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhecon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhecon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cheequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zheev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cheevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zheevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cheevr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zheevr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cheevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zheevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chegst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhegst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chegv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhegv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chegvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhegvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chegvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhegvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cherfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cherfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zherfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zherfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cherfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cherfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zherfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zherfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhesv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chesvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhesvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chesvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhetrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chetrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhetrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chetri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhetri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chetrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhetrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chfrk       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chfrk' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhfrk       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhfrk' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_shgeqz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_shgeqz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dhgeqz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dhgeqz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chgeqz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chgeqz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhgeqz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhgeqz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpgst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpgst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpgst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpgst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpgv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpgv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpgv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpgv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpgvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpgvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpgvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpgvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpgvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpgvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpgvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpgvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chpsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhpsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chptrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chptrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhptrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhptrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_shsein      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_shsein' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dhsein      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dhsein' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chsein      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chsein' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhsein      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhsein' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_shseqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_shseqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dhseqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dhseqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_chseqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chseqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zhseqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhseqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clacgv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacgv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlacgv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacgv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slacn2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slacn2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlacn2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlacn2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clacn2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacn2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlacn2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacn2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slacpy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slacpy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlacpy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlacpy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clacpy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacpy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlacpy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacpy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clacp2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacp2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlacp2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacp2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlag2c      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlag2c' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slag2d      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slag2d' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlag2s      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlag2s' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clag2z      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clag2z' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slagge      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slagge' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlagge      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlagge' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clagge      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clagge' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlagge      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlagge' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slamch      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slamch' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlamch      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlamch' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slangb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slangb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlangb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlangb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clangb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clangb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlangb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlangb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slange      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slange' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlange      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlange' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clange      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clange' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlange      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlange' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clanhe      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clanhe' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlanhe      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlanhe' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clacrm      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacrm' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlacrm      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacrm' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clarcm      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarcm' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlarcm      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarcm' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slansy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slansy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlansy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlansy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clansy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clansy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlansy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlansy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slantr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slantr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlantr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlantr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clantr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clantr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlantr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlantr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slarfb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarfb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlarfb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarfb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clarfb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarfb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlarfb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarfb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slarfg      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarfg' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlarfg      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarfg' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clarfg      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarfg' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlarfg      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarfg' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slarft      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarft' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlarft      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarft' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clarft      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarft' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlarft      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarft' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slarfx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarfx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlarfx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarfx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clarfx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarfx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlarfx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarfx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slarnv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarnv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlarnv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarnv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clarnv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarnv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlarnv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarnv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slascl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slascl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlascl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlascl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clascl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clascl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlascl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlascl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slaset      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slaset' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlaset      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlaset' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_claset      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_claset' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlaset      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlaset' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slasrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slasrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlasrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlasrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slassq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slassq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlassq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlassq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_classq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_classq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlassq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlassq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slaswp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slaswp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlaswp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlaswp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_claswp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_claswp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlaswp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlaswp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slatms      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slatms' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlatms      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlatms' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clatms      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clatms' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlatms      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlatms' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slauum      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slauum' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlauum      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlauum' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clauum      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clauum' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlauum      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlauum' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sopgtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sopgtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dopgtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dopgtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sopmtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sopmtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dopmtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dopmtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorgbr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgbr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorgbr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgbr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorghr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorghr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorghr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorghr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorglq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorglq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorglq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorglq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorgql      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgql' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorgql      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgql' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorgqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorgqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorgrq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgrq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorgrq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgrq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorgtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorgtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorgtsqr_r… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgtsqr_r… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorgtsqr_r… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgtsqr_r… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormbr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormbr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dormbr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormbr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sormhr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormhr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dormhr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormhr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sormlq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormlq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dormlq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormlq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sormql      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormql' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dormql      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormql' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sormqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dormqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sormrq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormrq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dormrq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormrq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sormrz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormrz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dormrz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormrz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sormtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dormtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spbequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpbequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpbequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpbequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spbstf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbstf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpbstf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbstf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpbstf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbstf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpbstf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbstf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spbsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpbsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpbsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpbsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spbsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpbsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpbsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpbsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spbtrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbtrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpbtrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbtrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpbtrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbtrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpbtrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbtrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spftrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spftrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpftrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpftrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpftrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpftrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpftrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpftrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spftri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spftri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpftri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpftri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpftri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpftri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpftri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpftri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spftrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spftrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpftrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpftrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpftrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpftrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpftrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpftrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spocon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spocon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpocon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpocon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpocon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpocon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpocon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpocon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spoequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spoequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpoequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpoequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpoequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpoequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpoequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpoequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spoequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spoequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpoequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpoequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpoequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpoequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpoequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpoequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sporfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sporfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dporfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dporfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cporfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cporfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zporfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zporfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sporfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sporfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dporfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dporfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cporfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cporfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zporfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zporfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sposv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sposv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dposv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dposv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cposv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cposv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zposv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zposv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsposv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsposv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zcposv      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zcposv' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sposvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sposvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dposvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dposvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cposvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cposvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zposvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zposvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sposvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sposvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dposvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dposvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cposvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cposvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zposvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zposvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spotrf2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spotrf2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpotrf2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpotrf2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpotrf2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpotrf2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpotrf2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpotrf2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spotrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spotrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpotrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpotrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpotrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpotrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpotrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpotrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spotri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spotri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpotri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpotri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpotri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpotri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpotri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpotri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spotrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spotrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpotrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpotrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpotrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpotrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpotrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpotrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sppcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sppcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dppcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dppcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cppcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cppcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zppcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zppcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sppequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sppequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dppequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dppequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cppequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cppequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zppequ      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zppequ' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sppsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sppsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dppsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dppsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cppsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cppsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zppsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zppsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sppsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sppsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dppsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dppsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cppsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cppsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zppsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zppsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spstrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spstrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpstrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpstrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpstrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpstrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpstrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpstrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sptcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sptcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dptcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dptcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cptcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cptcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zptcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zptcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spteqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spteqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpteqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpteqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpteqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpteqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpteqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpteqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sptrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sptrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dptrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dptrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cptrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cptrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zptrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zptrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sptsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sptsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dptsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dptsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cptsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cptsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zptsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zptsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sptsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sptsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dptsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dptsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cptsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cptsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zptsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zptsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spttrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spttrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpttrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpttrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpttrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpttrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpttrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpttrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_spttrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spttrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dpttrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpttrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cpttrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpttrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zpttrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpttrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_crot        | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_crot' has   |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zrot        | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zrot' has   |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssbev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsbev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssbevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsbevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssbevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsbevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssbgst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbgst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsbgst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbgst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssbgv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbgv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsbgv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbgv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssbgvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbgvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsbgvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbgvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssbgvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbgvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsbgvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbgvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssbtrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbtrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsbtrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbtrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssfrk       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssfrk' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsfrk       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsfrk' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cspcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cspcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zspcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zspcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspgst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspgst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspgst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspgst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspgv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspgv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspgv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspgv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspgvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspgvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspgvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspgvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspgvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspgvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspgvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspgvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cspsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cspsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zspsv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zspsv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sspsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dspsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cspsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cspsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zspsvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zspsvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssptrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssptrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsptrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsptrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsptrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsptrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstebz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstebz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstebz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstebz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstedc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstedc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstedc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstedc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cstedc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cstedc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zstedc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zstedc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstegr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstegr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstegr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstegr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cstegr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cstegr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zstegr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zstegr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstein      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstein' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstein      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstein' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cstein      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cstein' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zstein      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zstein' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstemr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstemr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstemr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstemr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cstemr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cstemr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zstemr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zstemr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssteqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssteqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsteqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsteqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csteqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csteqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsteqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsteqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssterf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssterf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsterf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsterf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstevr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstevr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstevr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstevr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sstevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dstevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssycon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssycon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsycon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsycon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csycon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csycon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsycon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsycon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssyequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyequb     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyequb'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsyev       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyev' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssyevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsyevd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssyevr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsyevr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssyevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsyevx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssygst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsygst      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygst' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssygv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsygv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssygvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsygvd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygvd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssygvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsygvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssyrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsyrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csyrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsyrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssyrfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyrfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyrfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyrfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyrfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyrfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyrfsx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyrfsx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsysv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csysv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsysv       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssysvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsysvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csysvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsysvx      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysvx' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssysvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysvxx     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysvxx'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsytrd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssytrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsytrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csytrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsytrf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssytri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsytri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csytri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsytri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssytrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dsytrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_csytrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsytrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztbcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztbcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztbrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztbrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztbtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztbtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stfsm       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stfsm' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtfsm       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtfsm' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctfsm       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctfsm' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztfsm       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztfsm' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stftri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stftri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtftri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtftri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctftri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctftri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztftri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztftri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stfttp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stfttp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtfttp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtfttp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctfttp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctfttp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztfttp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztfttp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stfttr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stfttr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtfttr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtfttr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctfttr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctfttr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztfttr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztfttr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stgevc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgevc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtgevc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgevc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctgevc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgevc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztgevc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgevc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stgexc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgexc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtgexc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgexc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctgexc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgexc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztgexc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgexc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stgsen      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgsen' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtgsen      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgsen' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctgsen      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgsen' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztgsen      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgsen' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stgsja      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgsja' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtgsja      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgsja' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctgsja      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgsja' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztgsja      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgsja' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stgsna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgsna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtgsna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgsna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctgsna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgsna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztgsna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgsna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stgsyl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgsyl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtgsyl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgsyl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctgsyl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgsyl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztgsyl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgsyl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stpcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtpcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctpcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztpcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztprfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztprfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztptri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztptri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztptrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztptrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stpttf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpttf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtpttf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpttf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctpttf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpttf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztpttf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpttf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stpttr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpttr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtpttr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpttr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctpttr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpttr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztpttr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpttr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrcon      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrcon' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strevc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strevc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrevc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrevc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrevc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrevc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrevc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrevc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strexc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strexc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrexc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrexc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrexc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrexc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrexc      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrexc' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrrfs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrrfs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strsen      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strsen' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrsen      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrsen' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrsen      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrsen' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrsen      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrsen' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strsna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strsna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrsna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrsna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrsna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrsna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrsna      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrsna' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strsyl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strsyl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrsyl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrsyl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrsyl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrsyl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrsyl      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrsyl' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strsyl3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strsyl3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrsyl3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrsyl3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrsyl3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrsyl3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strtri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strtri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrtri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrtri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrtri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrtri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrtri      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrtri' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrtrs      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrtrs' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strttf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strttf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrttf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrttf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrttf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrttf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrttf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrttf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_strttp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strttp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtrttp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrttp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctrttp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrttp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztrttp      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrttp' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stzrzf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stzrzf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtzrzf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtzrzf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctzrzf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctzrzf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztzrzf      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztzrzf' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cungbr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungbr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zungbr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungbr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunghr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunghr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunghr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunghr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunglq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunglq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunglq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunglq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cungql      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungql' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zungql      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungql' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cungqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zungqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cungrq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungrq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zungrq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungrq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cungtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zungtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cungtsqr_r… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungtsqr_r… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zungtsqr_r… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungtsqr_r… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmbr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmbr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunmbr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmbr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunmhr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmhr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunmhr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmhr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunmlq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmlq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunmlq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmlq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunmql      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmql' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunmql      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmql' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunmqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunmqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunmrq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmrq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunmrq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmrq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunmrz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmrz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunmrz      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmrz' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunmtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunmtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cupgtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cupgtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zupgtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zupgtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cupmtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cupmtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zupmtr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zupmtr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sbdsdc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sbdsdc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dbdsdc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dbdsdc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sbdsvdx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sbdsvdx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dbdsvdx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dbdsvdx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sbdsqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sbdsqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dbdsqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dbdsqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cbdsqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cbdsqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zbdsqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zbdsqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sdisna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sdisna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ddisna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ddisna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbbrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbbrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbbrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbbrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbbrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbbrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbbrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbbrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbrfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbrfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbrfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbrfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbrfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbrfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbrfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbrfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbsvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbsvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbsvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbsvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbsvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbsvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbsvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbsvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbtrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbtrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbtrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbtrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbtrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbtrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbtrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbtrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgebak_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgebak_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgebak_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgebak_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgebak_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgebak_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgebak_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgebak_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgebal_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgebal_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgebal_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgebal_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgebal_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgebal_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgebal_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgebal_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgebrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgebrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgebrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgebrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgebrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgebrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgebrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgebrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgecon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgecon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgecon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgecon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgecon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgecon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgecon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgecon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgees_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgees_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgees_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgees_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgees_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgees_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgees_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgees_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeesx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeesx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeesx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeesx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeesx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeesx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeesx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeesx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgehrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgehrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgehrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgehrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgehrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgehrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgehrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgehrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgejsv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgejsv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgejsv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgejsv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgejsv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgejsv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgejsv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgejsv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgelq2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelq2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgelq2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelq2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgelq2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelq2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgelq2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelq2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgelqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgelqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgelqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgelqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgels_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgels_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgels_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgels_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgels_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgels_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgels_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgels_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgelsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgelsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgelsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgelsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgelss_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelss_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgelss_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelss_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgelss_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelss_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgelss_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelss_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgelsy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelsy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgelsy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelsy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgelsy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelsy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgelsy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelsy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqlf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqlf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqlf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqlf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqlf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqlf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqlf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqlf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqp3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqp3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqp3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqp3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqp3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqp3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqp3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqp3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqpf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqpf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqpf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqpf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqpf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqpf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqpf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqpf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqr2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqr2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqr2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqr2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqr2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqr2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqr2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqr2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqrfp_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrfp_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqrfp_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrfp_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqrfp_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrfp_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqrfp_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrfp_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgerfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgerfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgerfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgerfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgerfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgerfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgerfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgerfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgerfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgerfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgerfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgerfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgerfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgerfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgerfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgerfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgerqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgerqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgerqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgerqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgerqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgerqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgerqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgerqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesdd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesdd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesdd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesdd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesdd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesdd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesdd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesdd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgedmd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgedmd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgedmd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgedmd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgedmd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgedmd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgedmd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgedmd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgedmdq_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgedmdq_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgedmdq_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgedmdq_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgedmdq_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgedmdq_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgedmdq_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgedmdq_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsgesv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsgesv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zcgesv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zcgesv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesvdx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvdx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvdx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvdx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvdx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvdx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvdx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvdx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesvdq_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvdq_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvdq_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvdq_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvdq_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvdq_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvdq_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvdq_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesvj_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvj_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvj_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvj_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvj_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvj_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvj_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvj_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgesvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgesvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgesvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgesvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgesvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgesvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgesvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgesvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetf2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetf2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetf2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetf2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetf2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetf2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetf2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetf2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetrf2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetrf2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetrf2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetrf2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetrf2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetrf2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetrf2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetrf2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggbak_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggbak_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggbak_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggbak_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggbak_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggbak_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggbak_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggbak_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggbal_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggbal_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggbal_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggbal_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggbal_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggbal_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggbal_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggbal_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgges_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgges_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgges_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgges_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgges_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgges_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgges_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgges_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgges3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgges3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgges3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgges3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgges3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgges3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgges3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgges3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggesx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggesx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggesx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggesx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggesx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggesx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggesx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggesx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggev3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggev3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggev3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggev3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggev3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggev3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggev3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggev3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggglm_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggglm_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggglm_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggglm_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggglm_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggglm_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggglm_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggglm_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgghrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgghrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgghrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgghrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgghrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgghrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgghrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgghrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgghd3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgghd3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgghd3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgghd3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgghd3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgghd3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgghd3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgghd3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgglse_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgglse_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgglse_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgglse_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgglse_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgglse_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgglse_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgglse_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggqrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggqrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggqrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggqrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggqrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggqrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggqrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggqrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggrqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggrqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggrqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggrqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggrqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggrqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggrqf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggrqf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggsvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggsvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggsvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggsvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggsvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggsvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggsvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggsvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggsvd3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggsvd3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggsvd3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggsvd3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggsvd3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggsvd3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggsvd3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggsvd3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggsvp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggsvp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggsvp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggsvp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggsvp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggsvp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggsvp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggsvp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sggsvp3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sggsvp3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dggsvp3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dggsvp3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cggsvp3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cggsvp3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zggsvp3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zggsvp3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgtcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgtcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgtcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgtcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgtcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgtcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgtcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgtcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgtrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgtrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgtrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgtrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgtrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgtrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgtrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgtrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgtsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgtsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgtsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgtsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgtsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgtsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgtsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgtsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgtsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgtsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgtsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgtsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgtsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgtsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgtsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgtsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgttrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgttrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgttrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgttrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgttrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgttrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgttrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgttrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgttrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgttrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgttrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgttrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgttrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgttrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgttrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgttrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbgst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbgst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbgst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbgst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbgv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbgv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbgv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbgv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbgvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbgvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbgvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbgvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbgvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbgvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbgvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbgvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbtrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbtrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbtrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbtrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_checon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_checon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhecon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhecon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chegst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhegst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chegv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhegv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chegvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhegvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chegvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhegvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cherfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cherfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zherfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zherfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cherfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cherfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zherfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zherfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chfrk_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chfrk_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhfrk_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhfrk_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_shgeqz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_shgeqz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dhgeqz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dhgeqz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chgeqz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chgeqz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhgeqz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhgeqz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpgst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpgst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpgst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpgst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpgv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpgv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpgv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpgv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpgvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpgvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpgvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpgvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpgvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpgvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpgvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpgvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chpsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chpsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhpsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhpsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chptrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chptrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhptrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhptrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_shsein_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_shsein_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dhsein_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dhsein_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chsein_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chsein_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhsein_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhsein_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_shseqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_shseqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dhseqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dhseqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chseqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chseqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhseqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhseqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clacgv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacgv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlacgv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacgv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slacn2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slacn2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlacn2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlacn2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clacn2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacn2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlacn2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacn2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slacpy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slacpy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlacpy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlacpy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clacpy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacpy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlacpy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacpy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clacp2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacp2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlacp2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacp2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlag2c_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlag2c_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slag2d_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slag2d_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlag2s_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlag2s_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clag2z_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clag2z_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slagge_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slagge_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlagge_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlagge_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clagge_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clagge_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlagge_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlagge_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_claghe_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_claghe_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlaghe_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlaghe_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slagsy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slagsy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlagsy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlagsy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clagsy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clagsy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlagsy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlagsy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slapmr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slapmr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlapmr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlapmr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clapmr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clapmr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlapmr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlapmr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slapmt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slapmt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlapmt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlapmt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clapmt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clapmt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlapmt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlapmt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slartgp_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slartgp_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlartgp_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlartgp_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slartgs_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slartgs_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlartgs_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlartgs_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slapy2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slapy2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlapy2_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlapy2_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slapy3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slapy3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlapy3_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlapy3_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slamch_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slamch_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlamch_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlamch_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slangb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slangb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlangb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlangb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clangb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clangb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlangb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlangb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slange_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slange_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlange_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlange_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clange_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clange_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlange_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlange_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clanhe_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clanhe_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlanhe_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlanhe_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clacrm_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clacrm_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlacrm_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlacrm_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clarcm_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarcm_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlarcm_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarcm_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slansy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slansy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlansy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlansy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clansy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clansy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlansy_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlansy_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slantr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slantr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlantr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlantr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clantr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clantr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlantr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlantr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slarfb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarfb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlarfb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarfb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clarfb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarfb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlarfb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarfb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slarfg_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarfg_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlarfg_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarfg_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clarfg_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarfg_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlarfg_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarfg_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slarft_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarft_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlarft_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarft_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clarft_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarft_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlarft_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarft_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slarfx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarfx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlarfx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarfx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clarfx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarfx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlarfx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarfx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slarnv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slarnv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlarnv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlarnv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clarnv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clarnv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlarnv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlarnv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slascl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slascl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlascl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlascl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clascl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clascl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlascl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlascl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slaset_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slaset_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlaset_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlaset_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_claset_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_claset_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlaset_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlaset_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slasrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slasrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlasrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlasrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slassq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slassq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlassq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlassq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_classq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_classq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlassq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlassq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slaswp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slaswp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlaswp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlaswp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_claswp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_claswp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlaswp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlaswp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slatms_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slatms_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlatms_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlatms_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clatms_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clatms_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlatms_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlatms_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slauum_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slauum_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlauum_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlauum_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_clauum_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clauum_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zlauum_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlauum_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sopgtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sopgtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dopgtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dopgtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sopmtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sopmtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dopmtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dopmtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorgbr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgbr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorgbr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgbr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorghr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorghr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorghr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorghr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorglq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorglq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorglq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorglq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorgql_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgql_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorgql_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgql_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorgqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorgqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorgrq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgrq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorgrq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgrq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorgtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorgtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorgtsqr_r… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorgtsqr_r… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorgtsqr_r… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorgtsqr_r… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormbr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormbr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dormbr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormbr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormhr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormhr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dormhr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormhr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormlq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormlq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dormlq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormlq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormql_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormql_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dormql_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormql_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dormqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormrq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormrq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dormrq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormrq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormrz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormrz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dormrz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormrz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sormtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sormtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dormtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dormtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spbequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpbequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpbequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpbequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spbstf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbstf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpbstf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbstf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpbstf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbstf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpbstf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbstf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spbsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpbsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpbsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpbsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spbsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpbsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpbsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpbsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spbtrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbtrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpbtrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbtrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpbtrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbtrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpbtrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbtrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spftrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spftrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpftrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpftrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpftrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpftrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpftrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpftrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spftri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spftri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpftri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpftri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpftri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpftri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpftri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpftri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spftrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spftrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpftrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpftrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpftrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpftrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpftrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpftrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spocon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spocon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpocon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpocon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpocon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpocon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpocon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpocon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spoequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spoequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpoequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpoequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpoequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpoequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpoequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpoequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spoequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spoequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpoequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpoequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpoequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpoequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpoequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpoequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sporfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sporfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dporfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dporfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cporfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cporfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zporfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zporfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sporfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sporfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dporfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dporfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cporfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cporfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zporfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zporfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sposv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sposv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dposv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dposv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cposv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cposv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zposv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zposv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsposv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsposv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zcposv_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zcposv_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sposvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sposvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dposvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dposvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cposvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cposvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zposvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zposvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sposvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sposvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dposvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dposvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cposvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cposvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zposvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zposvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spotrf2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spotrf2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpotrf2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpotrf2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpotrf2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpotrf2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpotrf2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpotrf2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spotrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spotrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpotrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpotrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpotrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpotrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpotrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpotrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spotri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spotri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpotri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpotri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpotri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpotri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpotri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpotri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spotrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spotrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpotrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpotrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpotrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpotrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpotrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpotrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sppcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sppcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dppcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dppcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cppcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cppcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zppcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zppcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sppequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sppequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dppequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dppequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cppequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cppequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zppequ_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zppequ_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sppsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sppsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dppsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dppsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cppsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cppsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zppsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zppsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sppsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sppsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dppsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dppsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cppsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cppsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zppsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zppsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spstrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spstrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpstrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpstrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpstrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpstrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpstrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpstrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sptcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sptcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dptcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dptcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cptcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cptcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zptcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zptcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spteqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spteqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpteqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpteqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpteqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpteqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpteqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpteqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sptrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sptrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dptrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dptrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cptrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cptrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zptrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zptrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sptsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sptsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dptsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dptsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cptsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cptsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zptsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zptsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sptsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sptsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dptsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dptsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cptsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cptsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zptsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zptsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spttrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spttrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpttrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpttrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpttrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpttrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpttrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpttrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_spttrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_spttrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dpttrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dpttrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cpttrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cpttrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zpttrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zpttrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_crot_work   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_crot_work'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zrot_work   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zrot_work'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbgst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbgst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbgst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbgst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbgv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbgv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbgv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbgv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbgvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbgvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbgvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbgvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbgvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbgvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbgvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbgvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbtrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbtrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbtrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbtrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssfrk_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssfrk_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsfrk_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsfrk_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cspcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cspcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zspcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zspcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspgst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspgst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspgst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspgst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspgv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspgv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspgv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspgv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspgvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspgvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspgvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspgvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspgvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspgvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspgvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspgvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cspsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cspsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zspsv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zspsv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sspsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sspsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dspsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dspsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cspsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cspsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zspsvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zspsvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssptrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssptrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsptrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsptrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsptrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsptrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstebz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstebz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstebz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstebz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstedc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstedc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstedc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstedc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cstedc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cstedc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zstedc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zstedc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstegr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstegr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstegr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstegr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cstegr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cstegr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zstegr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zstegr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstein_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstein_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstein_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstein_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cstein_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cstein_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zstein_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zstein_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstemr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstemr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstemr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstemr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cstemr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cstemr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zstemr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zstemr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssteqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssteqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsteqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsteqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csteqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csteqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsteqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsteqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssterf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssterf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsterf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsterf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstevr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstevr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstevr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstevr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sstevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sstevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dstevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dstevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssycon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssycon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsycon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsycon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csycon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csycon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsycon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsycon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyequb_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyequb_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyev_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyev_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssygst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsygst_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygst_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssygv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsygv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssygvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsygvd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygvd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssygvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsygvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyrfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyrfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyrfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyrfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyrfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyrfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyrfsx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyrfsx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysvx_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysvx_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysvxx_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysvxx_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztbcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztbcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztbrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztbrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztbtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztbtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stfsm_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stfsm_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtfsm_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtfsm_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctfsm_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctfsm_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztfsm_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztfsm_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stftri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stftri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtftri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtftri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctftri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctftri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztftri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztftri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stfttp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stfttp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtfttp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtfttp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctfttp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctfttp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztfttp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztfttp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stfttr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stfttr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtfttr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtfttr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctfttr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctfttr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztfttr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztfttr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stgevc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgevc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtgevc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgevc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctgevc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgevc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztgevc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgevc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stgexc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgexc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtgexc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgexc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctgexc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgexc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztgexc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgexc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stgsen_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgsen_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtgsen_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgsen_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctgsen_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgsen_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztgsen_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgsen_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stgsja_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgsja_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtgsja_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgsja_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctgsja_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgsja_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztgsja_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgsja_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stgsna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgsna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtgsna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgsna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctgsna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgsna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztgsna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgsna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stgsyl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stgsyl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtgsyl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtgsyl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctgsyl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctgsyl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztgsyl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztgsyl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stpcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtpcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctpcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztpcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztprfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztprfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztptri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztptri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztptrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztptrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stpttf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpttf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtpttf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpttf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctpttf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpttf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztpttf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpttf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stpttr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpttr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtpttr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpttr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctpttr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpttr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztpttr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpttr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrcon_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrcon_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strevc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strevc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrevc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrevc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrevc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrevc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrevc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrevc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strexc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strexc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrexc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrexc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrexc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrexc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrexc_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrexc_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrrfs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrrfs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strsen_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strsen_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrsen_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrsen_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrsen_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrsen_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrsen_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrsen_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strsna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strsna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrsna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrsna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrsna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrsna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrsna_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrsna_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strsyl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strsyl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrsyl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrsyl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrsyl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrsyl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrsyl_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrsyl_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strsyl3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strsyl3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrsyl3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrsyl3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrsyl3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrsyl3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrsyl3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrsyl3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strtri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strtri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrtri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrtri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrtri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrtri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrtri_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrtri_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrtrs_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrtrs_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strttf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strttf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrttf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrttf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrttf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrttf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrttf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrttf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_strttp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_strttp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtrttp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtrttp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctrttp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctrttp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztrttp_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztrttp_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stzrzf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stzrzf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtzrzf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtzrzf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctzrzf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctzrzf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztzrzf_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztzrzf_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cungbr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungbr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zungbr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungbr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunghr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunghr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunghr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunghr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunglq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunglq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunglq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunglq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cungql_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungql_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zungql_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungql_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cungqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zungqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cungrq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungrq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zungrq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungrq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cungtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zungtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cungtsqr_r… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cungtsqr_r… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zungtsqr_r… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zungtsqr_r… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmbr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmbr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunmbr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmbr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmhr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmhr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunmhr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmhr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmlq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmlq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunmlq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmlq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmql_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmql_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunmql_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmql_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunmqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmrq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmrq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunmrq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmrq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmrz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmrz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunmrz_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmrz_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunmtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunmtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunmtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunmtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cupgtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cupgtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zupgtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zupgtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cupmtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cupmtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zupmtr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zupmtr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_claghe      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_claghe' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlaghe      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlaghe' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slagsy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slagsy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlagsy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlagsy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clagsy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clagsy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlagsy      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlagsy' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slapmr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slapmr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlapmr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlapmr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clapmr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clapmr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlapmr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlapmr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slapmt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slapmt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlapmt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlapmt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_clapmt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_clapmt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zlapmt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zlapmt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slapy2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slapy2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlapy2      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlapy2' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slapy3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slapy3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dlapy3      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlapy3' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_slartgp     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slartgp'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlartgp     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlartgp'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_slartgs     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_slartgs'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dlartgs     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dlartgs'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cbbcsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cbbcsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cbbcsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cbbcsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheswapr    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheswapr'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheswapr_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheswapr_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetri2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetri2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetri2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetri2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetri2x    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetri2x'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetri2x_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetri2x_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyconv     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyconv'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyconv_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyconv_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyswapr    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyswapr'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyswapr_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyswapr_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytri2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytri2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytri2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytri2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytri2x    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytri2x'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytri2x_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytri2x_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunbdb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunbdb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cunbdb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunbdb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cuncsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cuncsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cuncsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cuncsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cuncsd2by1  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cuncsd2by1' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cuncsd2by1… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cuncsd2by1… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dbbcsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dbbcsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dbbcsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dbbcsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorbdb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorbdb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorbdb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorbdb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorcsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorcsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dorcsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorcsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorcsd2by1  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorcsd2by1' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorcsd2by1… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorcsd2by1… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyconv     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyconv'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyconv_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyconv_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyswapr    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyswapr'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyswapr_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyswapr_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytri2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytri2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytri2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytri2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytri2x    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytri2x'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytri2x_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytri2x_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sbbcsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sbbcsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sbbcsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sbbcsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorbdb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorbdb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorbdb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorbdb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorcsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorcsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sorcsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorcsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorcsd2by1  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorcsd2by1' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorcsd2by1… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorcsd2by1… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyconv     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyconv'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyconv_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyconv_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyswapr    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyswapr'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyswapr_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyswapr_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytri2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytri2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytri2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytri2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytri2x    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytri2x'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytri2x_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytri2x_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zbbcsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zbbcsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zbbcsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zbbcsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheswapr    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheswapr'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheswapr_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheswapr_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetri2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetri2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetri2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetri2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetri2x    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetri2x'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetri2x_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetri2x_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyconv     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyconv'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyconv_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyconv_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyswapr    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyswapr'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyswapr_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyswapr_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytri2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytri2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytri2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytri2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytri2x    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytri2x'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytri2x_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytri2x_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunbdb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunbdb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zunbdb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunbdb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zuncsd      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zuncsd' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zuncsd_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zuncsd_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zuncsd2by1  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zuncsd2by1' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zuncsd2by1… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zuncsd2by1… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgemqrt     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgemqrt'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgemqrt     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgemqrt'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgemqrt     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgemqrt'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgemqrt     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgemqrt'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeqrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeqrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeqrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeqrt2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrt2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqrt2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrt2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqrt2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrt2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqrt2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrt2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqrt3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrt3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqrt3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrt3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqrt3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrt3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqrt3     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrt3'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stpmqrt     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpmqrt'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtpmqrt     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpmqrt'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctpmqrt     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpmqrt'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztpmqrt     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpmqrt'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stpqrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpqrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtpqrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpqrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctpqrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpqrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztpqrt      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpqrt' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_stpqrt2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpqrt2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtpqrt2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpqrt2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctpqrt2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpqrt2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztpqrt2     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpqrt2'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stprfb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stprfb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dtprfb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtprfb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ctprfb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctprfb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ztprfb      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztprfb' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgemqrt_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgemqrt_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgemqrt_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgemqrt_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgemqrt_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgemqrt_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgemqrt_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgemqrt_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqrt2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrt2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqrt2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrt2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqrt2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrt2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqrt2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrt2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqrt3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqrt3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqrt3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqrt3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqrt3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqrt3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqrt3_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqrt3_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stpmqrt_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpmqrt_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtpmqrt_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpmqrt_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctpmqrt_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpmqrt_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztpmqrt_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpmqrt_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stpqrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpqrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtpqrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpqrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctpqrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpqrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztpqrt_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpqrt_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stpqrt2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stpqrt2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtpqrt2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtpqrt2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctpqrt2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctpqrt2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztpqrt2_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztpqrt2_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_stprfb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_stprfb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dtprfb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dtprfb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ctprfb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ctprfb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ztprfb_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ztprfb_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysv_rook  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_rook' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_rook  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_rook' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_rook  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_rook' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_rook  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_rook' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_rook | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyr        | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyr' has   |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zsyr        | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyr' has   |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssysv_rook… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_rook… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_rook… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_rook… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_rook… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_rook… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_rook… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_rook… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_roo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_roo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csyr_work   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csyr_work'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsyr_work   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsyr_work'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ilaver      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ilaver' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_ssysv_aa    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_aa'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysv_aa_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_aa_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_aa    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_aa'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_aa_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_aa_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_aa    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_aa'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_aa_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_aa_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_aa    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_aa'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_aa_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_aa_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesv_aa    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesv_aa'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesv_aa_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesv_aa_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesv_aa    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesv_aa'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesv_aa_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesv_aa_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_aa   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_aa'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysv_rk    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_rk'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysv_rk_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_rk_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_rk    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_rk'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_rk_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_rk_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_rk    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_rk'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_rk_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_rk_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_rk    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_rk'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_rk_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_rk_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesv_rk    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesv_rk'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesv_rk_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesv_rk_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesv_rk    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesv_rk'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesv_rk_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesv_rk_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_rk   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_rk'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_rk   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_rk'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_rk   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_rk'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_rk   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_rk'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_rk   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_rk'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_rk   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_rk'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_rk_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_rk_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_rk_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_rk_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_rk_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_rk_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_rk_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_rk_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_rk_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_rk_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_rk_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_rk_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytri_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytri_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytri_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytri_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytri_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytri_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytri_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytri_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetri_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetri_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetri_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetri_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytri_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytri_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytri_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytri_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytri_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytri_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytri_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytri_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetri_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetri_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetri_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetri_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssycon_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssycon_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsycon_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsycon_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csycon_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csycon_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsycon_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsycon_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_checon_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_checon_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhecon_3    | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhecon_3'   |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssycon_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssycon_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsycon_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsycon_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csycon_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csycon_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsycon_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsycon_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_checon_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_checon_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhecon_3_w… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhecon_3_w… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgelq       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelq' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgelq       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelq' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgelq       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelq' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgelq       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelq' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgelq_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgelq_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgelq_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgelq_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgelq_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgelq_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgelq_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgelq_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgemlq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgemlq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgemlq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgemlq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgemlq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgemlq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgemlq      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgemlq' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgemlq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgemlq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgemlq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgemlq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgemlq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgemlq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgemlq_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgemlq_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgeqr       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqr' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgeqr       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqr' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgeqr       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqr' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgeqr       | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqr' has  |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgeqr_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgeqr_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgeqr_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgeqr_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgeqr_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgeqr_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgeqr_work  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgeqr_work' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgemqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgemqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_dgemqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgemqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_cgemqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgemqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_zgemqr      | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgemqr' has |
|          |                     |                     | no Fortran BIND(C)   |
|          |                     |                     | declaration          |
| WARNING  | LAPACKE_sgemqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgemqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgemqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgemqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgemqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgemqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgemqr_work | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgemqr_wor… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetsls     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetsls'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetsls     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetsls'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetsls     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetsls'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetsls     | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetsls'    |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetsls_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetsls_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetsls_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetsls_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetsls_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetsls_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetsls_wo… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetsls_wo… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetsqrhrt  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetsqrhrt' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetsqrhrt  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetsqrhrt' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetsqrhrt  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetsqrhrt' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetsqrhrt  | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetsqrhrt' |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sgetsqrhrt… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sgetsqrhrt… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dgetsqrhrt… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dgetsqrhrt… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cgetsqrhrt… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cgetsqrhrt… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zgetsqrhrt… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zgetsqrhrt… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevr_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevr_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevr_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevr_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevr_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevr_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevr_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevr_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssyevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssyevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsyevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsyevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevr_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevr_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevr_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevr_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevr_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevr_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevr_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevr_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cheevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cheevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zheevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zheevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssbevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssbevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsbevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsbevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbev_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbev_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbevd_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbevd_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chbevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chbevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhbevx_2st… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhbevx_2st… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssygv_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygv_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsygv_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygv_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssygv_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssygv_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsygv_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsygv_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chegv_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegv_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhegv_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegv_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chegv_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chegv_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhegv_2sta… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhegv_2sta… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssysv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssysv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsysv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsysv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csysv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csysv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsysv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsysv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chesv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chesv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhesv_aa_2… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhesv_aa_2… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrf_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrf_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_ssytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_ssytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dsytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dsytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_csytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_csytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zsytrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zsytrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_chetrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_chetrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zhetrs_aa_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zhetrs_aa_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorhr_col   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorhr_col'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_sorhr_col_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_sorhr_col_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorhr_col   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorhr_col'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_dorhr_col_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_dorhr_col_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunhr_col   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunhr_col'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_cunhr_col_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_cunhr_col_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunhr_col   | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunhr_col'  |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_zunhr_col_… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_zunhr_col_… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_set_nanche… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_set_nanche… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
| WARNING  | LAPACKE_get_nanche… | Unmatched procedure | C function           |
|          |                     |                     | 'LAPACKE_get_nanche… |
|          |                     |                     | has no Fortran       |
|          |                     |                     | BIND(C) declaration  |
+-----------------------------------------------------------------------------+

Summary: 0 Errors, 2520 Warnings


## Case 2: dgemm.f

