"""
Lab 6: Breadth-First Search Implementation
Finds shortest path (by number of edges) in unweighted graph.
"""
from typing import List, Dict, Optional
from collections import deque
from graph import Graph


def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    """
    # 1. Check if start or end not in graph
    if start not in graph.vertices or end not in graph.vertices:
        return None

    # 2. Initialize queue with (vertex, path)
    queue = deque([(start, [start])])

    # 3. Visited set
    visited = {start}

    # For printing BFS levels (to match expected output)
    level = 0
    print(f"\nBFS from '{start}' to '{end}':")
    print("-" * 40)

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current, path = queue.popleft()
            print(f"Level {level}: Visiting '{current}'")

            # 5. If found destination
            if current == end:
                print(f"\nFound path with {len(path) - 1} edges!\n")
                return path

            # 6. Explore neighbors
            for neighbor in graph.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        level += 1

    return None


def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    if start not in graph.vertices:
        return {}

    distances = {start: 0}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    path = bfs_find_path(graph, v1, v2)
    return path is not None