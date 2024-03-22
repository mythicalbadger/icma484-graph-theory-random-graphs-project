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

    @classmethod
    def generate_ER_graph(cls, n: int, E: int, p: float)-> Graph:
        """Generate random graph using ER model"""
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        for i in range(E):
            r1 = random.randint(0, n-1)
            r2 = random.randint(0, n-1)
            while graph.has_edge(r1, r2) or r1 == r2:
                r1 = random.randint(0, n-1)
                r2 = random.randint(0, n-1)
            if random.random() < p:
                graph.add_edge(r1, r2)
        return graph
