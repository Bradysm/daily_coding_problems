# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list,
# we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
# If pos is -1, then there is no cycle in the linked list.


# This might be one of the weirdest cycle problems that I've ever seen. Most cycle problems, you
# can run something like a fast slow and if they ever meet than you know you have a cycle,
# you could also do the HashSet where you hash the actual node itself and not just the value
# so when you see that object again, you know you have a cycle in the LL

# The thin that threw me off was the position, I still really don't understand it so I just put a flag
# to check if that position was correct or not. I then just compared to see if I have seen that object
# or not using a set. Sets are implemented using hashing so this allows for theoretical O(1) lookup
# (depending on the collisions and resolution). If we see that current node in the set, then
# we know there is a cycle; return False. Otherwise, if head turns into None, return True. Super easy,
# but a very common problem!


def hasCycle(head, pos):
    """
    :type head: ListNode
    :type pos: int
    :rtype: bool
    """
    if pos == -1: return False
    seen = set()
    while head is not None:
        if head in seen:
            return False
        else:
            seen.add(head)
        head = head.next
    return True
