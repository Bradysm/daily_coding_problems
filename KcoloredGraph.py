"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, 
write a function to determine whether each vertex in the graph can be colored 
such that no two adjacent vertices share the same color using at most k colors.


O(n) space where n is the number of nodes in the graph
O(n*n*k) time beacuse at every node you at the worst go through every value and check every dependency edge


To me, this problem is VERY similar to the N queens problem. Essentially, what we're trying to do, is go
through the graph, select a node, assign it a value, then try to move through the graph all the way
until there is no more nodes to assign a value, and all the nodes have been assigned a value that is 
valid.

My thought process is that, in the worst case, we need to try all combinations of colorings in the graph.
Now, technically we could just assign random colors, then keep flipping the ones that aren't valid
until they become valid and then call it a day. This really doesn't sound like to great of an idea to me,
but its a decent start none the less.

Hmm. Okay, so let's try to break the problem down. Let's assume we're at a node in the graph. We don't really
care about how we got there, but we want to asssign this node a color. Now, we know that the only valid
colors are the colorst that are in the domain of colors, D, which are not in the set of colors S, which
represent the set of colors for nodes that are already colored which are connected to our current node
with an edge. You might have to read through that another time to make sure you fully understand what im 
trying to say because that is a mouth full. We can then take our current node, assign it a color that is in
the set of valid colors, given the current graph orientation of color assignments, and then move onto the
next node in the graph, and continue this pattern until we get to a point where the set of valid colors is
empty and we still have a node that is in need of assignment, or until we've assigned all the nodes a valid
color and have completed our job!

Now, how do we move to the next node? Well, since we're given the graph in a matrix, I find it easiest to think
of the node as simply the index we're currentl at. So index 0, would be the first node, and when we ask the
graph for the edges from index zero to other nodes all we need to do is graph[node] and this will return an
array of length n filled with 0's and 1's. The index that we're at in that array represents a node within the
graph and if there is a 1 as the value at that index, then that means that there is a connection between our
current node and the other node in the graph. If there is a zero, then there is no connection to that node and thus
no constraint between our node and that node.

Now that we know how to traverse the graph, let's write a backtracking algorithm to solve this problem for us.
First, we will start at node 0. Then we will assign it a node in the domain of valid colors, and then move onto
node 1 and check to see if there is a valid color that can be assigned given our current coloring orientation.
If there is, great, assign it that value and move onto node 2. We keep this process going until our node index
is greater than the length of the graph. This means that we've successfully colored the whole graph in a valid
orientation. If we run into a situation where we can't add a valid color with our current orientation, then
we backtrack and have the previous node try a different color. And this backtracking continues until we satisfy
the constraints again.

Great! Let's write the code. Note that in the code below, I was speed coding and I chose to check the range
of all colors and then check to see if it's valid. Another perfectly fine solution would be to create a function
called, valid_colorings and then have it return a list of valid colorings instead of also checking to see if it's
valid in the if statement, in fact, im going to do that right
"""

def k_coloring(graph, k):
    values = [None] * len(graph) # array containing the value within the domain of k
    return solve_csp_2(0, values, graph, k)



def solve_csp(curr_node, node_values, graph, k):
    # check to see if the current node is greater than the length of the grapp
    # then return true because we've assigned values that align with constraints
    # and have no more nodes to check. Also a graph with no nodes in it can be valid with any k of colors
    if curr_node >= len(graph): return True

    # pick a value, check to see if valid, if valid move to next node otherwise, try agian
    next_node = curr_node + 1
    for value in range(k):
        node_values[curr_node] = value

        # check to see if the current node coloring is valid, then check to see if we can create a valid coloring
        if valid_constraints(curr_node, graph, node_values) and solve_csp(next_node, node_values, graph, k):
            return True
        
        # not valid or not a valid selection, backtrack and try a new value

    # did not find a valid coloring for the current orientation return false
    return False
    


def solve_csp_2(curr_node, node_values, graph, k):
    # check to see if the current node is greater than the length of the grapp
    # then return true because we've assigned values that align with constraints
    # and have no more nodes to check. Also a graph with no nodes in it can be valid with any k of colors
    if curr_node >= len(graph): return True

    # pick a value, check to see if valid, if valid move to next node otherwise, try agian
    next_node = curr_node + 1
    for value in valid_colorings(curr_node, graph, node_values, k):
        node_values[curr_node] = value

        # check to see if we can construct a valid coloring with the given orientation
        if solve_csp_2(next_node, node_values, graph, k): return True
        
        # not valid or not a valid selection, backtrack and try a new value

    # did not find a valid coloring for the current orientation return false
    return False
    



def valid_colorings(curr_node, graph, node_values, k) -> list:
    colors = set([color for color in range(k)])
    node_edges = graph[curr_node]

    for node, has_edge in enumerate(node_edges):
        node_color = node_values[node]
        if has_edge and node_color in colors:
            colors.remove(node_color)
    
    return list(colors)



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

test_graph_2 = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]




print(k_coloring(test_graph, 3)) # this should be true because you should be able to color anything with three colors
print(k_coloring(test_graph, 2)) # this is false because you get stuck with the dependency at assigning to the node 2

print(k_coloring(test_graph_2, 2)) # this is true, set 0 to value 0 and then node 1 and 2 to value 1