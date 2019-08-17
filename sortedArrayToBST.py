# Hi, here's your problem today. This problem was recently asked by LinkedIn:

# Given a sorted list of numbers, change it into a balanced binary search tree. 
# You can assume there will be no duplicate numbers in the list.

# okay, so this problem is actually interesting. Although, not challenging, it requires you to think a bit though.
# the first thing you should do when you get a whole bunhc of jargon is to do a practice problem

# [1, 2, 3, 4, 5, 6, 7]

# we want the output to be 

#       4
#   2       5
# 1   3   6   7

# Now, let's think about what it means for something to be a BST. We want for every node in the BST
# for everything to the right of it to be greater than or equal to the node, and everything to the left
# of the node to be less than the value at that node. Great. Now, let's look at the balanced definiton
# so for something to be balanced, the last full row in the tree must be at most one level less
# than the deepest node in the tree. So, to keep something balanced, it would make since if
# we divided the numbers in half, put one half on one side of the tree, and then put the other
# half on the other side of the tree. Doing this would be acting optimally and would ensure
# that we create a balanced tree. Since we know the numbers are already in sorted order, we can use this
# to our advantage. Notice that is we pull the middle number, 4, out of the list, then we have 
# a situation where everything to the left of 4 in the list is less than 4 and everything to the 
# right is greater than 4. We can then create a new node and give 4 the value for that node.
# we can then set the left of that node to the recursive result of this function for the 
# left part of the array, and then we can set the right child of this node to the recursive result
# for the right child of the array. By picking the number in the middle, we act optimally to create
# a balanced tree, and we allow ourselves to utilize the definiton of a BST to our advantage. We 
# know we're finished when the left pointer is greater than or equal to the right pointer, or with
# python (since we can utilize array splicing) when the array is empty

# let's look at how we would do this in code

# this implementation will have O(N) runtime and O(logn) space
# every number in the array has a recursive call, and there will be at most logn calls on the
# stack at once

from tree import Tree # tree node that I use for tree problmes 

def sorted_list_to_BST(nums):
    if nums is None or len(nums) == 0: return None # the base case
    mid = (len(nums)-1) // 2
    root = Tree(nums[mid])
    root.left = sorted_list_to_BST(nums[:mid])
    root.right = sorted_list_to_BST(nums[mid+1:])
    return root
    