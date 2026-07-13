#include <stdio.h>

// Buggy C declaration: C passes double by value, but Fortran expects references (pointers).
// The symbol is mangled as calculate_force_ by gfortran.
extern void calculate_force_(double mass, double acceleration, double* force);

int main() {
    double mass = 5.0;
    double acceleration = 9.8;
    double force = 0.0;

    printf("Calling calculate_force_ with mass=%f, acceleration=%f...\n", mass, acceleration);
    fflush(stdout);

    // This will cause a Segmentation Fault because Fortran expects mass and acceleration
    // to be pointers (double*), but C is passing values (double) directly in registers!
    calculate_force_(mass, acceleration, &force);

    printf("Result force: %f\n", force);
    return 0;
}
