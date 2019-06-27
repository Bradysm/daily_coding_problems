# problem: given root to binary tree, validate if BST

# This problem is more so understanding what is going on when you create a binary search tree.
# what really helped me create this, my I say BEAUTIFUL, peace of code is realizing that binary
# searches slowly cut the data down and create an INTERVAL that the value must land between
# this algorithm is no different. You start with the interval -inf - +inf, check the root
# against that and then split the tree in half. Okay, now the interval needs to change.
# the max anything can be to the left of the root is the value at the root, and all elements to
# the right of the root must be > then the root. This then means that When you recursively
# call the validate function, you're going to want to pass in the roots values to update the interval
# that you're validating against. This moving of information from the parent nodes to the children
# is very important and you must be able to do it both ways in interviews!!!

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, -sys.maxsize-1, sys.maxsize)
    
    def validate(self, root: TreeNode, lrange: int, rrange:int) -> bool:
        # check to see if node is within the defined interval
        if root is None: return True
        if not(root.val > lrange and root.val < rrange): return False
        
        # check its subtrees
        return self.validate(root.left, lrange, root.val) and self.validate(root.right, root.val, rrange)