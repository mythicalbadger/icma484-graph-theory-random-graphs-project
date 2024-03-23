"""The module for the Graph class, which represents a graph of vertices."""

from typing import Dict, Set

import networkx as nx

from src.models.vertex import Vertex


class Graph:
    """A class to represent a graph of vertices."""

    order: int
    size: int

    def __init__(self, vertices: Set[Vertex]) -> None:
        """Initialize a graph with a set of vertices."""
        self.vertices: Dict[int, Vertex] = {v.label: v for v in vertices}
        self.order = len(vertices)
        self.size = 0

    def add_edge(self, v1_label: int, v2_label: int) -> None:
        """Add an edge between two vertices."""
        v1, v2 = self.vertices[v1_label], self.vertices[v2_label]
        v1.add_edge(v2)
        v2.add_edge(v1)
        self.size += 1

    def remove_edge(self, v1_label: int, v2_label: int) -> None:
        """Remove the edge between two vertices."""
        v1, v2 = self.vertices[v1_label], self.vertices[v2_label]
        v1.remove_edge(v2)
        v2.remove_edge(v1)
        self.size -= 1

    def has_edge(self, v1_label: int, v2_label: int) -> bool:
        """Check if there exist an edge between two vertices."""
        v1 = self.vertices[v1_label]
        v2 = self.vertices[v2_label]
        return v1.has_edge(v2) and v2.has_edge(v1)

    def to_networkx(self) -> nx.Graph:
        """Return a networkx graph representation of this graph."""
        g = nx.Graph()
        for v in self.vertices.values():
            g.add_node(v.label)
            for n in v.neighbors:
                g.add_edge(v.label, n.label)
        return g
