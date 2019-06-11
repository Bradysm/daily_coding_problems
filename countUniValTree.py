# count the number of unival trees
# these are trees where nodes under it have the same value


# the key to this problem is to think of this recursion from the bottom up
# if you don't and you check from the top down, you will be evaluating
# every subtree multiple times. Instead, we can think of this from the bottom
# up and check if the bottom is a uni tree, and then bump up to the next level
# and check to see if that is a universal tree. The parent of the two nodes
# will only be a universal tree if the two nodes below it are universal trees
# so we can make the check at the solely below it because we've already checked
# everything below those two children (so we've inductively proven it already).
# lastly, we need to think of the null case. When we reach null, we want to
# not count a uni tree, but we want to give the parent of the null ptr to still
# have the opportunity to be a uni tree (you will see why this is important)

# so, if we think of this first, we cannot decide whether a node is a uni
# tree based on the number of uni trees below it. Maybe the child of the parent
# wasnt a uni tree, but there were 100's of uni trees below that child. Although
# there might have been 100's of uni trees, we cannot determine that this parent
# is a unitree or not. Instead, we must also pass back a value with the total
# number of uni trees. To do this, we will pass back a boolean value that will
# represent whether this node was a uni tree. We can then make the decision at the
# parent of whether this one was a unitree or not based on the boolean
# and checking to see if the numbers match. This will run in O(n) time and
# will take extra space since we're adding to the stack for each call O(logn) assuming
# the tree is balanced, and O(n) extra space if there is no balance constraint.

def unival(root):
    num, _ = unival_help(root)
    return num


def unival_help(root):
    if root is None: return 0, True  # check the base case
    total = 0  # total number of uni trees
    uni = True  # represent whether current parent is a uni tree
    if root.left:   # check the left
        ltotal, luni = unival_help(root.left)
        uni = (luni and uni) and (root.val == root.left.val)  # check to see if still valid
        total += ltotal
    if root.right:  # check the right
        rtotal, runi = unival_help(root.left)
        uni = (runi and uni) and (root.val == root.right.val)  # check to see if still valid
        total += rtotal
    return total + 1 if uni else total, uni
