"""
Check two trees are isomorphic

1. Root the tree by the center node(s)
2. Serialize the tree to a sorted string of its structure
3. Compare strings

"""


import graphs
import dot

graph = graphs.undirected(graphs.T2)


def center(graph):
    "We peel away leaves like an onion until we're at the center"

    leaves = []
    n = len(graph)

    # get initial leaf nodes
    for node in range(n):
        if len(graph[node]) <= 1:
            # no neighbors or 1 neighbor, we're a leaf
            leaves.append(node)


    neighbors = [len(adj) for adj in graph]

    done = len(leaves)
    while done < n:
        new_leaves = []

        for node in leaves:
            for neighbor in graph[node]:
                # removing this node means the parent has 1 less child
                neighbors[neighbor] -= 1
                if neighbors[neighbor] == 1:
                    new_leaves.append(neighbor)

        done += len(new_leaves)
        leaves = new_leaves


    return leaves


if __name__ == '__main__':
    c = center(graph)
    print('centers are', c)
    dot.adj_list(graph).view()
