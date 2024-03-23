"""ZER algorithm implementation."""

import math
import random

from src.algorithms.graph_generation import GraphGeneration
from src.models.graph import Graph
from src.models.vertex import Vertex


class ZER(GraphGeneration):
    """A class to represent the ZER model."""

    def generate(self, n: int, e: int, p: float) -> Graph:
        """Generate a random graph using the ZER model with a fixed number of edges."""
        edges = list()
        for i in range(n):
            for j in range(n):
                if i != j:
                    edges.append((i, j))
        i = -1
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        while i < e:
            r = random.random()
            k = int(max(math.log(r, 1 - p) - 1, 0))
            edge = random.choice(edges)
            if graph.has_edge(edge[0], edge[1]):
                i = i - k - 1
            graph.add_edge(edge[0], edge[1])
            i = i + k + 1
        return graph

    def generate_fixed_edge(self, n: int, e: int, p: float) -> Graph:
        """Generate a random graph with a fixed number of edges."""
        raise NotImplementedError
