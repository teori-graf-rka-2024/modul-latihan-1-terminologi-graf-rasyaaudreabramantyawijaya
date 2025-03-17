#1
import pytest
import networkx as nx 
def make_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    my_graph = nx.Graph()
    my_graph.add_edges_from(edges)
    return my_graph
edges=[(1,2), (2,3), (3,4), (4,5)]
graph = make_graph(edges)
print(graph)

#2 
def get_degree(G: nx.Graph, node: int) -> int:
    degrees = G.degree(node)
    return degrees
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3,4), (4,5)]) 
nodes = 2
print(get_degree(G, nodes))

#3
import networkx as nx

def traversal(G: nx.Graph, start: int) -> list[int]:
    dfs = list(nx.dfs_preorder_nodes(G, source=start))
    return dfs

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3,4), (4,5)]) 
print(traversal(G, 1))

#4
def traversal(G: nx.Graph, start: int) -> list[int]:
    bfs = list(nx.bfs_tree(G, source=start))
    return bfs
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3,4), (4,5)])  
print(traversal(G, 1))

#5
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    shortest = nx.shortest_path(G, source=source, target=target)
    return shortest

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3,4), (4,5)])  
print(find_shortest_path(G, 1, 3))

#6
import matplotlib.pyplot as plt

def visualize_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()
    return "Graph visualized"

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3,4), (4,5)])
print(visualize_graph(G))
