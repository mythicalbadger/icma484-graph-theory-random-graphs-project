"""Main module for the Streamlit application."""

import matplotlib.pyplot as plt
from math import comb
import networkx as nx
import streamlit as st

from src.algorithms.graph_generation import GraphGeneration

st.write("Hello, world!")

n = st.number_input("Number of vertices", min_value=1, value=10)
p = st.number_input("Edge probability", min_value=0.0, max_value=1.0, value=0.5)
E = st.number_input("Max number of edges", min_value=0, max_value=comb(n, 2), value=15)

if st.button("Generate graph"):
    graph = GraphGeneration.generate_erdos_renyi_graph(n, p)
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    networkx_graph = graph.to_networkx()
    position = nx.kamada_kawai_layout(networkx_graph)

    nx.draw(networkx_graph, position, node_color="skyblue", edge_color="black")
    st.pyplot(fig)

if st.button("Generate ER graph"):
    graph = GraphGeneration.generate_ER_graph(n, E, p)
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    networkx_graph = graph.to_networkx()
    position = nx.kamada_kawai_layout(networkx_graph)

    nx.draw(networkx_graph, position, node_color="skyblue", edge_color="black")
    st.pyplot(fig)

if st.button("Generate ZER graph"):
    graph = GraphGeneration.generate_ZER_graph(n, E, p)
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    networkx_graph = graph.to_networkx()
    position = nx.kamada_kawai_layout(networkx_graph)

    nx.draw(networkx_graph, position, node_color="skyblue", edge_color="black")
    st.pyplot(fig)

