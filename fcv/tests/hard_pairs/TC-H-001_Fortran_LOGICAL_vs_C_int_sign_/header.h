/* header.h */
void set_flag(int *flag);
/* Caller checks: if (flag == 1) { ... }
   GFortran sets flag to -1 (0xFFFFFFFF). Check FAILS silently. */