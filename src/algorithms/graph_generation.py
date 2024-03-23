"""Module with graph generation algorithms."""

import math
import random

from src.models.graph import Graph
from src.models.vertex import Vertex


class GraphGeneration:
    """A class to generate random graphs."""

    # edges = list()
    #
    # @classmethod
    # def create_edges(cls, n: int):
    #     for i in range(n):
    #         for j in range(n):
    #             if i != j:
    #                 edges.append((i, j))

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
    def generate_ER_graph(cls, n: int, E: int, p: float) -> Graph:
        """Generate random graph using ER model."""
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        for i in range(E):
            r1 = random.randint(0, n - 1)
            r2 = random.randint(0, n - 1)
            while graph.has_edge(r1, r2) or r1 == r2:
                r1 = random.randint(0, n - 1)
                r2 = random.randint(0, n - 1)
            if random.random() < p:
                graph.add_edge(r1, r2)
        return graph

    @classmethod
    def generate_ZER_graph(cls, n: int, E: int, p: float) -> Graph:
        """Generate a random graph using ZER model."""
        edges = list()
        for i in range(n):
            for j in range(n):
                if i != j:
                    edges.append((i, j))
        i = -1
        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)
        while i < E:
            r = random.random()
            k = int(max(math.log(r, 1 - p) - 1, 0))
            edge = random.choice(edges)
            if graph.has_edge(edge[0], edge[1]):
                i = i - k - 1
            graph.add_edge(edge[0], edge[1])
            i = i + k + 1
        return graph

    @classmethod
    def generate_PreLogZER_graph(cls, n: int, E: int, p: float) -> Graph:
        """Generate a random graph using PreLogZER model."""
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
        while i < E:
            phi = random.randrange(0, mx)
            k = int(max(math.ceil(log[phi] / c), 0))
            edge = random.choice(edges)
            if graph.has_edge(edge[0], edge[1]):
                i = i - k - 1
            graph.add_edge(edge[0], edge[1])
            i = i + k + 1
        return graph

    @classmethod
    def generate_prezer_graph(cls, n: int, e: int, p: float, m: int = 10) -> Graph:
        """Generate a random graph using PreZER algorithm."""

        def cumulative_probability(k: int) -> float:
            """Calculate cumulative probability of edges being skipped (0-k)."""
            return 1 - (1 - p) ** (k + 1)

        def log(x: float, base: float) -> float:
            """Calculate logarithm of a number `x` with base `base`."""
            return math.log(x) / math.log(base)

        def decode_edge_index(index: int) -> tuple[int, int]:
            """Decode an edge index into a pair of vertex labels."""
            return index // n, index % n

        vertices = {Vertex(i) for i in range(n)}
        graph = Graph(vertices)

        cumulative_skip_probabilities = [cumulative_probability(k) for k in range(m)]

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
                skip_value = math.ceil(log(x=1 - alpha, base=1 - p)) - 1
            new_edge_count = edge_count + skip_value + 1
            vertex_i, vertex_j = decode_edge_index(new_edge_count)

            if vertex_i != vertex_j:
                graph.add_edge(vertex_i, vertex_j)
                edge_count = new_edge_count

        graph.remove_edge(vertex_i, vertex_j)
        return graph
