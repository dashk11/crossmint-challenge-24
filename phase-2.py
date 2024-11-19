"""
Crossmint Challenge - Phase 2 Implementation
"""

import requests
from contants import GOAL_ENDPOINT, CANDIDATE_ID
from helpers import build_quadrant, place_object


def solve_phase_2(goal_shape, quadrant, rows, cols):
    """
    Place objects based on the quadrant and symmetry.

    Args:
        goal_shape (list): Original goal shape (used for reference).
        quadrant (list): Top-left quadrant of the goal shape.
        rows (int): Number of rows in the full grid.
        cols (int): Number of columns in the full grid.
    """
    for i, row in enumerate(quadrant):
        for j, shape in enumerate(row):
            if shape == "SPACE":
                continue

            # Place in all symmetrical quadrants
            positions = [
                (i, j),
                (i, cols - j - 1),
                (rows - i - 1, j),
                (rows - i - 1, cols - j - 1),
            ]

            for row_idx, col_idx in positions:
                place_object(shape, row_idx, col_idx)


if __name__ == "__main__":
    # 1) Fetch the goal shape from the API
    response = requests.get(GOAL_ENDPOINT, data={"candidateId": CANDIDATE_ID})
    response.raise_for_status()
    goal_shape = response.json()["goal"]

    rows = len(goal_shape)
    cols = len(goal_shape[0])

    # 2) Extract the top-left quadrant
    quadrant = build_quadrant(goal_shape)

    # 3) Place objects using quadrant and symmetry
    solve_phase_2(goal_shape, quadrant, rows, cols)
