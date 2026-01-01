#!/bin/bash
set -e

# Check if output file exists
if [ ! -f /app/output.txt ]; then
    echo "ERROR: output.txt not found"
    exit 1
fi

# Run Python tests
python3 /tests/test_outputs.py

exit 0
