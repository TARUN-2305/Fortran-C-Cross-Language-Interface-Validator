#include <stdio.h>

// Clean BIND(C) prototype matching standard interop rules.
void calculate_force(double mass, double acceleration, double* force);

int main() {
    double mass = 5.0;
    double acceleration = 9.8;
    double force = 0.0;

    printf("Calling calculate_force with mass=%f, acceleration=%f...\n", mass, acceleration);
    fflush(stdout);

    // Safe call using standard BIND(C) interop
    calculate_force(mass, acceleration, &force);

    printf("Result force: %f (Expected: 49.0)\n", force);
    return 0;
}
