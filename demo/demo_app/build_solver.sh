#!/bin/bash
# build_solver.sh - Compile both buggy and fixed solvers as shared libraries
set -e

echo "=== FCValidator Solver Compiler ==="

# 1. Check for gfortran
if ! command -v gfortran &>/dev/null; then
    echo "Error: gfortran is required but not found in PATH." >&2
    exit 1
fi

# 2. Check for gcc
if ! command -v gcc &>/dev/null; then
    echo "Error: gcc is required but not found in PATH." >&2
    exit 1
fi

# 3. Detect Platform OS and select shared library extension
OS_SUFFIX="so"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" || "$OS" == "Windows_NT" ]]; then
    OS_SUFFIX="dll"
fi

echo "Platform Detected: shared library suffix is .$OS_SUFFIX"

# 4. Compile Buggy Shared Library
echo "Compiling Buggy Solver (fem_solver_buggy.f90 + fem_bridge_buggy.c)..."
gfortran -c solver/fem_solver_buggy.f90 -o solver/fem_solver_buggy.o -fPIC
gcc -c solver/fem_bridge_buggy.c -o solver/fem_bridge_buggy.o -fPIC
gcc -shared solver/fem_solver_buggy.o solver/fem_bridge_buggy.o -o libfem_solver_buggy.$OS_SUFFIX -lgfortran

# 5. Compile Fixed Shared Library
echo "Compiling Fixed Solver (fem_solver_fixed.f90 + fem_bridge_fixed.c)..."
gfortran -c solver/fem_solver_fixed.f90 -o solver/fem_solver_fixed.o -fPIC
gcc -c solver/fem_bridge_fixed.c -o solver/fem_bridge_fixed.o -fPIC
gcc -shared solver/fem_solver_fixed.o solver/fem_bridge_fixed.o -o libfem_solver_fixed.$OS_SUFFIX -lgfortran

echo ""
echo "=================================================="
echo "Solvers compiled successfully!"
echo "  - Buggy library: libfem_solver_buggy.$OS_SUFFIX"
echo "  - Fixed library: libfem_solver_fixed.$OS_SUFFIX"
echo "=================================================="
