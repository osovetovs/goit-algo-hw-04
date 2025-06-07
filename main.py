"""Main file to run benchmarks."""

from benchmarks.run_benchmark import benchmark_algorithms
from optional_task.merge_k import merge_k_lists

if __name__ == "__main__":
    dataset_sizes = [100, 1000, 5000]
    benchmark_algorithms(dataset_sizes)

    # Optional Task
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(lists)
    print("\nMerged list:", merged)
