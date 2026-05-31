/* header.h  — written assuming f2c/g77 ABI */
typedef struct { float re; float im; } complex_f;
void complex_add(complex_f *result, const complex_f *a, const complex_f *b);