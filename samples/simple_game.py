"""
Simple example of using the mixed strategy in a game.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mixed_strategy import get_action

def run_simple_game():
    """
    Run a simple 10-round game with a predetermined opponent.
    """
    # Initialize game with 10 rounds
    T = 10
    my_action = [None] * (T + 1)  # 1-indexed
    partner_action = [None] * (T + 1)  # 1-indexed
    state = "Happy"
    
    # Define a simple opponent behavior pattern
    opponent_pattern = ["C", "C", "D", "C", "D", "D", "C", "C", "D", "C"]
    
    print("Running a simple 10-round Prisoner's Dilemma game")
    print("Round | My Action | State | Opponent's Action")
    print("-" * 45)
    
    for round in range(1, T + 1):
        # Set opponent's action for the current round
        partner_action[round] = opponent_pattern[round-1]
        
        # Get my action using the mixed strategy
        action, state = get_action(my_action, partner_action, state, T, round)
        my_action[round] = action
        
        # Display the results
        print(f"{round:5d} | {action:9s} | {state:5s} | {partner_action[round]}")
    
    # Print a summary of the game
    print("\nSummary:")
    print(f"Total cooperations: {my_action[1:].count('C')}")
    print(f"Total defections: {my_action[1:].count('D')}")
    print(f"Cooperation rate: {my_action[1:].count('C') / T:.2f}")

if __name__ == "__main__":
    run_simple_game()
