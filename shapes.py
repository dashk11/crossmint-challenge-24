"""
Astral object classes used in phase 2.
"""

from contants import BASE_API, CANDIDATE_ID, POLYANETS, COMETHS, SOLOONS


class Shape:
    """
    Base class for all astral objects
    """

    def __init__(self, row=None, column=None):
        """
        Initialize class attributes
        :param row:    int, "y" coordinate for the Crossmint logo
        :param column: int, "x" coordinate for the Crossmint logo
        """
        self.endpoint = BASE_API
        self.data = {"candidateId": CANDIDATE_ID, "row": row, "column": column}


class Polyanets(Shape):
    """
    Class to store Polyanet instances
    """

    def __init__(self, **kwargs):
        """
        Define Polyanets attributes
        :param kwargs:    int, optional keyword arguments as specified for
                          the parent class: row, column
        """
        super().__init__(**kwargs)
        self.endpoint += POLYANETS


class Cometh(Shape):
    """
    Class to store Cometh instances
    """

    def __init__(self, variant="", **kwargs):
        """
        Define Cometh attributes
        :param variant:   str, Cometh variant including its direction as
                          a prefix, e.g., "UP_COMETH"
        :param kwargs:    int, optional keyword arguments as specified for
                          the parent class: row, column
        """
        super().__init__(**kwargs)
        self.endpoint += COMETHS

        # Extract the direction from the variant and make it lowercase
        self.data["direction"] = variant.split("_")[0].lower()


class Soloons(Shape):
    """
    Class to store Soloon instances
    """

    def __init__(self, variant, **kwargs):
        """
        Define Soloons attributes
        :param variant:   str, Soloon variant including its color as a prefix
                          e.g., "PURPLE_SOLOON"
        :param kwargs:    int, optional keyword arguments as specified for
                          the parent class: row, column
        """
        super().__init__(**kwargs)
        self.endpoint += SOLOONS

        # Extract the color from the variant and make it lowercase
        self.data["color"] = variant.split("_")[0].lower()
