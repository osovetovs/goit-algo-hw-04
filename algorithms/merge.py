"""Merge sort algorithm."""

from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort a list using merge sort.

    :param arr: List of integers.
    :return: Sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists.

    :param left: First sorted list.
    :param right: Second sorted list.
    :return: Merged sorted list.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
