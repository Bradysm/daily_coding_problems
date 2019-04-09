# Given a binary tree, return the pre-order traversal of its nodes' values
# because the recursive solution is obvious, complete the iterative one

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# to mimic recursion we will be using a stack. Since recursion continually adds stack frames
# onto the runtime stack, we should think of it in the same way to turn recursion into iteration
# next, we then know pre-order goes root->left->right
# thus, we want to initially add the root, then add right, then add left
# the reason we do this is because if the root of the tree has two children, we want the left
# child on the top of the stack. Thus, we push right then left
# we then continue poppping and pushing until the stack is empty

def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    order = []
    stack = []  # stack to mimic the recursion
    if root is not None:
        stack.append(root)

    # pop off the next node then add right, left (we want left to be ontop)
    while len(stack) > 0:
        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        # add to the end
        order.append(node.val)

    # return pre-order
    return order
