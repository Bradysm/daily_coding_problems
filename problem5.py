# Leet code 129
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.
#            1
#          2   3
# the sum would be 12+13 = 25


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumPaths(root, 0)

    def sumPaths(self, rt, c_sum):
        """sums the paths to the leaf of the tree from root"""
        if rt is None: return 0
        c_sum = (c_sum * 10) + rt.val
        if rt.left is None and rt.right is None: return c_sum
        return self.sumPaths(rt.right, c_sum) + self.sumPaths(rt.left, c_sum)


