#
# ==============================================================
# ==============================================================
# ================
# Dijkstra's Shortest Path - Interactive CLI
#
# This program lets the user build an undirected weighted graph by entering
# nodes and edges, displays the graph as ASCII art, then finds and highlights
# the shortest path between two chosen nodes using Dijkstra's algorithm.
#
# Flow:
#   1. User enters node names
#   2. User enters edge weights for each pair of nodes
#   3. Graph is displayed
#   4. User picks a source and destination node
#   5. Dijkstra's algorithm finds the shortest path
#   6. Graph is re-displayed with the shortest path highlighted
#
# ==============================================================
# ==============================================================
# ================

import heapq


def get_nodes():
    """
    Prompt the user to enter node names one at a time.

    Nodes are the vertices of the graph - e.g. cities,
    routers, or any named location. The user types each
    name and presses Enter, then types 'done' when finished.

    Returns:
        list: A list of node name strings entered by the user.
    """
    nodes = []
    print("Enter node names one at a time. Type 'done' when finished.")
    while True:
        node = input("Node name: ").strip()
        if node.lower() == 'done':
            break
        if node and node not in nodes:
            nodes.append(node)
    return nodes


def get_edges(nodes):
    """
    Prompt the user to enter edge weights between node pairs.

    For every unique pair of nodes, the user is asked to supply
    a numeric weight (distance / cost). Entering nothing or a
    non-positive number means no edge exists between that pair.

    Args:
        nodes (list): The list of node names from get_nodes().

    Returns:
        dict: Adjacency dict  {node: {neighbor: weight, ...}, ...}
    """
    graph = {node: {} for node in nodes}
    print("\nEnter edge weights (press Enter to skip / no edge):")
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            val = input(f"  Weight between '{u}' and '{v}': ").strip()
            try:
                w = float(val)
                if w > 0:
                    graph[u][v] = w
                    graph[v][u] = w
            except ValueError:
                pass  # no edge
    return graph


def display_graph(graph, path=None):
    """
    Print a simple ASCII representation of the graph.

    Each edge is shown as  NodeA --weight-- NodeB.
    If a *path* list is provided the edges that belong to
    that path are marked with  *** ... ***  so they stand
    out visually.

    Args:
        graph (dict): Adjacency dict returned by get_edges().
        path  (list): Optional ordered list of nodes forming
                      the shortest path to highlight.
    """
    path_edges = set()
    if path:
        for k in range(len(path) - 1):
            a, b = path[k], path[k + 1]
            path_edges.add((a, b))
            path_edges.add((b, a))

    printed = set()
    print("\n--- Graph ---")
    for u in graph:
        for v, w in graph[u].items():
            edge = tuple(sorted([u, v]))
            if edge not in printed:
                printed.add(edge)
                if (u, v) in path_edges:
                    print(f"  *** {u} --{w}-- {v} ***")
                else:
                    print(f"  {u} --{w}-- {v}")
    print("-------------")


def dijkstra(graph, start, end):
    """
    Find the shortest path between *start* and *end* in *graph*
    using Dijkstra's algorithm.

    The function uses a min-heap (priority queue) to always
    expand the cheapest unvisited node next.  A *parents* dict
    records how each node was reached so the full path can be
    reconstructed once the destination is found.

    Args:
        graph (dict): Adjacency dict  {node: {neighbor: weight}}
        start (str) : Source node name.
        end   (str) : Destination node name.

    Returns:
        tuple: (path, total_cost)
            path       - ordered list of node names from start to end,
                         or an empty list if no path exists.
            total_cost - numeric sum of edge weights along the path,
                         or float('inf') if unreachable.
    """
    # distances[node] = best known cost to reach node from start
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # parents[node] = the node we came from on the cheapest path
    parents = {node: None for node in graph}

    # Min-heap entries: (cost, node)
    heap = [(0, start)]
    visited = set()

    while heap:
        current_cost, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)

        # Early exit once we reach the destination
        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parents[neighbor] = current_node
                heapq.heappush(heap, (new_cost, neighbor))

    # Reconstruct path by walking back through parents
    if distances[end] == float('inf'):
        return [], float('inf')   # disconnected

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parents[node]
    path.reverse()

    return path, distances[end]


def main():
    print("=== Dijkstra's Shortest Path - Interactive CLI ===")

    nodes = get_nodes()
    if len(nodes) < 2:
        print("Need at least 2 nodes. Exiting.")
        return

    graph = get_edges(nodes)
    display_graph(graph)

    print("\nEnter source and destination nodes to find the shortest path.")
    src = input("Source node: ").strip()
    dst = input("Destination node: ").strip()

    if src not in graph or dst not in graph:
        print("One or both nodes not found in the graph.")
        return

    path, cost = dijkstra(graph, src, dst)

    if not path:
        print(f"\nNo path exists between '{src}' and '{dst}'.")
    else:
        print(f"\nShortest path: {' -> '.join(path)}")
        print(f"Total cost   : {cost}")
        display_graph(graph, path)


if __name__ == "__main__":
    main()
