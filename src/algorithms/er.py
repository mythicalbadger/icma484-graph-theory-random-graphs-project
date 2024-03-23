"""ER algorithm implementation."""

import random

from src.algorithms.graph_generation import GraphGeneration
from src.models.graph import Graph
from src.models.vertex import Vertex
from src.utils import calculate_n_c, decode_edge_no_self_loops


class ER(GraphGeneration):
    """A class to represent the ER algorithm."""

    def generate(self, n: int, e: int, p: float) -> Graph:
        """Generate random graph using ER model."""
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        for i in range(e):
            r1 = random.randint(0, n - 1)
            r2 = random.randint(0, n - 1)
            while graph.has_edge(r1, r2) or r1 == r2:
                r1 = random.randint(0, n - 1)
                r2 = random.randint(0, n - 1)
            if random.random() < p:
                graph.add_edge(r1, r2)
        return graph

    def generate_fixed_edge(self, n: int, e: int, p: float) -> Graph:
        """Generate a random graph using the ER model with a fixed number of edges."""
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        n_c = calculate_n_c(n)

        while graph.size < n_c:
            for i in range(e):
                theta = random.random()
                if theta < p:
                    vertex_i, vertex_j = decode_edge_no_self_loops(i, n)
                    graph.add_edge(vertex_i, vertex_j)

        return graph
