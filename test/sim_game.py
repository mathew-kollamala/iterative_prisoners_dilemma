"""
Simulation file for the mixed strategy model with a 100-round game.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mixed_strategy import get_action

def sim_game():
    """
    Simulate a 100-round game to observe strategy transitions and calculate scores.
    """
    # Initialize game with 100 rounds
    T = 100
    my_action = [None] * (T + 1)  # 1-indexed, so we need T+1 elements
    partner_action = [None] * (T + 1)
    state = "Happy"

    # Generate a pattern with random cooperation rate between 50% and 90%
    import random

    # Generate a random cooperation rate between 0.5 (50%) and 0.9 (90%)
    coop_probability = random.uniform(0.5, 0.9)

    # Create a pattern with the random cooperation rate
    opponent_pattern = []
    for _ in range(T):
        if random.random() < coop_probability:
            opponent_pattern.append("C")
        else:
            opponent_pattern.append("D")

    # Count the actual cooperation rate
    coop_rate = opponent_pattern.count("C") / len(opponent_pattern)

    print(f"Testing a longer game ({T} rounds) with variable opponent behavior")
    print(f"Target cooperation rate: {coop_probability:.2f} (randomly selected between 0.5 and 0.9)")
    print(f"Actual cooperation rate: {coop_rate:.2f} ({opponent_pattern.count('C')} cooperations, {opponent_pattern.count('D')} defections)")
    print("Switch to T-Spiteful occurs at round", int(T * 0.7))
    print("Last two rounds are", T-1, "and", T)

    # Define payoff matrix (3,3; 5,0; 0,5; 1,1)
    # Format: (my_score, opponent_score)
    payoff_matrix = {
        ("C", "C"): (3, 3),  # Both cooperate
        ("D", "C"): (5, 0),  # I defect, opponent cooperates
        ("C", "D"): (0, 5),  # I cooperate, opponent defects
        ("D", "D"): (1, 1)   # Both defect
    }

    # Initialize scores
    my_score = 0
    opponent_score = 0

    print("\nRound | My Action | State | Opponent's Action | My Score | Opponent Score | Total My Score | Total Opponent Score")
    print("-" * 110)

    # Track state changes
    state_changes = []

    for round in range(1, T + 1):
        partner_action[round] = opponent_pattern[round-1]

        # Record the state before the action
        prev_state = state

        action, state = get_action(my_action, partner_action, state, T, round)
        my_action[round] = action

        # Track state changes
        if state != prev_state:
            state_changes.append((round, prev_state, state))

        # Calculate scores for this round
        round_scores = payoff_matrix[(action, partner_action[round])]
        my_round_score = round_scores[0]
        opponent_round_score = round_scores[1]

        # Update total scores
        my_score += my_round_score
        opponent_score += opponent_round_score

        # Print all rounds
        print(f"{round:5d} | {action:9s} | {state:5s} | {partner_action[round]:17s} | {my_round_score:8d} | {opponent_round_score:14d} | {my_score:14d} | {opponent_score:20d}")

    # Print state changes
    print("\nState Changes:")
    for round, old_state, new_state in state_changes:
        print(f"Round {round}: {old_state} -> {new_state}")

    # Calculate statistics
    my_coop_count = my_action[1:].count('C')
    my_defect_count = my_action[1:].count('D')
    my_coop_rate = my_coop_count / T

    # Print a summary of the game
    print("\nSummary:")
    print(f"My cooperations: {my_coop_count} ({my_coop_rate:.2f})")
    print(f"My defections: {my_defect_count} ({my_defect_count/T:.2f})")
    print(f"Final scores (using 3,3; 5,0; 0,5; 1,1 payoff matrix):")
    print(f"My total score: {my_score}")
    print(f"Opponent total score: {opponent_score}")

    # Calculate phase statistics
    switch_round = int(T * 0.7)
    gradual_phase = my_action[1:switch_round+1]
    spiteful_phase = my_action[switch_round+1:]

    print("\nPhase Analysis:")
    print(f"Gradual phase (rounds 1-{switch_round}):")
    print(f"  Cooperations: {gradual_phase.count('C')} ({gradual_phase.count('C')/len(gradual_phase):.2f})")
    print(f"  Defections: {gradual_phase.count('D')} ({gradual_phase.count('D')/len(gradual_phase):.2f})")

    print(f"T-Spiteful phase (rounds {switch_round+1}-{T}):")
    print(f"  Cooperations: {spiteful_phase.count('C')} ({spiteful_phase.count('C')/len(spiteful_phase):.2f})")
    print(f"  Defections: {spiteful_phase.count('D')} ({spiteful_phase.count('D')/len(spiteful_phase):.2f})")

if __name__ == "__main__":
    sim_game()
