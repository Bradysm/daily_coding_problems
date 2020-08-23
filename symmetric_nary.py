class Node:
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root):
    stack = create_stack(root)
    symmetric = check_roots_symmertric(root)


    while stack and symmetric:
        # do something
        node1, node2 = stack.pop()
        symmetric = check_roots_symmertric(node1, node2)
        stack += create_stack(node1, node2)

    return symmetric


def check_roots_symmertric(root1, root2=None):
    root1_children = root1.children

    # check to see if it's the center of a a new tree
    root2_children = root2.children if root2 else root1_children
    
    symmetric = True if len(root2_children) == len(root1_children) else False

    # check to see if the children are symmetric
    for node1, node2 in zip(reversed(root1_children), root2_children):
        if node1.value is not node2.value:
            symmetric = False
            break

    return symmetric

def create_stack(root, root2=None):
    stack = []

    # create iteration
    children1 = root.children
    children2 = reversed(root2.children if root2 else root.children)


    # create tuple children up to the middle (middle)
    for child1, child2 in zip(children1, children2):
        stack.append((child1, child2))

    return stack


tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1, children=[Node(2)])]
tree.children[1].children = [Node(1, children=[Node(2)]), Node(4), Node(9)]

# true
print(is_symmetric(tree))

# add an extra node, should be false
tree.children[0].children = [Node(9), Node(4), Node(1, children=[Node(2), Node(3)])]
print(is_symmetric(tree))