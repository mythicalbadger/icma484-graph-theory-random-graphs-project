"""Main module for the Streamlit application."""

from math import comb

import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

from src.algorithms.er import ER
from src.algorithms.graph_generation import GraphGeneration
from src.algorithms.pre_zer import PreZER
from src.algorithms.prelog_zer import PreLogZER
from src.algorithms.zer import ZER

algorithms = {"ER": ER(), "ZER": ZER(), "PreLogZER": PreLogZER(), "PreZER": PreZER()}

st.title("Random Graph Generator")
st.sidebar.title("Parameters")

n = st.sidebar.number_input("Number of vertices", min_value=1, value=10)
p = st.sidebar.number_input(
    "Edge probability", min_value=0.0, max_value=0.99, value=0.5
)

col1, col2 = st.sidebar.columns(2)

with col1:
    placeholder_E = st.empty()
    if "E" not in st.session_state:
        st.session_state.E = 15
with col2:
    max_edges = st.sidebar.button("Max")
    if max_edges:
        st.session_state.E = comb(n, 2)

E = placeholder_E.number_input(
    "Max number of edges", min_value=0, max_value=comb(n, 2), key="E"
)

algorithm = st.sidebar.selectbox(
    label="Select a graph generation algorithm",
    options=list(algorithms.keys()),
    index=0,
)

st.sidebar.title("Plot Settings")
width = st.sidebar.slider("plot width", 1, 25, 20)
height = st.sidebar.slider("plot height", 1, 25, 20)

graph_generation_algo: GraphGeneration = algorithms[algorithm]

if st.sidebar.button("Generate graph"):
    graph = graph_generation_algo.generate(n, E, p)
    fig, ax = plt.subplots(1, 1, figsize=(width, height))
    networkx_graph = graph.to_networkx()
    position = nx.kamada_kawai_layout(networkx_graph)

    nx.draw(networkx_graph, position, node_color="skyblue", edge_color="black")
    st.pyplot(fig)

    st.write(f"n: {graph.order}")
    st.write(f"m: {graph.size}")
