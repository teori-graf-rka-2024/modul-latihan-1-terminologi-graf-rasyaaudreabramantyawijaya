#1
import pytest
import networkx as nx 
def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    my_graph = nx.Graph()
    my_graph.add_edges_from(edges)
    return my_graph

#2 
def get_degree(G: nx.Graph, node: int) -> int:
    degrees = G.degree(node)
    return degrees

#3
import networkx as nx
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    dfs = list(nx.dfs_preorder_nodes(G, source=start))
    return dfs

#4
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    bfs = list(nx.bfs_tree(G, source=start))
    return bfs

#5
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    shortest = nx.shortest_path(G, source=source, target=target)
    return shortest

#6
import matplotlib.pyplot as plt
def visualize_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()
    return "Graph visualized"
