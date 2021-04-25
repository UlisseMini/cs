"""
Depth first search, O(V+E)

Isn't super useful on its own,
but when augmented with other algorithms it shines.

For example, identifying components: https://youtu.be/7fujbpJ0LB4

"""

from graphs import G1 as graph


visited = [False] * len(graph)

def dfs_recursive(at):
    if visited[at]: return
    yield at
    visited[at] = True

    for neighbor in graph[at]:
        yield from dfs_recursive(neighbor)


for node in dfs_recursive(0):
    print(node)
