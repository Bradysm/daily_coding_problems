# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.


# immediately, when I saw this problem, I knew what I needed to do, and there is a naive brute force solution
# that most people think of when they first see this problem. Naively people think of just iterating through
# all off the lists first node, and then picking the min out of those and then point to that node with the
# the pointer of the list being returned. Although this is easy and simple, the time complexity for this
# is enormous. This is because each time you pick the next smallest node, you have to go through ALL OF THE LISTS!!

# what if there was a way that we could utilize the fact that all of the lists are sorted, and initially
# go through each list once, but never have to iterate through all of them again just to find the next smallest

# The idea that I am talking about is building a heap of size k and running through all of the lists initally
# and adding the first node to the heap with an integer representing which list that this node came from.
# Once you've added the first node to the array, you will then build the min heap which takes O(k) time because
# there are k numbers. (If you need a refresher on that time complexity, I recommend you looking into heaps
# before continuing). Once we have the min heap built, we can then pop off the min value, and add the
# next node from that list that it came from (which takesn O(logk) time and then continue this process
# until all of the list pointers are at Null. We now have used a mergesort to merge all of the lists
# together in O(max(listsize)k) time and O(k) space. Much better than the niave version!!!!

# also note that I ma using heapreplace instead of heap.pop then heap.push. This is because each
# of those methods will take log(k) time whereas replace will take log(k) time.

# since I am not to sure of the input, I am assuming that the lists are given using an array that points to their
# head node.
from Node import Node # this will be used to build the LL
import heapq

def merge_k_lists(lists):
    """
    Merges k sorted lists into one sorted lists
    :param lists: array of linked lists
    :return: sorted LinkedList
    """
    heap = list() # create an array of size k
    for i, n in enumerate(lists):
        heap.append((n.data, n, i))

    # build the min heap, and create list to return
    heapq.heapify(heap)
    head = None
    curr = None

    # continue removing and adding until correct
    while len(heap) > 0:
        val, minnode, arr_i,  = heap[0]  # peak the smallest
        lists[arr_i] = lists[arr_i].next  # move the current node down
        n = lists[arr_i]  # node to be added to the heap
        minnode.next = None  # set next to none so it's no longer a part of the prev list
        # add it to the new list
        if head is None:
            head = minnode
            curr = head
        else:
            curr.next = minnode
            curr = minnode

        heapq.heapreplace(heap, (n.data, n, arr_i)) if n is not None else heapq.heappop(heap)

    return head


# lists to test the solution
list_a = Node(1, Node(5, Node(7)))
list_b = Node(2, Node(3, Node(4)))
list_c = Node(6, Node(10, Node(15, Node(20))))

l = [list_a, list_b, list_c]

new_head = merge_k_lists(l)
while new_head is not None:
    print(new_head.data)
    new_head = new_head.next

print('\ntesting on a single list:')
list_a = Node(1, Node(5, Node(7)))
new_head = merge_k_lists([list_a])
while new_head is not None:
    print(new_head.data)
    new_head = new_head.next


