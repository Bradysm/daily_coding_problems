# Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z':
# a value of 0 represents 'a', a value of 1 represents 'b', and so on.
# Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# (As a reminder, any shorter prefix of a string is lexicographically smaller: for example,
# "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isLeaf(self, rt):
        """checks to see if a node is a leaf"""
        if rt.left is None and rt.right is None:
            return True
        return False

    def smallestFromLeaf(self, root):
        """
        Run a DFS to get the path of the sequence, and then return the shortest
        path lexiographically
        :type root: TreeNode
        :rtype: str
        """
        stack = [(root, "")]  # (current node, sequence path)
        paths = []  # list of valid paths
        while len(stack) > 0:
            node, path = stack.pop()
            path = chr(97 + node.val) + path
            if self.isLeaf(node):
                paths.append(path)
            else:
                if node.left is not None:
                    stack.append((node.left, path))
                if node.right is not None:
                    stack.append((node.right, path))

        return min(paths)  # return the smallest path