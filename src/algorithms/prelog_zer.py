"""PreLogZER algorithm implementation."""

import math
import random

from src.algorithms.graph_generation import GraphGeneration
from src.models.graph import Graph
from src.models.vertex import Vertex
from src.utils import decode_edge_no_self_loops


def decode_edge_index(index: int, n: int) -> tuple[int, int]:
    """Decode an edge index into a pair of vertex labels."""
    return index // n, index % n


class PreLogZER(GraphGeneration):
    """A class to represent the PreLogZER model."""

    def generate(self, n: int, e: int, p: float) -> Graph:
        """Generate a random graph using the PreLogZER model."""
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        c = math.log(1 - p)
        rand_max = 2**16  # 16-bit random number
        log = list()
        for i in range(1, rand_max + 1):
            log.append(math.log(i / rand_max))
        i = -1
        while i < e:
            phi = random.getrandbits(16)
            k = int(max(math.ceil(log[phi] / c), 0))
            i = i + k + 1
            v_i, v_j = decode_edge_no_self_loops(i, n)
            graph.add_edge(v_i, v_j)
            i = i + k + 1
        graph.remove_edge(v_i, v_j)
        return graph
