/* header.h  — built on Windows */
void file_seek(int fd, long offset);
/* On Linux: long=8, Fortran c_long=8  → OK
   On Windows: long=4, Fortran c_long=4 → OK locally
   Cross-compiled Linux→Windows: c_long stays 8, C long becomes 4 → CRASH */