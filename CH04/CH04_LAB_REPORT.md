# Chapter 4: Quicksort — Lab Report

## Student Information
- **Name:** Nathan Higgins
- **Date:** May 9 2026
- **Course:** COSC 2436

## Algorithm Summary

- **How it works:**  
Quicksort selects a pivot value and divides the list into smaller and larger values around the pivot. The process repeats recursively until the list is sorted.

- **Time complexity:**  
Average Case: O(n log n)  
Worst Case: O(n²)

- **When to use it:**  
Quicksort is useful for efficiently sorting large datasets.

## Test Results

| Input | Sorted Output |
|-------|----------------|
| 9, 4, 2, 7 | 2, 4, 7, 9 |
| 8, 1, 6, 3 | 1, 3, 6, 8 |

## Reflection Questions

1. **Why is Quicksort considered efficient?**  
Quicksort divides problems into smaller pieces and sorts them recursively, making it fast on average.

2. **What role does the pivot play?**  
The pivot separates values into smaller and larger groups during sorting.

3. **What happens in the worst-case scenario?**  
The algorithm becomes less efficient when poor pivot choices create uneven partitions.

## Challenges Encountered

One challenge was understanding how partitioning worked during recursion. I solved this by drawing diagrams of the sorting process.
