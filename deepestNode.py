"""
Hi, here's your problem today. This problem was recently asked by Google:

You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.


My thought process here is to use a queue, push in the node and the depth of the node
in a tuple, then if the node in question is deeper, then set that to the new deepest node

At the end, return the deepest

This will run in O(n) space and O(n) time
You could use a DFS instead of BFS and this would decrease the space to O(d),
but, I like using levels, I think they make the most sense for me to understand
in this situation, plus, RIP to Avicii
"""


class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
    # check for an empty tree
    if not node: return node

    # Fill this in.
    deepest_node = (node, 1)
    queue = [deepest_node]

    # while there are still nodes to visit
    while queue:
        # pop off the front of the queue
        node_and_level = queue.pop(0)
        curr_node, curr_node_level = node_and_level

        # update the deepest node in a fancy way using max
        deepest_node = max(deepest_node, node_and_level, key=lambda x: x[1])
        
        # add children to the queue if there are any
        next_level = curr_node_level + 1
        if curr_node.right: queue.append((curr_node.right, next_level))
        if curr_node.left: queue.append((curr_node.left, next_level))

    return deepest_node


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))