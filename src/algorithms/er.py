"""ER algorithm implementation."""

import random

from src.algorithms.graph_generation import GraphGeneration
from src.models.graph import Graph
from src.models.vertex import Vertex
from src.utils import decode_edge_no_self_loops

def decode_edge_index(index: int, n: int) -> tuple[int, int]:
    """Decode an edge index into a pair of vertex labels."""
    return index // n, index % n

class ER(GraphGeneration):
    """A class to represent the ER algorithm."""

    def generate(self, n: int, e: int, p: float) -> Graph:
        """Generate random graph using ER model."""
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        for i in range(e):
            if random.random() < p:
                v_i, v_j = decode_edge_no_self_loops(i, n)
                graph.add_edge(v_i, v_j)
        graph.remove_edge(v_i, v_j)
        return graph
