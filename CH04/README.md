# Lab 04: Quicksort

## Student Information
- **Name:** YOUR REAL NAME HERE
- **Date:** March 20, 2025

## Quicksort Concepts

### Divide and Conquer
Quicksort uses a divide-and-conquer strategy by breaking a list into smaller sublists. It selects a pivot element, partitions the remaining elements into smaller and larger groups, recursively sorts those groups, and then combines them into a final sorted list.

### The Three Steps
1. **Choose pivot:** Select the first element of the array as the pivot.
2. **Partition:** Separate the remaining elements into two lists: elements less than or equal to the pivot and elements greater than the pivot.
3. **Recurse and combine:** Recursively sort both partitions and combine them with the pivot in the middle.

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])

Pivot = 3  
Less = [2, 1]  
Greater = [5, 4]  

quicksort([2, 1])  
Pivot = 2  
Less = [1]  
Greater = []  

Result = [1] + [2] + [] = [1, 2]

quicksort([5, 4])  
Pivot = 5  
Less = [4]  
Greater = []  

Result = [4] + [5] + [] = [4, 5]

Final result = [1, 2] + [3] + [4, 5]  
= [1, 2, 3, 4, 5]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | The pivot splits the array evenly each time. |
| Average | O(n log n) | Random pivot positions typically divide the list fairly evenly. |
| Worst | O(n²) | The pivot is always the smallest or largest element, creating very unbalanced partitions. |

## Reflection Questions

1. If the array is already sorted and the first element is chosen as pivot, quicksort will repeatedly create very unbalanced partitions, resulting in O(n²) time complexity.

2. Pivot selection can be improved by choosing a random pivot or using a median-of-three strategy to avoid consistently poor splits.

3. Quicksort is generally much faster than bubble sort and often performs similarly to merge sort, though merge sort guarantees O(n log n) performance in all cases.

4. We use `array[1:]` so the pivot is not included in the partition lists, preventing duplication of the pivot element.
