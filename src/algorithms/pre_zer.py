"""PreZER algorithm implementation."""

import math
import random

from src.algorithms.graph_generation import GraphGeneration
from src.models.graph import Graph
from src.models.vertex import Vertex
from src.utils import decode_edge_no_self_loops


def cumulative_probability(k: int, p: float) -> float:
    """Calculate cumulative probability of edges being skipped (0-k)."""
    return 1 - (1 - p) ** (k + 1)


def log(x: float, base: float) -> float:
    """Calculate logarithm of a number `x` with base `base`."""
    return math.log(x) / math.log(base)


def decode_edge_index(index: int, n: int) -> tuple[int, int]:
    """Decode an edge index into a pair of vertex labels."""
    return index // n, index % n


class PreZER(GraphGeneration):
    """A class to represent the PreZER algorithm."""

    def generate(self, n: int, e: int, p: float) -> Graph:
        """Generate a random graph using the PreZER model."""
        m = 15
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)

        cumulative_skip_probabilities = [
            cumulative_probability(k, p) for k in range(m + 1)
        ]

        edge_count = -1
        skip_value = -1

        vertex_i, vertex_j = -1, -1

        while edge_count < e:
            alpha = random.random()
            idx = 0

            while idx <= m:
                if alpha < cumulative_skip_probabilities[idx]:
                    skip_value = idx
                    break
                idx += 1

            if idx == m + 1:
                skip_value = math.ceil(log(1 - alpha, 1 - p)) - 1
            edge_count = edge_count + skip_value + 1
            vertex_i, vertex_j = decode_edge_no_self_loops(edge_count, n)

            graph.add_edge(vertex_i, vertex_j)

        graph.remove_edge(vertex_i, vertex_j)
        return graph
