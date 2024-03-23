"""PreLogZER algorithm implementation."""

import math
import random

from src.algorithms.graph_generation import GraphGeneration
from src.models.graph import Graph
from src.models.vertex import Vertex


class PreLogZER(GraphGeneration):
    """A class to represent the PreLogZER model."""

    def generate(self, n: int, e: int, p: float) -> Graph:
        """Generate a random graph using the PreLogZER model."""
        edges = list()
        for i in range(n):
            for j in range(n):
                if i != j:
                    edges.append((i, j))
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        c = math.log(1 - p)
        mx = 2 ^ 32
        log = list()
        for i in range(1, mx + 1):
            log.append(math.log(i / mx))
        i = -1
        while i < e:
            phi = random.randrange(0, mx)
            k = int(max(math.ceil(log[phi] / c), 0))
            edge = random.choice(edges)
            if graph.has_edge(edge[0], edge[1]):
                i = i - k - 1
            graph.add_edge(edge[0], edge[1])
            i = i + k + 1
        return graph
