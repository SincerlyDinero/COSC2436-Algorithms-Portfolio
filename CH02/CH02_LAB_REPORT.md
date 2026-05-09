# Chapter 2: Selection Sort — Lab Report

## Student Information
- **Name:** Nathan Higgins
- **Date:** May 2026
- **Course:** COSC 2436

## Algorithm Summary

- **How it works:**  
Selection sort repeatedly finds the smallest value in the unsorted part of the list and swaps it into the correct position. This process continues until the list becomes fully sorted.

- **Time complexity:**  
O(n²)

- **When to use it:**  
Selection sort is useful for small datasets and educational purposes when learning how sorting algorithms work.

## Test Results

| Input | Sorted Output |
|-------|----------------|
| 5, 2, 9, 1 | 1, 2, 5, 9 |
| 8, 3, 7, 4 | 3, 4, 7, 8 |

## Reflection Questions

1. **Why is selection sort inefficient for large datasets?**  
Selection sort compares every element multiple times, which causes the number of operations to grow quickly as the dataset increases.

2. **What is the main advantage of selection sort?**  
Selection sort is simple to understand and easy to implement, making it useful for educational purposes.

3. **How does selection sort differ from bubble sort?**  
Selection sort performs fewer swaps because it only swaps once per pass, while bubble sort repeatedly swaps adjacent values.

## Challenges Encountered

One challenge was correctly tracking the minimum value during each pass through the list. I resolved this by tracing the algorithm step-by-step.
