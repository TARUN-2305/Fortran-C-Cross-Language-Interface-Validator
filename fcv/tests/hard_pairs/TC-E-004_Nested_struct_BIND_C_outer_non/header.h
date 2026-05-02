/* header.h */
typedef struct { int a; int b; } inner_t;
typedef struct { inner_t inner; double val; } outer_t;
void dummy_proc(struct outer_struct x);
