"""Module with graph properties algorithms."""

import networkx

from src.models.graph import Graph


class GraphProperties:
    """A class to represent graph properties algorithms."""

    @classmethod
    def average_degree(cls, graph: Graph) -> float:
        """Return the average degree of the graph."""
        return sum(v.degree() for v in graph.vertices.values()) / graph.order

    @classmethod
    def is_connected(cls, nx_graph: networkx.Graph) -> bool:
        """Check if the graph is connected."""
        return networkx.is_connected(nx_graph)

    @classmethod
    def chromatic_number(cls, nx_graph: networkx.Graph) -> int:
        """Return the chromatic number of the graph."""
        colors = networkx.greedy_color(nx_graph).values()
        return len(set(colors))

    @classmethod
    def number_of_components(cls, nx_graph: networkx.Graph) -> int:
        """Return the number of connected components in the graph."""
        return networkx.number_connected_components(nx_graph)

    @classmethod
    def num_cycles(cls, nx_graph: networkx.Graph) -> int:
        """Return the number of cycles in the graph."""
        return len(list(networkx.simple_cycles(nx_graph)))

    @classmethod
    def maximal_independent_set(cls, nx_graph: networkx.Graph) -> set[int]:
        """Return the maximal independent set of the graph."""
        return set(networkx.maximal_independent_set(nx_graph))

    @classmethod
    def is_planar(cls, nx_graph: networkx.Graph) -> bool:
        """Check if the graph is planar."""
        return networkx.check_planarity(nx_graph)[0]

    @classmethod
    def greatest_component(cls, nx_graph: networkx.Graph) -> networkx.Graph:
        """Return the greatest component of the graph."""
        giant = max(networkx.connected_components(nx_graph), key=len)
        return nx_graph.subgraph(giant)
