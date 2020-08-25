

class LLNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def print_list(self):
        print(self.val, end=" ")
        if self.next:
            self.next.print_list()
        else:
            print()


"""
Sort linked list in O(nlogn) time with O(1) space
This is simply a merge sort where we keep splitting the problem size in
half. At each row of the recursion tree we do O(n) amount of work
in the conquer step of the LL' comprehension. There are O(logn) rows
in the recursion tree because we split the problem size in half
each time.

I think the understanding of the problem is pretty intuitive, but
doing it might be a litt more tough. I wrote two helper functions to
help me do this problem. The first one splits a linked list in
half. The second one solves the brute force sort for mea and returns
the list. Finding the middle of a linked list is simply done by
using fast and slow pointers. As long as one is moving twice as
fast as the other it will cover twice the distance, so we know we're
at halfway when the fast pointer can no longer move two steps ahead
"""


def sort_LL(head: LLNode) -> LLNode:
    return merge_srot(head)

def merge_srot(head: LLNode) -> LLNode:
    # length of one or 2
    if not head.next or not head.next.next:
        return brute_force_sort(head)

    # split in hald and call merge sort on both halves
    split_left, split_right = split_ll(head)
    left_sorted = merge_srot(split_left)
    right_sorted = merge_srot(split_right)

    # conquer both halves into one list and retunr the list
    sorted_ll = None
    sorted_ll_last = None

    # while there are still elements in both lsits
    while left_sorted and right_sorted:
        smallest_node = None

        # get the smallest node from the two lists
        if left_sorted.val < right_sorted.val:
            smallest_node = left_sorted
            left_sorted = left_sorted.next
        else:
            smallest_node = right_sorted
            right_sorted = right_sorted.next
        
        # remove the smallest node from on eof ht elists
        smallest_node.next = None

        # add the smallest node to the new list
        if not sorted_ll_last:
            sorted_ll = smallest_node
            sorted_ll_last = smallest_node
        else:
            sorted_ll_last.next = smallest_node
            sorted_ll_last = smallest_node

    # add remaining elements
    if left_sorted:
        sorted_ll_last.next = left_sorted
    
    if right_sorted:
        sorted_ll_last.next = right_sorted

    return sorted_ll



def split_ll(head: LLNode):
    list1 = head

    # create fast and slow pointers
    fast = slow = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    # create list 2
    list2 = slow.next

    # split the lsits
    slow.next = None

    return (list1, list2)

def brute_force_sort(head: LLNode) -> LLNode:
    node1 = head
    node2 = head.next

    if not node2:
        return node1

    smaller_val = node1.val if node1.val < node2.val else node2.val
    larger_val = node1.val if node1.val > node2.val else node2.val

    # assign the values
    node1.val = smaller_val
    node2.val = larger_val
    return node1



ll = LLNode(1, LLNode(8, LLNode(3, LLNode(5, LLNode(7, LLNode(9, LLNode(2)))))))

sorted_ll = sort_LL(ll)

print("sorted list: ", end="")
sorted_ll.print_list()