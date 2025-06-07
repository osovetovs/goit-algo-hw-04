"""Optional task: merge k sorted lists."""

from heapq import merge
from typing import List

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Merge k sorted lists into a single sorted list.

    :param lists: List of k sorted integer lists.
    :return: One merged sorted list.
    """
    result = []
    for lst in lists:
        result = list(merge(result, lst))
    return result
