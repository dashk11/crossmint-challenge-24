"""
Helper functions for phase 1 and phase 2.
"""

import requests
from shapes import Polyanets, Cometh, Soloons
from contants import CANDIDATE_ID, BASE_API, GOAL_ENDPOINT


def fetch_goal_shape():
    """
    Fetch the goal shape for the Crossmint challenge.

    Returns:
        list: A 2D list representing the goal shape.

    Raises:
        Exception: If the request fails or response data is invalid.
    """
    response = requests.get(BASE_API + GOAL_ENDPOINT, data={"candidateId": CANDIDATE_ID})
    if response.status_code != 200:
        raise Exception(f"Failed to fetch goal shape: {response.status_code}")
    return response.json()["goal"]


def create_entity(shape, row, column):
    """
    Create and place the appropriate astral object.

    Args:
        shape (str): Name of the object (e.g., "POLYANET", "UP_COMETH").
        row (int): Row index for placement.
        column (int): Column index for placement.

    Raises:
        Exception: If the POST request fails.
    """
    astral_object = None

    if shape == "POLYANET":
        astral_object = Polyanets(row=row, column=column)
    elif "COMETH" in shape:
        astral_object = Cometh(shape, row=row, column=column)
    elif "SOLOON" in shape:
        astral_object = Soloons(shape, row=row, column=column)

    if astral_object:
        response = requests.post(astral_object.endpoint, data=astral_object.data)
        if response.status_code != 200:
            raise Exception(f"Failed to create entity at ({row}, {column}): {response.status_code}")


def build_quadrant(goal_shape):
    """
    Extract the top-left quadrant from the goal shape.

    Args:
        goal_shape (list): 2D list of the entire goal shape.

    Returns:
        list: 2D list of the top-left quadrant.
    """
    rows = len(goal_shape)
    cols = len(goal_shape[0])
    quadrant = []

    for i in range(rows // 2):
        quadrant.append(goal_shape[i][:cols // 2])

    return quadrant


def place_object(shape, row, column):
    """
    Create and place the appropriate astral object.

    Args:
        shape (str): Name of the object (e.g., "POLYANET", "UP_COMETH").
        row (int): Row index for placement.
        column (int): Column index for placement.
    """
    astral_object = None

    if shape == "POLYANET":
        astral_object = Polyanets(row=row, column=column)
    elif "COMETH" in shape:
        astral_object = Cometh(shape, row=row, column=column)
    elif "SOLOON" in shape:
        astral_object = Soloons(shape, row=row, column=column)

    if astral_object:
        response = requests.post(astral_object.endpoint, data=astral_object.data)
        response.raise_for_status()

