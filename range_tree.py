"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), 
return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).

"""

import math

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def is_leaf(self) -> bool:
        """
        if the node has a left or a right childen, then false is returned, otherwise
        true is returned
        """
        return not (self.left or self.right)


def sum_tree_range(root: Node, num_range:list) -> int:
    """
    Sums the nodes within the BST that fall within the range given by
    the two element array containing the range to be summed.
    range: list witht the first element being the lower bound, and the second being the upper bound (inclusive)
    bst_root: root of the BST 
    """
    return sum_tree_range_recursive(root, num_range, [float("-inf"), float("inf")])


def sum_tree_range_recursive(root: Node, num_range:list, bst_range: list) -> int:
    """
    O(R) space and O(R) time
    - where R represents the size of the range
    - we only follow down the tree whne there is a path that can be within the range
        as a result, the upper bound of recursive calls is the size of the range itself
    """

    # check for base case of null root
    if not root: return 0

    # check to see if BST has any path that could some within the range
    if not intersecting_ranges(bst_range, num_range): 
        print("not intersecting range")
        return 0

    # calculate the nodes position within the range
    node_position = calculate_range_position(root.value, num_range)

    # add the current node to the sum if it's within the range, otherwise, set sum to 0
    range_sum = 0 if node_position is not 0 else root.value

    # the current node has a value less than the range (or within range and still need to expore), so move to the right
    # SOLVE TO THE RIGHT
    if node_position == -1 or node_position == 0: 
        print("Moving right", [root.value, bst_range[1]])
        range_sum += sum_tree_range_recursive(root.right, num_range, [root.value, bst_range[1]])

    # the current node has a value greater than the range (or within range and still need to expore), so move to the left
    # SOLVE TO THE LEFT
    if node_position == 1 or node_position == 0:
        print("Moving left", [bst_range[0], root.value])
        range_sum += sum_tree_range_recursive(root.left, num_range, [bst_range[0], root.value])

    return range_sum



# DOES NOT HAVE THE BST RANGE OPTIMIZATION
def sum_tree_range_iterative(root: Node, num_range: list) -> int:
    range_sum = 0
    stack = [root] if root else []

    # while the stack isn't empty
    while stack:
        # get the current node, and calculate it's range position
        curr_node = stack.pop()
        if not curr_node: continue
        curr_node_range_position = calculate_range_position(curr_node.value, num_range)

        # if within the correct range, add the value
        if curr_node_range_position == 0: 
            range_sum += curr_node.value

        # add children to stack based on it's position within the range
        # Explore the right
        if curr_node_range_position == -1 or curr_node_range_position == 0: stack.append(curr_node.right)

        # Explore the left
        if curr_node_range_position == 1 or curr_node_range_position == 0: stack.append(curr_node.left)

    return range_sum  


def intersecting_ranges(a, b) -> bool:
    intersection = min(a[1], b[1]) - max(a[0], b[0])
    return True if intersection > 0 else False

def calculate_range_position(node_value: int, num_range: list) -> int:
    """
    if the node_value is within the range, then 0 is returned,
    if it's below the range, then -1 will be returned if it's
    greater than the range, then 1 will be returned
    """
    if node_value < num_range[0]: return -1
    if node_value > num_range[1]: return 1
    return 0


"""
    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).

"""
# bottom level
two = Node(value=2)
four = Node(value=4)
six = Node(value=6)
ten = Node(value=10)
eleven = Node(value=11, left=ten)
sixteen = Node(value=16, left=eleven)


# second level
three = Node(value=3, right=four, left=two)
eight = Node(value=8, right=sixteen, left=six)

# top level
five = Node(value=5, right=eight, left=three)

# recursive implementation
print("Recursive soltution")
print(sum_tree_range(five, [4, 9]))
print(sum_tree_range(eight, [4, 9]))
print(sum_tree_range(three, [4, 9]))


# iterative impelmentation
print("\nIterative soltution")
print(sum_tree_range_iterative(five, [4, 9]))
print(sum_tree_range_iterative(eight, [4, 9]))
print(sum_tree_range_iterative(three, [4, 9]))

