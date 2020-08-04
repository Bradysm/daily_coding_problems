"""
Hi, here's your problem today. This problem was recently asked by Twitter:
Given a linked list, remove all duplicate values from the linked list.
For instance, given 1 -> 2 -> 3 -> 3 -> 4, then we wish to return the linked list 1 -> 2 -> 4.


Essentially what we do here is run though the list, get a set of the duplicate
elements within the list, so when we pass through it a second time, we see if that
current value is a duplicate, if so, then we remove it from the list. So we make two
passes, one to get the duplicates, and one to remove the duplicates from the list

O(n) time and space
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        return str(self.val) + " " + str(self.next)


def remove_duplicate_nodes(head:Node):
    duplicates = get_duplicates(head)
    prev = None
    curr = head

    # while there are more nodes to process
    while curr is not None:
        # check to see if curr is in seen
        if curr.val in duplicates:
            # remove curr from the list
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next


def get_duplicates(head:Node) -> set:
    seen = set()
    has_duplicates = set()
    
    curr = head
    while curr is not None:
        # check to see if it's in seen
        if curr.val not in seen:
            seen.add(curr.val)
        else:
            has_duplicates.add(curr.val)

        curr = curr.next

    return has_duplicates


n = Node(1, Node(2, Node(3, Node(3, Node(4)))))
n2 = Node(1, Node(2, Node(3, Node(3, Node(4, Node(2))))))

# 1 2 3 3 4
print("List 1 before:",n)
remove_duplicate_nodes(n)
print(n)

print("List 2 before:", n2)
remove_duplicate_nodes(n2)
print(n2)



