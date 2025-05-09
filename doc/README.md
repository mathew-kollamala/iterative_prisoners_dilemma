# Iterative Prisoner's Dilemma

This project implements a mixed strategy model for the Iterative Prisoner's Dilemma game.

## Strategies

### Gradual Strategy
Cooperates by default, but if the opponent defects, it punishes with a number of defections equal to the cumulative defections by the opponent up to that point.

### T-Spiteful Strategy
Plays tit-for-tat unless betrayed twice consecutively, then always defects.

### Mixed Strategy
Combines both strategies:
- Uses Gradual strategy until 70% of the game
- Switches to T-Spiteful strategy after 70% of the game
- Always defects in the last two rounds

## Usage

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

## Testing

Run the tests using:

```bash
python -m test.test_mixed_strategy
python -m test.test_gradual_punishment
python -m test.test_state_persistence
```

## Simulation

Run the simulation with scoring:

```bash
python -m test.sim_game
```
