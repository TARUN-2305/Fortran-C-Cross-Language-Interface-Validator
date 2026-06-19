#include <stdio.h>

void c_add(int a, float b, float *result) {
    printf("[C Code] Received integer a = %d\n", a);
    printf("[C Code] Received float b = %.4f\n", b);
    *result = (float)a + b;
    printf("[C Code] Computed sum to result pointer: %.4f\n", *result);
}
