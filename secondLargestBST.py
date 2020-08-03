
"""
Given the root to a BST, return the node containing the second
largest value

    8
   / \
       10
        \
         14
         /
        12
         \
          13

so here we would return 13
"""

# tree node
class Node:
    """
    Node used for a tree
    """
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.val = value

    # helper methods
    def has_right(self) -> bool:
        return True if self.right is not None else False
    
    def has_left(self) -> bool:
        return True if self.left is not None else False

    def is_leaf(self) -> bool:
        return False if self.has_right() or self.has_left() else True


def find_second_largest(root: Node) -> Node:
    """
    Finds the second largest node in a tree in O(h) time where h is the height of
    the tree. The space is O(1) as we only use pointers to nodes within the tree

    This solution assumes there is always two nodes in a tree. If there are not
    two nodes, then None will be returned, indicating that there is not second
    largest node.
    """
    prev_node = None
    curr_node = root

    # find the max while keeping track of the previous
    while curr_node.has_right():
        prev_node = curr_node
        curr_node = curr_node.right

    # if the max node has a left subtree, return the max from the left subtree
    if curr_node.has_left():
        return find_max_node(curr_node.left)
    
    # otherwise, return the prev node
    return prev_node


def find_max_node(root: Node) -> Node:
    curr_node = root

    # move to the right until there is no more nodes to the right
    while curr_node.has_right():
        curr_node = curr_node.right
    
    return curr_node



"""

   8
   / \
       10
        \
         14
         /
        12
         \
          13

"""
tree = Node(8, right=Node(10, right=Node(14, left=Node(12, right=Node(13)))))



"""
    8
   / \
  *   10
      / \
     9   14
"""
tree2 = Node(8, right=Node(10, right=Node(14), left=Node(9)))


print(find_second_largest(tree).val) # should print 13
print(find_second_largest(tree2).val) # should print 10