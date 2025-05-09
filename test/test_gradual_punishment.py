"""
Test file to verify the Gradual strategy's punishment mechanism.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mixed_strategy import gradual_strategy

def test_gradual_punishment():
    """
    Test that the Gradual strategy correctly punishes defections.
    """
    # Initialize a 15-round game
    rounds = 15
    my_action = [None] * (rounds + 1)  # 1-indexed, so we need rounds+1 elements
    partner_action = [None] * (rounds + 1)

    # Define a specific opponent behavior pattern to test punishment
    # The opponent defects in rounds 3, 7, and 8
    opponent_pattern = [
        "C",  # Round 1
        "C",  # Round 2
        "D",  # Round 3 - First defection
        "C",  # Round 4
        "C",  # Round 5
        "C",  # Round 6
        "D",  # Round 7 - Second defection
        "D",  # Round 8 - Third defection
        "C",  # Round 9
        "C",  # Round 10
        "C",  # Round 11
        "C",  # Round 12
        "C",  # Round 13
        "C",  # Round 14
        "C",  # Round 15
    ]

    print("Testing Gradual strategy's punishment mechanism")
    print("Round | My Action | Opponent's Action | Total Opponent Defections | My Total Defections")
    print("-" * 90)

    for round in range(1, rounds + 1):
        # Set opponent's action for the current round
        partner_action[round] = opponent_pattern[round-1]

        # Determine my action using the Gradual strategy
        my_action[round] = gradual_strategy(my_action, partner_action, round)

        # Calculate statistics for display
        opponent_defections = partner_action[:round].count("D") if round > 1 else 0
        my_defections = my_action[:round].count("D")

        # Display the results
        opponent_action = partner_action[round]
        print(f"{round:5d} | {my_action[round]:9s} | {opponent_action:17s} | {opponent_defections:26d} | {my_defections:18d}")

if __name__ == "__main__":
    test_gradual_punishment()
