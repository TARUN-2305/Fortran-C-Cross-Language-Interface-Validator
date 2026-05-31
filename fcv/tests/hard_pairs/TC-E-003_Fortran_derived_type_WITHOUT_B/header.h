/* header.h */
typedef struct {
  int nx, ny, nz;
  double dx, dy, dz;
  int periodic;   /* or _Bool */
} mesh_config;
void init_mesh(const mesh_config *cfg);