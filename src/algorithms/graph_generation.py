"""Module with graph generation algorithms."""

import random

from src.models.graph import Graph
from src.models.vertex import Vertex


class GraphGeneration:
    """A class to generate random graphs."""

    @classmethod
    def generate_erdos_renyi_graph(cls, n: int, p: float) -> Graph:
        """Generate a random graph using the Erdos-Renyi model."""
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    graph.add_edge(i, j)
        return graph
