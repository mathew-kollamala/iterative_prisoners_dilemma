# Iterative Prisoner's Dilemma - Comprehensive Documentation

## Overview

This project implements a mixed strategy model for the Iterative Prisoner's Dilemma game. The mixed strategy combines two well-known strategies:

1. **Gradual Strategy**: Cooperates by default, but if the opponent defects, it punishes with a number of defections equal to the cumulative defections by the opponent up to that point.
2. **T-Spiteful Strategy**: Plays tit-for-tat unless betrayed twice consecutively, then always defects.

The mixed strategy switches from Gradual to T-Spiteful at 70% of the game and always defects in the last two rounds.

## Prisoner's Dilemma

The Prisoner's Dilemma is a classic game theory scenario where two players must choose to either cooperate (C) or defect (D). The payoffs depend on the combination of choices:

| Player 1 | Player 2 | Player 1 Score | Player 2 Score |
|----------|----------|----------------|----------------|
| C        | C        | 3              | 3              |
| C        | D        | 0              | 5              |
| D        | C        | 5              | 0              |
| D        | D        | 1              | 1              |

In the iterative version, the game is played repeatedly, allowing players to develop strategies based on the history of interactions.

## Project Structure

```
iterative_prisoners_dilemma/
├── .build/                # Build process scripts
├── .config/               # Configuration files
├── .gitignore             # Git ignore file
├── README.md              # Project overview
├── dep/                   # Project dependencies
├── doc/                   # Additional documentation
│   ├── DOCUMENTATION.md   # This comprehensive documentation
│   └── README.md          # Quick reference documentation
├── res/                   # Static resources
├── samples/               # Example code
│   └── simple_game.py     # Simple example of using the mixed strategy
├── src/                   # Source code
│   └── mixed_strategy.py  # Implementation of the mixed strategy
├── test/                  # Test files
│   ├── sim_game.py        # Simulation with 100 rounds and scoring
│   ├── test_gradual_punishment.py  # Tests for gradual strategy
│   ├── test_mixed_strategy.py      # Tests for mixed strategy
│   └── test_state_persistence.py   # Tests for state persistence
└── tools/                 # Utility scripts
    └── run_simulation.sh  # Script to run simulations
```

## Strategies in Detail

### Gradual Strategy

The Gradual strategy is a forgiving strategy that cooperates by default but punishes defections proportionally:

1. Always cooperate in the first round
2. If the opponent defects, punish with a number of defections equal to the total number of times the opponent has defected so far
3. After completing the punishment cycle, return to cooperation

This strategy is effective against occasional defectors while maintaining cooperation with cooperative players.

### T-Spiteful Strategy

The T-Spiteful strategy is a variant of Tit-for-Tat with a permanent punishment mechanism:

1. Start by cooperating
2. If the opponent defects once, respond with a defection in the next round (like Tit-for-Tat)
3. If the opponent defects twice in a row, switch to permanent defection

The strategy uses a state variable ("Happy" or "Angry") to track whether it has seen two consecutive defections.

### Mixed Strategy

The mixed strategy combines both approaches:

1. Use the Gradual strategy for the first 70% of the game
2. Switch to the T-Spiteful strategy for the remaining 30%
3. Always defect in the last two rounds regardless of the opponent's actions

This combination aims to be forgiving in the early game while becoming more protective in the later stages.

## Implementation Details

### State Management

The mixed strategy uses a state variable to track the current mode:

- "Happy": Normal operation (Gradual or T-Spiteful depending on the game phase)
- "Angry": Permanent defection mode (triggered by two consecutive defections in T-Spiteful phase)

### Scoring System

The project uses the standard Prisoner's Dilemma payoff matrix:

- Both cooperate (C,C): 3,3
- Player defects, opponent cooperates (D,C): 5,0
- Player cooperates, opponent defects (C,D): 0,5
- Both defect (D,D): 1,1

### Configuration

Key parameters are configurable in `.config/settings.json`:

- `default_rounds`: Default number of rounds (10)
- `strategy_switch_percentage`: When to switch from Gradual to T-Spiteful (0.7 or 70%)
- `always_defect_last_rounds`: Number of rounds at the end to always defect (2)

## Usage Examples

### Basic Usage

```python
from src.mixed_strategy import get_action

# Initialize game parameters
T = 10  # Total number of rounds
my_action = [None] * (T + 1)  # 1-indexed
partner_action = [None] * (T + 1)  # 1-indexed
state = "Happy"  # Initial state

# For each round
for round in range(1, T + 1):
    # Set opponent's action for the current round
    partner_action[round] = opponent_action  # Replace with actual opponent action
    
    # Get your action using the mixed strategy
    action, state = get_action(my_action, partner_action, state, T, round)
    my_action[round] = action
```

### Running the Simulation

To run the 100-round simulation with scoring:

```bash
python -m test.sim_game
```

This will output:
- All 100 moves with actions and states
- Round-by-round scores
- Cumulative scores
- State changes
- Summary statistics
- Phase analysis

### Running Tests

To run the test suite:

```bash
bash .build/run_tests.sh
```

Or run individual tests:

```bash
python -m test.test_mixed_strategy
python -m test.test_gradual_punishment
python -m test.test_state_persistence
```

## Performance Analysis

The mixed strategy performs well against various opponent types:

1. **Against cooperative opponents**: Achieves high mutual cooperation in the Gradual phase, then exploits the opponent in the T-Spiteful phase for maximum points.

2. **Against defecting opponents**: Quickly punishes defections in the Gradual phase, then permanently defects in the T-Spiteful phase to minimize exploitation.

3. **Against mixed behavior**: Adapts to the opponent's pattern, punishing defections proportionally while maintaining cooperation when possible.

In the 100-round simulation with a highly cooperative opponent (85-90% cooperation), the strategy typically scores about twice as many points as the opponent.

## Future Improvements

Potential enhancements to consider:

1. **Dynamic strategy switching**: Adjust the switch point based on the opponent's behavior
2. **Learning mechanism**: Adapt the strategy based on the success of previous actions
3. **Parameter optimization**: Fine-tune the strategy parameters for different opponent types
4. **Additional strategies**: Implement more strategies like Pavlov, Generous Tit-for-Tat, etc.
5. **Tournament support**: Add functionality to run round-robin tournaments with multiple strategies

## References

1. Axelrod, R. (1984). The Evolution of Cooperation. Basic Books.
2. Beaufils, B., Delahaye, J. P., & Mathieu, P. (1996). Our meeting with gradual, a good strategy for the iterated prisoner's dilemma. In Proceedings of the Fifth International Workshop on the Synthesis and Simulation of Living Systems (pp. 202-209).
3. Tzafestas, E. (2000). Toward adaptive cooperative behavior. In Proceedings of the Simulation of Adaptive Behavior Conference (pp. 334-340).
