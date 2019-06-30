# Given a BST and a target value, return the closest value to the target, that is contained within the bst

#         10
#        /  \
#       5   15
#      / \  / \
#     2  5 13  22
#           \
#           14

# Okay, so when I see a BST problem, I immediately think of the fact that I'm given something that is sorted
# for a reason and I need to make a better algorithm as a result of that; and when I say better I mean bigger, faster, stronger (ayye wassup ye)
# So, to utilize the sorting to it's full potential, we should be thinking of how search is done in a BST. When we get
# to a node, we want to move in the direction that will lead us closer to the value that we're searching for
# so, let's say we're searching for 12, we will start at 10, move to the right because 12 > 10, then we will move to the left
# because 12 < 15 and then to the right again because 12 < 13. We're at null, so we should have the answer of the closest
# value by now. 

# okay, but hold up hold up. We need something to maintain the closest value. So we will use a variable called closest
# and initalize that to infinity because we want a difference that is unbounded initially. as we move through the tree
# we will check to see if the difference betwee tree.value and target is < closest-target. If it is, then update
# closest to tree.value and then keep moving along. Note, that you want to use abs for the difference incase there are negatives
# That means, if we follow on the correct searching path, we will run into the closest value to our searched value within the tree

# assuming that the tree is balanced,(best case) this will run in O(logn) time and O(1) space, worst case O(n) time O(1) space
# the worst case will happen when the tree looks like a linked list

# note that you can also create this algorithm recursively, but the space will move up to O(logn) for best case and O(n) for worst
# The space comes from the stack frames being created (look into recursion if you don't understand that)

import sys

def findClosestBstValue(root, target):
    closest = sys.maxsize
    currNode = root
    while currNode is not None:
        closest = min(currNode.val, closest, key=lambda x: abs(x-target))
        if currNode.val == target: break
        elif target < currNode.val: currNode = currNode.left
        else: currNode = currNode.right
    return closest