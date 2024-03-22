"""Module containing the Vertex class, which represents a node in a graph."""

from typing import Set


class Vertex:
    """A class to represent a vertex in a graph."""

    def __init__(self, label: int) -> None:
        """Initialize a vertex with a label and an empty set of neighbors."""
        self.label = label
        self.neighbors: Set[Vertex] = set()

    def add_edge(self, other: "Vertex") -> None:
        """Add an edge between this vertex and another vertex."""
        self.neighbors.add(other)

    def remove_edge(self, other: "Vertex") -> None:
        """Remove the edge between this vertex and another vertex."""
        self.neighbors.remove(other)

    def degree(self) -> int:
        """Return the degree of this vertex."""
        return len(self.neighbors)

    def has_edge(self, other: "Vertex")->bool:
        if self.neighbors.__contains__(other):
            return True
        return False

    def __str__(self) -> str:
        """Return the label of this vertex as a string."""
        return f"Node({self.label})"

    def __repr__(self) -> str:
        """Return the label of this vertex as a string."""
        return f"Node({self.label})"

    def __hash__(self) -> int:
        """Return the hash of this vertex."""
        return hash(self.label)
