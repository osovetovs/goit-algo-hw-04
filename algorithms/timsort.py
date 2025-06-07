"""Timsort using Python's built-in sorted()."""

from typing import List

def timsort(arr: List[int]) -> List[int]:
    """
    Sort a list using Python's built-in Timsort algorithm.

    :param arr: List of integers.
    :return: Sorted list.
    """
    return sorted(arr)
