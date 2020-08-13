"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Yelp.

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal distance. 
If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.



Here's my logic, we want to go through the tree in a level order, and then keep a dictionary
that will have the key be the horizontal distance and the value be the node that is at the lowest
point in the tree with that horizontal value. Then once we traverse the whole tree, we can sort the
dictionary based on the keys, and then map the array to the values, which whill be the nodes.

The reason we want to do a level order traversal is that we can use that to our advantage that when
we come across a new node with the same horizontal distance, since we can use it to our advantage that
the node at that same horizontal distance must have came before this current node or is on the same level.
As a result, we can simplt write over that in our dictionary!

Great! This will run in O(nlogn) time and O(n) space. This is because in the worst case, when the tree is full
then we will have half the number of nodes in the last level, this will then mean that the number of nodes
in the bottom view will be proportional to the total number of nodes in the tree, and thus, will be linearly
correlated to n, so the sorting time will still be upper bounded by O(nlogn)

Also, in the queue, we will store the node and the horizontal distance in a tuple
This will then allow us to update the bottom view dictionary as we will have the horizontal distnace
of the current node.
"""
from tree import Tree



def bottom_view_tree(root: Tree) -> list:
    # dictionary to store the horizontal distances
    horizontal_distances = {}
    queue = [] if not root else [(root, 0)] # (node, hd)

    # get the lowest horizontal distances
    while queue:
        # get the current node
        node, hd = queue.pop()

        # update the horiztonal distances dictionary
        horizontal_distances[hd] = node.value

        # add the children
        if node.right: queue.append((node.right, hd + 1))
        if node.left: queue.append((node.left, hd - 1))
        

    
    # sort by hd, and then map to the value using a list comprehension
    return [v for k, v in sorted(horizontal_distances.items(), key=lambda x: x[0])]


test_tree = Tree(5, Tree(7, Tree(9,left=Tree(8)), left=Tree(6)), left=Tree(3, Tree(4), left=Tree(1, left=Tree(0))))


print(bottom_view_tree(test_tree))