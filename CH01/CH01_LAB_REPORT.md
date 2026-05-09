# Chapter 1: Binary Search vs Linear Search — Lab Report

## Student Information
- **Name:** Nathan Higgins
- **Date:** May 9 2026
- **Course:** COSC 2436

## Algorithm Summary

- **How it works:**  
Linear search checks each item one at a time until the target value is found or the list ends. Binary search works on sorted data by checking the middle value, then eliminating either the left half or right half of the list.

- **Time complexity:**  
Linear Search: O(n)  
Binary Search: O(log n)

- **When to use it:**  
Linear search is useful for small or unsorted datasets. Binary search is best for large sorted lists where fast searching is needed.

## Test Results

| Input Size | Linear Search Comparisons | Binary Search Comparisons |
|------------|---------------------------|---------------------------|
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1000 | 1000 | 10 |

## Reflection Questions

1. **Why is binary search faster than linear search?**  
Binary search removes half of the remaining data during each step, making it much more efficient than checking every item individually.

2. **Why does binary search require sorted data?**  
The algorithm needs sorted data so it knows whether to move left or right after checking the middle value.

3. **What are practical uses of binary search?**  
Binary search is commonly used in databases, search engines, and applications requiring fast lookup operations.

## Challenges Encountered

One challenge was understanding how the midpoint changed during each iteration. I resolved this by tracing the algorithm manually with smaller datasets.
