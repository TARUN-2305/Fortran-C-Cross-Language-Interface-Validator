/* header.h */
typedef struct { double re; double im; } cdouble;
void apply_phase(cdouble *data, int n, cdouble phase);