"""Utility functions for the project."""
import math


def decode_edge(index: int, n: int) -> tuple[int, int]:
    """Decode an edge index into a pair of vertex labels."""
    return index // n, index % n


def decode_edge_no_self_loops(index: int, n: int) -> tuple[int, int]:
    """Decode an edge index into a pair of vertex labels, excluding self-loops."""
    i, j = decode_edge(index, n)
    return (i, j) if i != j else decode_edge_no_self_loops(index + 1, n)


def calculate_n_c(n: int, c: int = 42) -> int:
    """Calculate the number of edges used in Erdos-Renyi paper."""
    return int(0.5 * n * math.log(n) + c * n)
