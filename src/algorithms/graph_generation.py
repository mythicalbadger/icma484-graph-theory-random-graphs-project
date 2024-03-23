"""Module with graph generation algorithms."""

import abc

from src.models.graph import Graph


class GraphGeneration(metaclass=abc.ABCMeta):
    """A class to generate random graphs."""

    @classmethod
    def __subclasshook__(cls, __subclass) -> bool | _NotImplementedType:  # noqa ann001
        """Check if the class has the required methods."""
        return (
            hasattr(__subclass, "generate_enp") and callable(__subclass.generate)
        ) or NotImplemented

    @abc.abstractmethod
    def generate(self, n: int, e: int, p: float) -> Graph:
        """Generate a random graph given max number of edges."""
        raise NotImplementedError
