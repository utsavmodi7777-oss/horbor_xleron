#!/bin/bash

# Check if all output files exist
if [ ! -f /app/word_output.txt ]; then
    echo "ERROR: /app/word_output.txt not found"
    exit 1
fi

if [ ! -f /app/csv_output.txt ]; then
    echo "ERROR: /app/csv_output.txt not found"
    exit 1
fi

if [ ! -f /app/json_output.txt ]; then
    echo "ERROR: /app/json_output.txt not found"
    exit 1
fi

# Run validation tests
python3 /tests/test_outputs.py

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
