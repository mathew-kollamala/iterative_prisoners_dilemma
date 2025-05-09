# Iterative Prisoner's Dilemma

A mixed strategy model for round robin style iterative prisoner's dilemma.

## Project Structure

- `src/`: Source code for the mixed strategy model
- `test/`: Unit tests for the strategies
- `.config/`: Local configuration files
- `.build/`: Build process scripts
- `dep/`: Project dependencies
- `doc/`: Documentation
- `res/`: Static resources
- `samples/`: Example code
- `tools/`: Utility scripts

## Getting Started

1. Clone the repository
2. Run the sample code:
   ```
   python samples/simple_game.py
   ```
3. Run the tests:
   ```
   bash .build/run_tests.sh
   ```

## Strategies

The project implements a mixed strategy model that combines:

1. **Gradual Strategy**: Cooperates unless opponent defects, then punishes with defections equal to the cumulative defections by the opponent
2. **T-Spiteful Strategy**: Plays tit-for-tat unless betrayed twice consecutively, then always defects

The mixed strategy switches from Gradual to T-Spiteful at 70% of the game, and always defects in the last two rounds.

## Documentation

For more detailed documentation:
- Quick reference: [doc/README.md](doc/README.md)
- Comprehensive documentation: [doc/DOCUMENTATION.md](doc/DOCUMENTATION.md)
