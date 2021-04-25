"""
Return the dot representation of various graphs, for visualization.
"""

import graphviz

def adj_list(graph):
    dot = graphviz.Digraph()

    for node in range(len(graph)):
        dot.node(str(node))
        for neighbor in graph[node]:
            dot.edge(str(node), str(neighbor))

    return dot


