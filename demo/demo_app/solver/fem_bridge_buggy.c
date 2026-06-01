/* fem_bridge_buggy.c — Buggy C Bridge */
#include <stdio.h>
#include <string.h>

/* Declare the legacy Fortran subroutine (mangled with trailing underscore) */
/* nx and ny are declared as long* (8-byte pointers on LP64) */
extern void compute_displacement_(char *material, long *nx, long *ny, 
                                  double *load, double *result);

/* Clean C entry point for Flask ctypes calling */
double run_solver(char *material, long nx, long ny, double load) {
    double result = -999.0;
    
    printf("[C Bridge] Calling compute_displacement_ (Buggy legacy ABI)...\n");
    printf("[C Bridge] Passed: material=%s, nx=%ld, ny=%ld, load=%.2f\n", material, nx, ny, load);
    
    /* Mismatched Call: Omit the hidden string length size_t parameters! */
    /* Also passing pointers to 8-byte long instead of 4-byte int */
    compute_displacement_(material, &nx, &ny, &load, &result);
    
    printf("[C Bridge] Returned result = %.2f\n", result);
    return result;
}
