"""
Graph Traversal - Breadth-First Search (BFS)

This program demonstrates Breadth-First Search (BFS)
traversal of an undirected graph using a queue.
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
        """Add an undirected edge between two vertices."""

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def bfs(self, start: str) -> None:
        """Perform Breadth-First Search traversal."""

        if start not in self.graph:
            print(f"Vertex '{start}' does not exist.")
            return

        visited = set([start])
        queue = deque([start])

        print("BFS Traversal:")

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()


def main():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")

    graph.bfs("A")


if __name__ == "__main__":
    main()
