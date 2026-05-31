/* header.h */
void get_values(void (*cproc)(double));
/* BUG: if cproc is not 8-byte aligned on Apple ARM64, bit 2 may be set.
   C_F_PROCPOINTER clears bit 2. Branch target shifted by 4 bytes.
   Workaround: compile C with -falign-functions=8 */