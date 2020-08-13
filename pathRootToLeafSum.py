
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def is_leaf(self):
        return False if self.left or self.right else True
 

"""
For this problem, since we're moving from the top to the tree to
the bottom, I immedietaly thought of using a DFS from the top to the
bottom. Then as we move through the nodes, we will keep track of the
sum up to that node. Then when we get to a leaf, we will check to see
if the sum is equal to the target sum. Once the stack is empty,
then we know that there is no possible way to create the sum so we
return False. This will happen in O(n) time where n is the number of
nodes because we need to check all possible paths from the root
to the leafs, and then the space will be 

"""

def target_sum_bst(root, target):
    stack = [] if not root else [(root, 0)] # (curr node, current sum)

    while stack:
        curr_node, curr_sum = stack.pop()
        new_sum = curr_sum + curr_node.value

        # if we're at a leaf and the current
        if curr_node.is_leaf() and new_sum == target: 
            return True
        
        if curr_node.left: stack.append((curr_node.left, new_sum))
        if curr_node.right: stack.append((curr_node.right, new_sum))

    return False

#      1
#    /   \
#   2     3
#    \     \
#     6     4
n6 = Node(6)
n4 = Node(4)
n3 = Node(3, None, n4)
n2 = Node(2, None, n6)
n1 = Node(1, n2, n3)

print(target_sum_bst(n1, 9))
# True