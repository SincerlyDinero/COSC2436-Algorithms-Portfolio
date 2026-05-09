# Chapter 6: Breadth-First Search (BFS) — Lab Report

## Student Information
- **Name:** Nathan Higgins
- **Date:** May 9 2026
- **Course:** COSC 2436

## Algorithm Summary

- **How it works:**  
Breadth-first search explores nodes level by level using a queue.

- **Time complexity:**  
O(V + E)

- **When to use it:**  
BFS is useful for finding shortest paths in unweighted graphs.

## Test Results

| Starting Node | Traversal Order |
|---------------|-----------------|
| A | A, B, C, D |

## Reflection Questions

1. **Why does BFS use a queue?**  
A queue ensures nodes are explored in the correct order.

2. **What is BFS commonly used for?**  
BFS is commonly used in pathfinding and graph traversal.

3. **How is BFS different from DFS?**  
BFS explores level by level while DFS explores deeper first.

## Challenges Encountered

One challenge was managing visited nodes correctly. I resolved this by using a visited set.
