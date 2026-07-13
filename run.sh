#!/bin/bash
# run.sh - Activate virtual environment and demonstrate FCValidator on key test cases
set -e

echo "=== FCValidator Demonstration Suite ==="
echo ""

# 1. Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment '.venv' not found. Please run ./build.sh first." >&2
    exit 1
fi

# 2. Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

echo ""
echo "=================================================="
echo "DEMO 1: Hidden strlen bug (TC-A-001 - Failure Case)"
echo "=================================================="
fcv validate fcv/tests/hard_pairs/TC-A-001_Single_character_flag_no_BIND_/interface.f90 \
             fcv/tests/hard_pairs/TC-A-001_Single_character_flag_no_BIND_/header.h \
             --severity warning || true

echo ""
echo "=================================================="
echo "DEMO 2: INTEGER vs long (TC-B-001 - Failure Case)"
echo "=================================================="
fcv validate fcv/tests/hard_pairs/TC-B-001_INTEGER_vs_long_on_LP64_Linux_/interface.f90 \
             fcv/tests/hard_pairs/TC-B-001_INTEGER_vs_long_on_LP64_Linux_/header.h \
             --severity warning || true

echo ""
echo "=================================================="
echo "DEMO 3: Correct interface (TC-A-003 - Clean Case)"
echo "=================================================="
fcv validate fcv/tests/hard_pairs/TC-A-003_Correct_BIND_C_version_of_TC_A/interface.f90 \
             fcv/tests/hard_pairs/TC-A-003_Correct_BIND_C_version_of_TC_A/header.h \
             --severity warning

echo ""
echo "=================================================="
echo "DEMO 4: Running full Pytest suite (58 unique tests)"
echo "=================================================="
pytest fcv/tests/ -v --tb=short

echo ""
echo "=================================================="
echo "DEMO COMPLETE!"
echo "Refer to README.md for comprehensive project details."
echo "=================================================="
