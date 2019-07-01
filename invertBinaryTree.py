# This is one of the most infamous problems that I have done in a long time, and this
# is because the creator of Homebrew was not able to do this problem... so Google dropped him
# NOW, almost every software person at Google uses his software. So, if you aren't able
# to do a couple leet code problems, don't freak out. It's not the end of the world and we ALL
# struggle with different problems and question types

# okay, so the problem is probably pretty obvious, invert a Binary tree. But what does that even mean?

# Invert a binary tree.

#Example:

#Input:

#     4
#   /   \
#  2     7
# / \   / \
#1   3 6   9
#Output:

#     4
#   /   \
#  7     2
# / \   / \
#9   6 3   1


# so, pretty much when you look at the problem, given a root node, you want to swap the 
# right and left children. Then recursively keep doing that down the tree.

# let's first loook at the base case. So the base case would be if the root is null, so we just want to
# return null at that point

# so if you've ever done a problem that involves swapping numbers you know you want to use a temp variable
# to store the values and then move on from there to the next set. Here we will swap the right and left
# children and then tell the children to do the same thing for their children. We keep doing this down
# the tree and you keep going until you get to null, and then you work your way back up the tree!
# finally, you return the root node. Ez pz.

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None: return root
    swap_children(root)
    # invert the children
    invertTree(root.right)
    invertTree(root.left)
    return root


# iterative solution
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue) > 0:
		node = queue.pop() # get the first node
		if node is not None:
			swap_children(node)
			queue.append(node.left)
			queue.append(node.right)
    return tree


def swap_children(node):
    temp = node.right
    node.right = node.left
    node.left = temp