"""Main module for the Streamlit application."""

import time
from math import comb

import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

from src.algorithms.er import ER
from src.algorithms.graph_generation import GraphGeneration
from src.algorithms.graph_properties import GraphProperties
from src.algorithms.pre_zer import PreZER
from src.algorithms.prelog_zer import PreLogZER
from src.algorithms.zer import ZER

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.imgur.com/S9GoZzC.jpg");
}

[data-testid="stAppViewBlockContainer"] {
    background-color: rgba(255, 255, 255, 1);
    padding: 5em;
    margin-top: 5em;
    }
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

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
    start_time = time.time()
    graph = graph_generation_algo.generate(n, E, p)
    end_time = time.time()
    networkx_graph = graph.to_networkx()

    import streamlit as st

    st.header("Graph properties")
    col1, col2 = st.columns(2)
    col1.metric("Order", n)
    col2.metric("Size", graph.size)

    st.header("Connectivity")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average degree", GraphProperties.average_degree(graph))
    col2.metric(
        "Connected", "Yes" if GraphProperties.is_connected(networkx_graph) else "No"
    )
    col3.metric(
        "Number of components", GraphProperties.number_of_components(networkx_graph)
    )

    st.header("Coloring")
    col1, col2 = st.columns(2)
    col1.metric("Chromatic number", GraphProperties.chromatic_number(networkx_graph))

    st.header("Planarity")
    col1, col2 = st.columns(2)
    col1.metric("Planar", "Yes" if GraphProperties.is_planar(networkx_graph) else "No")

    st.header("Maximal Independent Set")
    col1, col2 = st.columns(2)
    col1.metric("Size", len(GraphProperties.maximal_independent_set(networkx_graph)))

    st.header("Visualization")
    fig, ax = plt.subplots(1, 1, figsize=(width, height))
    position = nx.kamada_kawai_layout(networkx_graph)
    nx.draw(networkx_graph, position, node_color="skyblue", edge_color="black")
    st.pyplot(fig)
