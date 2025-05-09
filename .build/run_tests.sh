#!/bin/bash

# Simple script to run all tests

echo "Running all tests for Iterative Prisoner's Dilemma"
echo "=================================================="

# Run each test file
for test_file in ../test/test_*.py; do
    echo "Running $test_file..."
    python3 "$test_file"
    echo ""
done

echo "All tests completed."
