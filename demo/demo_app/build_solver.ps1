# build_solver.ps1 - Compile buggy and fixed solvers on Windows natively
Write-Host "=== FCValidator Solver Compiler (Windows Native) ===" -ForegroundColor Cyan

# 1. Check for compilers in PATH
if (!(Get-Command gfortran -ErrorAction SilentlyContinue)) {
    Write-Error "gfortran is required but not found in your PATH. Please install MinGW-w64."
    Exit 1
}

if (!(Get-Command gcc -ErrorAction SilentlyContinue)) {
    Write-Error "gcc is required but not found in your PATH. Please install MinGW-w64."
    Exit 1
}

# 2. Compile Buggy DLL
Write-Host "Compiling Buggy Solver (libfem_solver_buggy.dll)..." -ForegroundColor Yellow
gfortran -c solver\fem_solver_buggy.f90 -o solver\fem_solver_buggy.o
gcc -c solver\fem_bridge_buggy.c -o solver\fem_bridge_buggy.o
gcc -shared solver\fem_solver_buggy.o solver\fem_bridge_buggy.o -o libfem_solver_buggy.dll -lgfortran

# 3. Compile Fixed DLL
Write-Host "Compiling Fixed Solver (libfem_solver_fixed.dll)..." -ForegroundColor Yellow
gfortran -c solver\fem_solver_fixed.f90 -o solver\fem_solver_fixed.o
gcc -c solver\fem_bridge_fixed.c -o solver\fem_bridge_fixed.o
gcc -shared solver\fem_solver_fixed.o solver\fem_bridge_fixed.o -o libfem_solver_fixed.dll -lgfortran

Write-Host ""
Write-Host "==================================================" -ForegroundColor Green
Write-Host "Build complete successfully!" -ForegroundColor Green
Write-Host "  - Buggy library: libfem_solver_buggy.dll" -ForegroundColor Green
Write-Host "  - Fixed library: libfem_solver_fixed.dll" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
