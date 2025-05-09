#!/bin/bash

# Script to run a simulation with different parameters

# Default values
ROUNDS=10
OPPONENT_STRATEGY="random"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -r|--rounds)
        ROUNDS="$2"
        shift
        shift
        ;;
        -o|--opponent)
        OPPONENT_STRATEGY="$2"
        shift
        shift
        ;;
        -h|--help)
        echo "Usage: $0 [options]"
        echo "Options:"
        echo "  -r, --rounds NUMBER    Number of rounds to play (default: 10)"
        echo "  -o, --opponent TYPE    Opponent strategy: random, tit-for-tat, always-defect, always-cooperate (default: random)"
        echo "  -h, --help             Show this help message"
        exit 0
        ;;
        *)
        echo "Unknown option: $1"
        exit 1
        ;;
    esac
done

echo "Running simulation with $ROUNDS rounds and $OPPONENT_STRATEGY opponent strategy"
echo "This is a placeholder for an actual simulation runner"
echo "In a real implementation, this would run the game with the specified parameters"
