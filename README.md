# Homework 4: Sorting Algorithms

## Overview

This project compares three sorting algorithms by execution time:

- Merge Sort
- Insertion Sort
- Timsort (Python's built-in `sorted()`)

### How to Run:
```bash
python main.py
```


## Conclusion
- Timsort consistently outperformed the other two algorithms in terms of execution time across all dataset sizes, demonstrating superior efficiency on both small and large data volumes.

- Merge Sort delivered solid performance on medium-sized datasets but became less optimal with larger datasets due to its O(n log n) time complexity.

- Insertion Sort was the least efficient of the three, particularly on large datasets, as its O(n²) complexity leads to significantly slower execution.
- 
## Sample Benchmark Output

| Size | Timsort (s) | Merge Sort (s) | Insertion Sort (s) |
|------|-------------|----------------|---------------------|
| 100  | 0.0003      | 0.0012         | 0.0028              |
| 1000 | 0.0021      | 0.0087         | 0.1303              |
| 5000 | 0.0136      | 0.0452         | 3.5127              |

> Timsort outperforms both Merge and Insertion Sort across all inputs. Its hybrid nature (merge + insertion) makes it ideal for practical use.

## Optional Task: `merge_k_lists`

Merges multiple sorted lists into one using `heapq.merge`.

```python
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(merge_k_lists(lists))
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
