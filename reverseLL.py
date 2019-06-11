# This is one of the more classic interview problems that I've seen
# Not only have I seen this in various interviews, but it's come up in
# some of my data structures class. I feel like this is one of those
# early right of passage problems. It's not hard, but it can be tough to wrap
# your head around. Even if you've done this problem before, you really need
# to think about what you're doing or else you can get caught up in this
# Null trap. Don't do that!

# the main topic for this problem is RUNNERS. So what is a runner,
# A runner is a pointer that moves down the list ahead of others.
# this will then help you solve linked list problems in O(n) time
# instead of O(n^2). So whenever you get to a LL problem and it involves
# moving nodes around, think about using runners. Most of the time, it will
# require 3 pointers with LL problems (two to do the work and then one
# to keep track of the work) but it's all problem specific so take
# that with a grain of salt.

# okay, first things first, let's think about what's happening here
# at a simple case (IE, in the middle of the list)
# we want to get the current node to point to the previous node.
# so we can do that by just moving the current nodes next to previous
# and we're done right? WRONG. If you do that you will lose track of the
# rest of the list. You need to also keep track of a next runner
# that will maintain the next node for curr to go to after you
# have "rotated" curr to point to the one before it.
# lastly, it helps me to think as if there was another LL called
# reveresed, and we will append to the front of this LL
# so we're indirectly reversing it. Thinking of it as previous
# trips me up, but if that's what is best for you then do that!
from Node import Node

def reverse_LL(head):
    curr = None  # start curr one behind next
    rev = None  # start rev at None incase there is no nodes
    nxt = head  # start nxt at the front, we will assume we move to next immediately
    while nxt:
        curr = nxt  # go to the current one
        nxt = nxt.next  # move it down
        curr.next = rev  # reverse it
        rev = curr  # get rev to point to the new front
    return rev


# build the list backwards
a = Node('a')
b = Node('b', a)
c = Node('c', b)
r = reverse_LL(c)

while r:
    print(r.data)
    r = r.next

