# Chapter 9: Dijkstra's Algorithm — Lab Report

## Student Information
- **Name:** Nathan Higgins
- **Date:** May 2026
- **Course:** COSC 2436

## Algorithm Summary

- **How it works:**  
Dijkstra’s algorithm finds the shortest path between nodes in a weighted graph.

- **Time complexity:**  
O(V²) or O((V + E) log V)

- **When to use it:**  
Dijkstra’s algorithm is useful for GPS navigation and shortest-path problems.

## Test Results

| Start | Destination | Distance |
|-------|--------------|----------|
| A | D | 7 |

## Reflection Questions

1. **Why is Dijkstra’s algorithm useful?**  
It efficiently finds the shortest path between locations.

2. **Why can’t Dijkstra’s algorithm use negative weights?**  
Negative weights can produce incorrect shortest paths.

3. **What real-world systems use Dijkstra’s algorithm?**  
GPS navigation systems and computer networks commonly use it.

## Challenges Encountered

One challenge was tracking node distances correctly during updates. I resolved this by carefully tracing the algorithm.
