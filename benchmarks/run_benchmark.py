"""Benchmark runner for sorting algorithms."""

import timeit
from algorithms.merge import merge_sort
from algorithms.insertion import insertion_sort
from algorithms.timsort import timsort
from utils.datasets import generate_data

def benchmark_algorithms(sizes: list[int]) -> None:
    """
    Benchmark sorting algorithms using random datasets.

    :param sizes: List of dataset sizes to test.
    """
    algorithms = {
        "Timsort (built-in)": timsort,
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
    }

    for size in sizes:
        data = generate_data(size)
        print(f"\n--- Dataset size: {size} ---")
        for name, func in algorithms.items():
            time = timeit.timeit(lambda: func(data.copy()), number=5)
            print(f"{name}: {time:.4f} seconds")
