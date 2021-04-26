"""
Some graphs for testing algorithms on, some created with https://csacademy.com/app/graph_editor/
"""

def K(n):
    "Fully connected graph"

    graph = [[j for j in range(n) if j != i] for i in range(n)]
    return graph


def undirected(g):
    "Turn a directed graph into an undirected graph"

    g = g.copy()
    for node, neighbors in enumerate(g):
        for neighbor in neighbors:
            # (node, neighbor) edge exists add edge (neighbor, node)
            # if needed
            if node not in g[neighbor]:
                g[neighbor].append(node)

    return g


G1 = [[2,4,5], [4,5], [3,4], [], [5], []]

T1 = [[2], [4], [3,4], [5], [], []] # 1 center
T2 = [[], [0,3], [3], [], [1], [4], [3], [3], [4], [6]] # 2 centers


