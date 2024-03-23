"""ZER algorithm implementation."""

import math
import random

from src.algorithms.graph_generation import GraphGeneration
from src.models.graph import Graph
from src.models.vertex import Vertex

from src.utils import decode_edge_no_self_loops

def decode_edge_index(index: int, n: int) -> tuple[int, int]:
    """Decode an edge index into a pair of vertex labels."""
    return index // n, index % n

class ZER(GraphGeneration):
    """A class to represent the ZER model."""

    def generate(self, n: int, e: int, p: float) -> Graph:
        """Generate a random graph using the ZER model with a fixed number of edges."""
        i = -1
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        while i < e:
            r = random.random()
            k = int(max(math.log(r, 1 - p) - 1, 0))
            i = i + k + 1
            v_i, v_j = decode_edge_no_self_loops(i, n)
            graph.add_edge(v_i, v_j)
        graph.remove_edge(v_i, v_j)
        return graph
