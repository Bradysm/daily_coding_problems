# This problem was asked by Google.
# Given a singly linked list and an integer k, remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively expensive.
# Do this in constant space and in one pass.

"""
Immediately when I see a linked list problem that requires one pass, I automatically
think about using "runners". I define runners as pointers that move down the
list and point to nodes that are needed. As you move down the list, they "run" down
the list with you. So, let's first look at this problem as if we were removing the
kth element from the list, that is simple, we move a runner down to the kth node
and remove that from the list. Okay, that was easy! Now we need to remove the kth
element from the END of the list. So, we just created a distance k from the front
of the list to remove the kth element from the front, if we can maintain that
distance k from the back of the list, then we can remove the kth from the back.

This is where runners come into play. We want to have two runners, the first runner
will go a distance k from the front of the list and then stop. The second runner
will start once the first runner gets to k. they will then move one step at a time
in sychrony until the first runner reaches the end of the list. Since the two runners
were a distance k apart from eachother, this distance will be maintained and now
the SECOND runner will be a distance K from the end of the list. We can then remove
the node from the list and BAMMMM. You've just removed the kth node from the end of the LL.
"""


class Node:
    """
    node class used to create a linked list
    """
    def __init__(self, val=0, n=None):
        self.val = val
        self.n = n

    def g_n(self):
        return self.n

    def g_val(self):
        return self.val

    def set_n(self, node):
        self.n = node

    def set_val(self, val):
        self.val = val


def remove_k_end(head, k):
    """
    Removes the kth node from the linked list
    :param head: linked list
    :param k: position to remove from the ll
    """
    rem = head
    kth = head
    # get to the kth pos
    while k > 0:
        kth = kth.g_n()
        k -= 1

    while kth.g_n() is not None:
        kth = kth.g_n()
        rem = rem.g_n()

    # remove it, and return head
    rem.set_n(rem.g_n().g_n())
    return head


# testing to make sure it works
# create the ll
ll = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None)))))))

curr = remove_k_end(ll, 2)
while curr is not None:
    print(curr.g_val())
    curr = curr.g_n()

