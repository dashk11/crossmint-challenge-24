"""
Crossmint Challenge - Phase 1
"""

from contants import POLYANETS
from helpers import fetch_goal_shape, create_entity


def solve_phase_1():
    """
    Implement the target shape for Phase 1.
    Fetches the goal shape and creates Polyanets at specified positions.
    """
    try:
        # 1) Fetch the target goal shape
        goal_shape = fetch_goal_shape()
    except Exception as error:
        print(f"Error fetching goal shape: {error}")
        return

    # 2) Place Polyanets
    for row_index, row in enumerate(goal_shape):
        for col_index, cell in enumerate(row):
            if cell == "POLYANET":
                create_entity(POLYANETS, row_index, col_index)


if __name__ == "__main__":
    solve_phase_1()
