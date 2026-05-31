/* header.h */
typedef struct {
  double charge;   /* was mass in Fortran */
  double mass;     /* was charge in Fortran */
  int    id;
} particle;
void dummy_proc(struct particle x);
