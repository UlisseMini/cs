"""
Depth first search, O(V+E)

Isn't super useful on its own,
but when augmented with other algorithms it shines.

For example, identifying components: https://youtu.be/7fujbpJ0LB4

"""

from graphs import G1 as graph


visited = [False] * len(graph)

def dfs_recursive(graph, at):
    if visited[at]: return
    yield at
    visited[at] = True

    for neighbor in graph[at]:
        yield from dfs_recursive(graph, neighbor)


print('recursive')
for node in dfs_recursive(graph, 0):
    print(node)


def dfs_iterative(graph, start):
    path = [start]

    visited = [False] * len(graph)

    while path != []:
        curr = path[-1]
        if not visited[curr]:
            yield curr
            visited[curr] = True

        deeper = False
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                path.append(neighbor)
                deeper = True
                break

        if not deeper:
            path = path[:-1]


print('\niterative')
for node in dfs_iterative(graph, 0):
    print(node)
