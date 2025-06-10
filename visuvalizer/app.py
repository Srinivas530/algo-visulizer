import streamlit as st
import random
from algooo import sorting, graphii

st.set_page_config(page_title="Algorithm Visualizer", layout="wide")
st.title("🎞️ Algorithm Visualizer with Live Animation")

mode = st.sidebar.selectbox("Choose Mode", ["Sorting", "Graph Traversal"])
speed = st.sidebar.slider("Speed (sec)", 0.01, 1.0, 0.1)

if mode == "Sorting":
    algo = st.selectbox("Select Sorting Algorithm", [
        "Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort", "Merge Sort"
    ])
    size = st.slider("Array Size", 5, 50, 25)
    array = [random.randint(10, 100) for _ in range(size)]
    st.write("Initial Array:", array)

    if st.button("Start Sorting"):
        chart = st.empty()
        sort_func = {
            "Bubble Sort": sorting.bubble_sort,
            "Insertion Sort": sorting.insertion_sort,
            "Selection Sort": sorting.selection_sort,
            "Quick Sort": sorting.quick_sort,
            "Merge Sort": sorting.merge_sort
        }[algo]
        sort_func(array, speed, chart)

elif mode == "Graph Traversal":
    algo = st.selectbox("Select Graph Algorithm", ["BFS", "DFS", "Dijkstra"])
    grid_size = st.slider("Grid Size", 5, 30, 10)

    st.subheader("Start Position")
    start_x = st.number_input("Start X", 0, grid_size - 1, 0, key="sx")
    start_y = st.number_input("Start Y", 0, grid_size - 1, 0, key="sy")

    st.subheader("Destination Position")
    end_x = st.number_input("End X", 0, grid_size - 1, grid_size - 1, key="ex")
    end_y = st.number_input("End Y", 0, grid_size - 1, grid_size - 1, key="ey")

    if st.button("Start Traversal"):
        chart = st.empty()
        start = (start_x, start_y)
        end = (end_x, end_y)
        if algo == "BFS":
            graphii.bfs(grid_size, start, end, speed, chart)
        elif algo == "DFS":
            graphii.dfs(grid_size, start, end, speed, chart)
        else:
            graphii.dijkstra(grid_size, start, end, speed, chart)
