"""
Some graphs for testing algorithms on, some created with https://csacademy.com/app/graph_editor/
"""

def K(n):
    "Fully connected graph"

    graph = [[j for j in range(n) if j != i] for i in range(n)]
    return graph



G1 = [[2,4,5], [4,5], [3,4], [], [5], []]

