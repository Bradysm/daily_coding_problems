from tree import Tree  # used for tree nodes


def pre_and_inorder_build(preorder: list, inorder: list) -> Tree:
    if not preorder and not inorder: return None  # check to see when there are no roots left
    if len(preorder) == 1 and len(inorder) == 1: return preorder[0]
    root = Tree(preorder[0]) # get the value from it
    i = inorder.index(root)  # get the index within inorder that val is at, this will split the list
    root.left = pre_and_inorder_build(preorder[1:1+i], inorder[0:i]) # ()
    root.right = pre_and_inorder_build(preorder[1+i:], inorder[i+1:]) # (i+1-end of list)


