#!/bin/bash
# build.sh - Set up virtual environment and install FCValidator and dependencies
set -e

echo "=== FCValidator Builder ==="

# 1. Install system dependencies if on Ubuntu/Debian
if command -v apt-get &>/dev/null; then
    echo "Installing system dependencies..."
    sudo apt-get update && sudo apt-get install -y python3-pip python3-venv libclang-dev
fi

# 2. Check Python installation
if ! command -v python3 &>/dev/null; then
    echo "Error: Python 3 is required but not found in PATH." >&2
    exit 1
fi

# 3. Create virtual environment if it does not exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment '.venv'..."
    python3 -m venv .venv
else
    echo "Virtual environment '.venv' already exists."
fi

# 4. Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# 5. Install the package in editable mode with development dependencies
echo "Installing package in editable developer mode..."
pip install --upgrade pip
pip install -e ".[dev]"

echo ""
echo "=================================================="
echo "Installation complete successfully!"
echo "To run the validator manually, activate the venv:"
echo "  source .venv/bin/activate"
echo "  fcv --help"
echo "Or execute the demonstration suite via: ./run.sh"
echo "=================================================="
