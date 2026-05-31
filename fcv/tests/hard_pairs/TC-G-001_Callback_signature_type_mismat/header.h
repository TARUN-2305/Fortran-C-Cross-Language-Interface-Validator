/* header.h */
typedef double (*integrand_fn)(double x);
void register_integrand(integrand_fn cb);