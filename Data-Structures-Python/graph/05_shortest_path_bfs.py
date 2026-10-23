"""
Shortest Path in an Unweighted Graph

This program finds the shortest path between
two vertices in an unweighted graph using
Breadth-First Search (BFS).
"""

from collections import deque


class Graph:
    """Represents an undirected graph."""

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex: str) -> None:
        """Add a vertex if it does not exist."""

        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1: str, vertex2: str) -> None:
        """Add an undirected edge."""

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def shortest_path(self, start: str, end: str) -> list[str] | None:
        """Return the shortest path between two vertices."""

        if start not in self.graph or end not in self.graph:
            return None

        visited = {start}
        queue = deque([(start, [start])])

        while queue:

            current, path = queue.popleft()

            if current == end:
                return path

            for neighbor in self.graph[current]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None


def main():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")
    graph.add_edge("E", "F")

    start = "A"
    end = "F"

    path = graph.shortest_path(start, end)

    if path:
        print(f"Shortest path from {start} to {end}:")
        print(" -> ".join(path))
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
