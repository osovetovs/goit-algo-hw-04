"""Utility functions for generating test data."""

from random import randint

def generate_data(size: int) -> list[int]:
    """
    Generate a list of random integers.

    :param size: Length of the list.
    :return: List of random integers.
    """
    return [randint(0, 10000) for _ in range(size)]
