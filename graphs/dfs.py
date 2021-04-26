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
    stack = [start]
    visited = [False] * len(graph)

    while stack != []:
        curr = stack.pop()
        if visited[curr]:
            continue

        yield curr
        visited[curr] = True

        # Reverse since we pop from the end of the stack, meaning before we visit
        # another neighbor is pushed, but we should visit the first guy first.
        for neighbor in reversed(graph[curr]):
            if not visited[neighbor]:
                stack.append(neighbor)


print('\niterative')
for node in dfs_iterative(graph, 0):
    print(node)
