class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        return False if self.left or self.right else True



def balanced_tree(root):
    # empty tree, return true
    height, balanced = balanced_recursive(root)

    return balanced


def balanced_recursive(root):
    """
    Checks to see if the subtrees below a node are balanced
    returns (node_height, balanced)
    """
    if not root: return (0, True)
    if root.is_leaf(): return (1, True) 

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