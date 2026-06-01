/* fem_bridge_fixed.c — Fixed C Bridge */
#include <stdio.h>

/* Declare the BIND(C) Fortran procedure (matches C signature perfectly) */
extern void compute_displacement(const char *material, int nx, int ny, 
                                 double load, double *result);

/* Clean C entry point for Flask ctypes calling */
double run_solver(char *material, long nx, long ny, double load) {
    double result = 0.0;
    
    printf("[C Bridge] Calling compute_displacement (Fixed BIND(C) ABI)...\n");
    printf("[C Bridge] Passed: material=%s, nx=%ld, ny=%ld, load=%.2f\n", material, nx, ny, load);
    
    /* Perfect match: Pass values directly as expected, map long to int */
    compute_displacement(material, (int)nx, (int)ny, load, &result);
    
    printf("[C Bridge] Returned result = %.2f\n", result);
    return result;
}
