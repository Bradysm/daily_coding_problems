
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


The thought process for this is that the largest node in a BST is the node all the way to the right
so if we keep taking the option to go to the right, and when we get to the node that does not 
allow us to move any farther right, that is the maximum value in the BST. So, the second largest node
in the tree, must be really close to that node, right? Well, kind of! If the maximum node is itself
a leaf node, then the node previous to that is the second largest node in the tree. But what happens
if that node is not a leaf node? Well, let's think about it, it could not have a subtree to the right
because that would mean that there is a node with a value greater than the current node which we're considering
the maximum, so that would contradict our claim of the node being the max node. So, the only case could be,
is if there is a left subtree. Now, if we think about the node that led us to the maximum node, (10 in the diagram above)
everything to the right of this node is greater than it, so returning 10 in this case would be wrong, because
we know that 13 is the second largest node. So, we can see, that if the max node has a left subtree, then we
want to return the maximum node from the left subtree, as that will be the second largest node, and NOT 10.
If the max node does not have a left subtree, then we will return the node that is previous to the max node.


So, this is simple. move as far to the right as possible, keep track of the current a prev node,
once there is no more moves to the right, check to see if there is a left subtree on the current node
if there isn't, then return prev, otherwise, return the max node from the left subtree. We then know this
algorithm is bounded by the height of the tree so the algorithm runs in O(h) time where in the best
case will be O(logn) (balanced tree) and in the worst case will be O(n) (essentially a linked list) and O(1) space.

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