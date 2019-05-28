# This problem was asked by Apple.

# Implement a queue using two stacks.
# Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
# enqueue, which inserts an element into the queue, and dequeue, which removes it.

# there are three cases, the stacks are empty, stack 1 has the front, or stack 2 has the front
# the way that I am thinking about this problem is that when we enqueue, we add to the stack
# that does not contain the element at the front of the queue. So this will then place all
# of the elements in the second stack in reverse order from how we want them. When we dequeue,
# we will remove from the stack that has one element and then move all of the elements from
# the second queue over to the queue that just had the top, EXCEPT WE LEAVE ONE ELEMENT. This
# element will now be the front of the queue.


class Queue:
    def __init__(self):
        """
        Initializes the queue using two stacks
        s1: stack 1
        s2: stack 2
        empty: defines if the queue is empty (could check instead of using this space)
        """
        self.s1 = list()
        self.s2 = list()
        self.s1Top = True

    def enqueue(self, obj):
        """
        enqueues the obj into the back of the queue
        :param obj: object to be enqueued
        """
        # both are empty or  s2 is top, set s1 to top incase empty
        if self.empty():
            self.s1Top = True
            self.s1.append(obj)
        elif self.s1Top:
            self.s2.append(obj)
        else:
            self.s1.append(obj)

    def dequeue(self):
        """
        dequeues the next element from the queue. If the queue is empty,
        then None is returned, else, the front element is returned
        :return: Object at the front of the queue
        """
        obj = None
        if not self.empty():
            # decide how to swap
            if self.s1Top:
                obj = self.__swap_stacks(self.s2, self.s1)
                self.s1Top = False
            else:
                obj = self.__swap_stacks(self.s1, self.s2)
                self.s1Top = True
        return obj

    def empty(self):
        """
        checks to see if the queue is empty
        :return: True if empty, False otherwise
        """
        return not(len(self.s1) or len(self.s2))

    def __swap_stacks(self, filledStack, topStack):
        """
        swaps the stacks by moving all of the elements to the other stack and returning
        the top of the topStack initially
        :param filledStack: stack that is filled with the elements
        :param newStack: stack to be filled
        :return: the top
        """
        obj = topStack.pop()
        while len(filledStack) > 1:
            topStack.append(filledStack.pop())
        return obj


# test the queue
q = Queue()


# test enqueue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# test dequeue
print(q.dequeue())
print(q.dequeue())

# enqueue some more
q.enqueue(4)
q.enqueue(5)

# dequeue the rest
while not q.empty():
    print(q.dequeue())

# try to remove from an empty queue
print("this should be none: ", q.dequeue())

# add to the empty queue
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)

# remove the last
while not q.empty():
    print(q.dequeue())


