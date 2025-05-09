"""
Test file to verify state persistence in the mixed strategy model.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mixed_strategy import get_action

def test_state_persistence():
    """
    Test that the state persists correctly when manually set.
    """
    # Initialize game with 10 rounds
    T = 10
    my_action = [None] * (T + 1)  # 1-indexed, so we need T+1 elements
    partner_action = [None] * (T + 1)

    # Test with manually setting the state to "Angry" in the T-Spiteful phase
    print("Testing state persistence with manually set 'Angry' state")
    print(f"Switch to T-Spiteful occurs at round {int(T * 0.7)}")
    print("Round | My Action | State | Opponent's Action")
    print("-" * 45)

    # Start with "Happy" state
    state = "Happy"

    # All opponent actions are cooperation
    for i in range(1, T + 1):
        partner_action[i] = "C"

    # Run the first 7 rounds normally (70% of 10 rounds is 7)
    for round in range(1, 8):
        action, state = get_action(my_action, partner_action, state, T, round)
        my_action[round] = action

        opponent_action = partner_action[round]
        print(f"{round:5d} | {action:9s} | {state:5s} | {opponent_action}")

    # Manually set state to "Angry" and continue
    state = "Angry"
    print("* Manually setting state to 'Angry' at round 8 *")

    # Continue with remaining rounds
    for round in range(8, T + 1):
        action, state = get_action(my_action, partner_action, state, T, round)
        my_action[round] = action

        opponent_action = partner_action[round]
        print(f"{round:5d} | {action:9s} | {state:5s} | {opponent_action}")

if __name__ == "__main__":
    test_state_persistence()
