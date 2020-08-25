class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        return False if self.left or self.right else True

"""
This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced. 
A height-balanced binary tree can be defined as one in which the heights 
of the two subtrees of any node never differ by more than one.



THought process: go as far down the tree and then build up the solution
using recursion. At each node, we need to check if the left and
right subtrees of that node is balanced, and then return the height
of that node so nodes above it can determine if their subtrees are balanced.

We then will create a recursive function that keeps getting called until
the tree node that we're at is a leaf. At this point we know the subtrees
are balanced becuase they're both null and we know that the height of the
leaf. People define this differently but for this problem, im just going
to define the height of a leaf as 0. It's perfectly fine to start at 1
if that's you kind of thing. We can then give the calling node enough
information to make it's judgement by giving it back the height of
our node and whether it's subtrees were balanced. Then the calling node
will take our two heights and see if they differ no more than 1, and will
also check to see if their subtrees were balacned below it, becuase
just becuase the current nodes height are not off by more than one. it's important
to consider the nodes below them and if they were off by more than one.

If both subtrees were balanced and their heights differed by no more than
1, then we can calculate the height of the current node and then 
returning true for the current node being balanced. Otherwise, we can
calculate the height and return false to let the calling node know that
the subbtree below it, at some point, was not balance.

Cheers!

"""

def balanced_tree(root):
    # empty tree, return true
    height, balanced = balanced_recursive(root)

    return balanced

# O(N) space and O(N) time

def balanced_recursive(root):
    """
    Checks to see if the subtrees below a node are balanced
    returns (node_height, balanced)
    """
    if not root: return (-1, True)
    if root.is_leaf(): return (0, True) 

    # get the height of the left subtree
    height_left, balanced_left = balanced_recursive(root.left)
    height_right, balanced_right = balanced_recursive(root.right)

    # check to see if either the right or the left is not balanced
    subtrees_balanced = True if balanced_left and balanced_right else False
    node_height = max(height_left, height_right) + 1
    balanced_tree = True if subtrees_balanced and (abs(height_left - height_right) < 2) else False

    return (node_height, balanced_tree)




tree1 = Tree(val=1, left=Tree(2), right=Tree(3))
print(balanced_tree(tree1))

# still balanced
tree2 = Tree(val=1, left=Tree(2, left=Tree(4)), right=Tree(3))
print(balanced_tree(tree2))

#unbalanced
unbalanced = Tree(val=1, left=Tree(2, left=Tree(4, left=Tree(5))), right=Tree(3))
print(balanced_tree(unbalanced))