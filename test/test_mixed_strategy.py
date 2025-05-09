"""
Test file for the mixed strategy model.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mixed_strategy import get_action

def test_strategy():
    """
    Test the mixed strategy with different scenarios.
    """
    # Initialize game with 10 rounds
    T = 10
    my_action = [None] * (T + 1)  # 1-indexed, so we need T+1 elements
    partner_action = [None] * (T + 1)
    state = "Happy"

    # Simulate a game where opponent always cooperates
    print("Scenario 1: Opponent always cooperates")
    for round in range(1, T + 1):
        partner_action[round] = "C"  # Opponent's action in current round

        action, state = get_action(my_action, partner_action, state, T, round)
        my_action[round] = action

        print(f"Round {round}: My action = {action}, State = {state}")

    print("\n" + "-" * 50 + "\n")

    # Reset for next scenario
    my_action = [None] * (T + 1)
    partner_action = [None] * (T + 1)
    state = "Happy"

    # Simulate a game where opponent always defects
    print("Scenario 2: Opponent always defects")
    for round in range(1, T + 1):
        partner_action[round] = "D"  # Opponent's action in current round

        action, state = get_action(my_action, partner_action, state, T, round)
        my_action[round] = action

        print(f"Round {round}: My action = {action}, State = {state}")

    print("\n" + "-" * 50 + "\n")

    # Reset for next scenario
    my_action = [None] * (T + 1)
    partner_action = [None] * (T + 1)
    state = "Happy"

    # Simulate a game with mixed opponent behavior
    print("Scenario 3: Mixed opponent behavior")
    # Define opponent's behavior pattern
    opponent_pattern = ["C", "C", "D", "C", "D", "D", "C", "C", "D", "C"]

    for round in range(1, T + 1):
        partner_action[round] = opponent_pattern[round-1]

        action, state = get_action(my_action, partner_action, state, T, round)
        my_action[round] = action

        print(f"Round {round}: My action = {action}, State = {state}")
        print(f"  Opponent's action: {partner_action[round]}")

if __name__ == "__main__":
    test_strategy()
