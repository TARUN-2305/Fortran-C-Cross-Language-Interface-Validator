/* header.h */
#pragma pack(1)   /* packed: NO padding inserted */
typedef struct {
  signed char method;    /* 1 byte @ offset 0 */
  double tolerance;      /* 8 bytes @ offset 1 (MISALIGNED!) */
  int max_iter;          /* 4 bytes @ offset 9 */
  double relax;          /* 8 bytes @ offset 13 (MISALIGNED!) */
} grid_params;
#pragma pack()
void dummy_proc(struct grid_params x);
