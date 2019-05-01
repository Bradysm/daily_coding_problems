# adding two linked lists together that represent numbers
# if we were given 99 and 25
# 9 -> 9
# 5 -> 2
# return 1 -> 2 -> 4

from Node import Node

"""
Below is my original solution. This will run in O(max(m,n)) time
but will take two passes through the list to complete. The first pass
returns the pointer to the longest list, and the second pass 
performs the actual addition of the numbers. The reson I first found
the longest list is because it saved from a lot of edge cases revolving
around adding to the end of the list and expanding.

We could've also done this by breaking down the problem node by
node and then recursively solving it. The second implementation
is provided below. The second implementation only requires one
pass.
"""
def longest(l1, l2):
    l1curr = l1
    l2curr = l2
    while l1 is not None and l2 is not None:
        l1 = l1.next
        l2 = l2.next
    return (l2curr, l1curr) if l1 is None else (l1curr, l2curr)


def add_numbers(num1, num2):
    """
    Adds two numbers together
    :param num1: number created with a linked list
    :param num2: number created with a linked list
    :return: linked list representing a new number
    """
    num1, num2 = longest(num1, num2)
    new_num = num1
    # check to see if we're on the last node
    while num1 is not None and num2 is not None:
        num1.data = num1.data + num2.data
        if num1.data > 9:
            tens = num1.data / 10
            num1.data = num1.data % 10
            num1.next = Node(tens+num1.next.data, num1.next.next) if num1.next else Node(tens)
        # move to next digit
        num1 = num1.next
        num2 = num2.next
    return new_num


def add(node1, node2, carry=0):
    """
    returns a list comprised of the linked lists
    :param node1: head of list 1
    :param node2: head of list 2
    :param carry: carry digit
    :return: ll containing number
    """
    if not node1 and not node2 and not carry:
        return None
    # get the digits
    dig1 = node1.data if node1 else 0
    dig2 = node2.data if node2 else 0
    total = dig1 + dig2 + carry
    # move down the list of possible
    node2 = node2.next if node2 else None
    node1 = node1.next if node1 else None

    return Node(total % 10, add(node1, node2, total / 10))


def print_num(node):
    if not node: return
    print_num(node.next)
    print(node.data)

# testing for first method
number1 = Node(9, Node(9, Node(1)))
number2 = Node(5, Node(8, Node(3)))
print_num(add_numbers(number1, number2))

print("\nnextNumber:\n")

number1 = Node(9, Node(9, Node(1)))
number2 = Node(5, Node(8, Node(3)))
print_num(add(number1, number2))

