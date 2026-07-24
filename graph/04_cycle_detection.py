"""
Cycle Detection in an Undirected Graph

This program detects whether an undirected graph
contains a cycle using Depth-First Search (DFS).
"""


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

    def has_cycle(self) -> bool:
        """Return True if the graph contains a cycle."""

        visited = set()

        for vertex in self.graph:
            if vertex not in visited:
                if self._dfs(vertex, visited, None):
                    return True

        return False

    def _dfs(
        self,
        vertex: str,
        visited: set,
        parent: str | None
    ) -> bool:

        visited.add(vertex)

        for neighbor in self.graph[vertex]:

            if neighbor not in visited:

                if self._dfs(neighbor, visited, vertex):
                    return True

            elif neighbor != parent:
                return True

        return False


def main():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    graph.add_edge("C", "D")

    print("Graph contains cycle:", graph.has_cycle())


if __name__ == "__main__":
    main()
