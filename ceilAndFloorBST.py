# given the root to a BST and a key k, find the ceil and floor of the BST corresponding to k
# The ceil of the BST for value k means the smallest number that is greater than or equal to k
# and the floor being the largest number that is less than or equal to k

# So when I get a problem with a BST, you know that you are making decisions based on the sorted order
# of the tree. FOr this problem, it means that we're making decisions based on the path that we will follow
# leading to k within the tree. What happens if k is in the tree? Well this would be simple, we would follow
# the path leading to k, by making deciions based on whether the current value at the node we're at is
# >= or < the value of k. Based on that, we then move in the correct direction and keep this moving. 
# once we get to k, we make floor and ceil equal to the node with k and call it a day.

# what happens if k is not in the tree though? THis is a more challenging, yet not too complicated version
# of checking for a BST in my opinion. When you check to see if a BST is valid, you use a range that you pass
# down throughout the tree. When you pass ceil and floor down with the recurisve calls, you're indirectly
# passing this range down with the recursive call! So what do we do with the range? Well we want to converge
# the range onto the number k because we want the number that is closest to k on both sides of K! SO,
# if we're at a number > k and that is < ceil, then we make ceil point to that
# node because it makes the range tighter to K!!!!! See, that's not too bad. We then continue acting in the
# way that we're searching for K, and continue updating the range until we get to k, or until we get to a leaf in
# the tree. Once we get to a leaf in the tree, we return the value.

from tree import Tree


def floor_and_ceil(root: Tree, k: int, ceil: Tree, floor: Tree):
    if root is None: return ceil, floor
    if root.value == k: # we found 
        return root, root
    elif root.value > k: # current value is greater than root
        ceil = root if (ceil is None or root.value < ceil.value) else ceil
        return floor_and_ceil(root.left, k, ceil, floor)
    else: # current value is < root
        floor = root if (floor is None or root.value > floor.value) else floor
        return floor_and_ceil(root.right, k, ceil, floor)
    

tree = Tree(10, Tree(20, Tree(31), Tree(19)), Tree(4, Tree(7, Tree(9), Tree(5)), Tree(3, None, Tree(1))))

this_ceil, this_floor = floor_and_ceil(tree, 6, None, None)
print('ceil val:', this_ceil.value)
print('floor val:', this_floor.value)