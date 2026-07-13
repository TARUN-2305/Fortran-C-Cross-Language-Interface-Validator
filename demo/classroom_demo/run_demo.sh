#!/bin/bash
# run_demo.sh - Classroom demonstration of silent ABI mismatch detection
set -e

# Resolve directories
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Activate virtual environment
if [ -d "../../.venv" ]; then
    source ../../.venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Warning: Virtual environment not found. Please activate it manually."
fi

echo "=================================================="
echo "STEP 1: Validating BUGGY interface pair"
echo "=================================================="
# We run without -e check so that validation failures don't halt script
fcv validate particle_tracker_buggy.f90 particle_tracker_buggy.h --use-flang || true

echo ""
echo "=================================================="
echo "STEP 2: Validating FIXED interface pair"
echo "=================================================="
fcv validate particle_tracker_fixed.f90 particle_tracker_fixed.h --use-flang
