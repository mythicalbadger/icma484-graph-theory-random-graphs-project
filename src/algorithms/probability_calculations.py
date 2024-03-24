"""Module for benchmarking the algorithms / calculating probabilities."""
import time
from math import comb

import pandas as pd

from src.algorithms.er import ER
from src.algorithms.graph_properties import GraphProperties
from src.algorithms.prelog_zer import PreLogZER
from src.algorithms.zer import ZER


def run_benchmark() -> dict[str, dict[str, list]]:
    """Run benchmark for the algorithms.""" ""
    ps = [0.2, 0.4, 0.6, 0.8]
    ns = [10000]

    algorithms = {
        "ER": ER(),
        "ZER": ZER(),
        "PreLogZER": PreLogZER(),
    }

    benchmark_data = {
        algorithm: {
            "time": [],
            "n": [],
            "m": [],
            "p": [],
            "avg_degree": [],
            "connected": [],
            "components": [],
            "chromatic_number": [],
            "planar": [],
            "maximal_independent_set": [],
        }
        for algorithm in algorithms.keys()
    }

    for algorithm in algorithms.keys():
        for n in ns:
            for p in ps:
                max_edges = comb(n, 2)

                for _ in range(100):
                    start = time.time()
                    graph = algorithms[algorithm].generate(n, max_edges, p)
                    end = time.time()
                    networkx_graph = graph.to_networkx()
                    benchmark_data[algorithm]["time"].append(end - start)
                    benchmark_data[algorithm]["n"].append(n)
                    benchmark_data[algorithm]["m"].append(graph.size)
                    benchmark_data[algorithm]["p"].append(p)
                    benchmark_data[algorithm]["avg_degree"].append(
                        GraphProperties.average_degree(graph)
                    )
                    benchmark_data[algorithm]["connected"].append(
                        GraphProperties.is_connected(networkx_graph)
                    )
                    benchmark_data[algorithm]["components"].append(
                        GraphProperties.number_of_components(networkx_graph)
                    )
                    benchmark_data[algorithm]["chromatic_number"].append(
                        GraphProperties.chromatic_number(networkx_graph)
                    )
                    benchmark_data[algorithm]["planar"].append(
                        GraphProperties.is_planar(networkx_graph)
                    )
                    benchmark_data[algorithm]["maximal_independent_set"].append(
                        len(GraphProperties.maximal_independent_set(networkx_graph))
                    )

    return benchmark_data


if __name__ == "__main__":
    benchmark_data = run_benchmark()
    for algorithm in benchmark_data:
        df = pd.DataFrame(benchmark_data[algorithm])
        with pd.ExcelWriter(f"benchmark_{algorithm}_10000.xlsx") as writer:
            df.to_excel(writer, sheet_name=algorithm, index=False)
