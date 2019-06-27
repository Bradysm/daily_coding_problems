def dfs(i, graph, visited):
    # check to see if there are no children and if in visited
    if len(graph[i]) == 0: return True
    if i in visited: return False

    # add the node to visite
    visited.append(i)
    for node in graph[i]:
        res = dfs(node, graph, visited)
        if res: return True
    return False


def eventualSafeNodes(graph):
    """
    :type graph: List[List[int]]
    :rtype: List[int]
    """
    safe = []  # contains the safe nodes
    print(len(graph[5]))
    if dfs(5, graph, []):
        safe.append(5)
    safe.sort()
    return safe


# testing graph
g = [[1, 2], [2, 3], [5], [0], [5], [], []]
print(eventualSafeNodes(g))
