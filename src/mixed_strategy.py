"""
Mixed Strategy Model for Iterative Prisoner's Dilemma

This module implements a mixed strategy that combines:
1. Gradual strategy: Cooperates unless opponent defects, then punishes with defections
   equal to the cumulative defections by the opponent
2. T-Spiteful strategy: Plays tit-for-tat unless betrayed twice consecutively, then always defects

The strategy switches from Gradual to T-Spiteful at 70% of the game,
and always defects in the last two rounds.
"""

def gradual_strategy(my_action, partner_action, round):
    """
    Implements the Gradual strategy.

    Cooperates by default, but if the opponent defects, it punishes with a number of
    defections equal to the cumulative defections by the opponent up to that point.

    Args:
        my_action: List of my actions in previous rounds
        partner_action: List of partner's actions in previous rounds
        round: Current round number (1-indexed)

    Returns:
        "C" for cooperate or "D" for defect
    """
    # If this is the first round, cooperate
    if round == 1:
        return "C"

    # Check if opponent defected in the previous round
    if partner_action[round-1] == "D":
        # Count total defections by opponent up to this point
        total_defections = partner_action[:round].count("D")

        # We need to start a punishment cycle of length equal to total_defections
        # First defection in the punishment cycle
        return "D"

    # If opponent didn't defect in the previous round, check if we're in a punishment cycle

    # Find the most recent defection by the opponent
    last_defection = -1
    for r in range(round-1, 0, -1):
        if partner_action[r] == "D":
            last_defection = r
            break

    # If opponent has never defected, cooperate
    if last_defection == -1:
        return "C"

    # Count total defections by opponent up to the last defection
    total_defections = partner_action[:last_defection+1].count("D")

    # Count how many rounds we've defected since the last defection by opponent
    punishment_so_far = 0
    for r in range(last_defection+1, round):
        if my_action[r] == "D":
            punishment_so_far += 1

    # If we haven't completed the punishment cycle, continue defecting
    if punishment_so_far < total_defections:
        return "D"

    # Otherwise, we've completed the punishment cycle, so cooperate
    return "C"

def t_spiteful_strategy(partner_action, round, state):
    """
    Implements the T-Spiteful strategy.

    Plays tit-for-tat unless betrayed twice consecutively, then always defects.
    The state ("Happy"/"Angry") tracks whether we've seen two consecutive defections.

    Args:
        partner_action: List of partner's actions in previous rounds
        round: Current round number (1-indexed)
        state: Current state, "Happy" (tit-for-tat) or "Angry" (always defect)

    Returns:
        Tuple of (action, new_state) where:
        - action is "C" for cooperate or "D" for defect
        - new_state is the updated state ("Happy" or "Angry")
    """
     # Check if we're already in "Angry" state (permanent defection)
    if state == "Angry":
        return "D", "Angry"

    # Check for two consecutive defections by opponent
    if partner_action[round-2] == "D" and partner_action[round-1] == "D":
        return "D", "Angry"  # Switch to permanent defection

    # Otherwise, play tit-for-tat (copy opponent's last move)
    return partner_action[round-1], "Happy"

def mixed_strategy(my_action, partner_action, state, T, round):
    """
    Implements the mixed strategy model.

    Uses Gradual strategy until 70% of the game, then switches to T-Spiteful.
    Always defects in the last two rounds.

    Args:
        my_action: List of your actions in previous rounds
        partner_action: List of partner's actions in previous rounds
        state: Current state, "Happy" (tit-for-tat) or "Angry" (always defect) for T-Spiteful
        T: Total number of rounds in the game
        round: Current round number (1-indexed)

    Returns:
        Tuple of (action, new_state) where:
        - action is "C" for cooperate or "D" for defect
        - new_state is the updated state ("Happy" or "Angry")
    """
    # Always defect in the last two rounds - business school!
    if round >= T - 1:
        return "D", "Angry"

    # Determine if we should switch to T-Spiteful (at 70% of the game)
    switch_round = int(T * 0.7)

    # Before the switch point, use Gradual strategy
    if round < switch_round:
        action = gradual_strategy(my_action, partner_action, round)
        return action, state  # Keep the current state unchanged

    # After the switch point, use T-Spiteful strategy
    else:
        action, new_state = t_spiteful_strategy(partner_action, round, state)
        return action, new_state

def get_action(my_action, partner_action, state, T, round):
    """
    Main function to determine the action for the current round.

    Args:
        my_action: List of your actions in previous rounds
        partner_action: List of partner's actions in previous rounds
        state: Current state, "Happy" (Gradual) or "Angry" (T-Spiteful)
        T: Total number of rounds in the game
        round: Current round number (1-indexed)

    Returns:
        Tuple of (action, new_state) where:
        - action is "C" for cooperate or "D" for defect
        - new_state is the updated state ("Happy" or "Angry")
    """
    return mixed_strategy(my_action, partner_action, state, T, round)
