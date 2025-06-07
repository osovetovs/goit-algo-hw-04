"""Insertion sort algorithm."""

from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sort a list using insertion sort.

    :param arr: List of integers.
    :return: Sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr