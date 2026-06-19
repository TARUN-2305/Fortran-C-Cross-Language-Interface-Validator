/* fem_bridge_buggy.c — Buggy C Bridge */
#include <stdio.h>

/* Declare the BIND(C) Fortran procedure (using matching C name) */
/* But C expects to pass nx and load by VALUE, which is a mismatch */
extern void compute_displacement(const char *material, long nx, 
                                 double load, double *result);

/* Clean C entry point for Flask ctypes calling */
double run_solver(char *material, long nx, double load) {
    double result = -999.0;
    
    printf("[C Bridge] Calling compute_displacement (Buggy BIND(C) ABI)...\n");
    printf("[C Bridge] Passed: material=%s, nx=%ld, load=%.2f\n", material, nx, load);
    
    /* Mismatched Call: Pass values directly by value, but Fortran expects references */
    compute_displacement(material, nx, load, &result);
    
    printf("[C Bridge] Returned result = %.2f\n", result);
    return result;
}
