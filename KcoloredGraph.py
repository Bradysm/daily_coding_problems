"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, 
write a function to determine whether each vertex in the graph can be colored 
such that no two adjacent vertices share the same color using at most k colors.
"""

def k_coloring(graph, k):
    values = [None] * len(graph) # array containing the value within the domain of k
    return solve_csp(0, values, graph, k)


def solve_csp(curr_node, node_values, graph, k):
    # check to see if the current node is greater than the length of the grapp
    # then return true because we've assigned values that align with constraints
    if curr_node >= len(graph): return True

    # pick a value, check to see if valid, if valid move to next node otherwise, try agian
    next_node = curr_node + 1
    for value in range(k):
        node_values[curr_node] = value

        # check to see if the current 
        if valid_constraints(curr_node, graph, node_values) and solve_csp(next_node, node_values, graph, k):
            return True
        
        # not valid or not a valid selection, backtrack and try a new value

    return False
    


def valid_constraints(curr_node, graph, node_values) -> bool:
    node_edges = graph[curr_node]

    for node, has_edge in enumerate(node_edges):
        # check to see if there is a connection that also has the same value
        if has_edge and (node_values[node] == node_values[curr_node]): 
            return False

    # return true if there is a connection without the same value
    return True


test_graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0 ,0]
]




print(k_coloring(test_graph, 3)) # this should be true because you should be able to color anything with three colors
print(k_coloring(test_graph, 2)) # this is false because you get stuck with the dependency at assigning to the node 2