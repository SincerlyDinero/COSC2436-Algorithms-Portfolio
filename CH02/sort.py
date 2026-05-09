"""
Lab 2: Sorting Algorithms
Implements selection sort with performance tracking.
"""
from typing import List, Dict, Callable


def find_smallest_index(arr: List[Dict], key: Callable, start: int) -> int:
    """
    Find index of smallest element from start position.
    
    Args:
        arr: List to search
        key: Function to extract comparison value
        start: Starting index
    
    Returns:
        Index of smallest element
    """
    # TODO: Implement find_smallest_index
    # 1. Initialize smallest_idx to start
    # 2. Get smallest_val using key(arr[start])
    # 3. Loop from start+1 to end of array
    # 4. If key(arr[i]) < smallest_val, update smallest_val and smallest_idx
    # 5. Return smallest_idx
    
    pass  # Remove this and add your code


def selection_sort(arr: List[Dict], key: Callable = lambda x: x, reverse: bool = False) -> List[Dict]:
    """
    Sort list using selection sort algorithm.
    Time Complexity: O(n²)
    Space Complexity: O(n) - creates copy
    
    Args:
        arr: List to sort
        key: Function to extract comparison value
        reverse: If True, sort descending
    
    Returns:
        Sorted list (does not modify original)
    """
    # TODO: Implement selection_sort
    # 1. Get n = len(arr)
    # 2. Initialize comparisons = 0, swaps = 0
    # 3. Create result = arr.copy() to avoid modifying original
    # 4. Loop i from 0 to n-1:
    #    a. If reverse, find largest element from i to end
    #    b. Else find smallest element from i to end
    #    c. Swap result[i] with result[extreme_idx] if needed
    # 5. Print comparison and swap counts
    # 6. Return result
    
    pass  # Remove this and add your code


def python_builtin_sort(arr: List[Dict], key: Callable, reverse: bool = False) -> List[Dict]:
    """
    Python's built-in sort for comparison.
    Time Complexity: O(n log n) - Timsort algorithm
    """
    # TODO: Implement python_builtin_sort
    # 1. Create result = arr.copy()
    # 2. Call result.sort(key=key, reverse=reverse)
    # 3. Print "Python Built-in Sort: O(n log n) - Timsort"
    # 4. Return result
    
    pass  # Remove this and add your code
