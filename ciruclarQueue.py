# leetcode problem 622
# Design your implementation of the circular queue.
# The circular queue is a linear data structure in which the operations are performed based on FIFO
# (First In First Out) principle and the last position is connected back to the first position to make a circle.
# It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
# In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the queue.
# But using the circular queue, we can use the space to store new values.

# Your implementation should support following operations:

# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.

# the key to implementing a ciruclar queue is that there are n positions, but there are n+2 states
# if there were n+1 states, that would be fine, but we need to allow for the other state
# (i.e. if back is one space behind front, is it full or empty?)
# as a result of this, you want to add an extra space to the underlying array in your implementation
# if the back is now one less than the front, then we know the queue is empty, and if the back is
# two less than the front, then we know the queue is full

# the last implementation detail is that it's CIRUCLAR. As a result, we need to be using the mod function
# when we're incrementing value that represent the front and back index. This will ensure the values
# "wrap around" the queue. Once you understand these concepts, the rest becomes trivial.

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.back = -1
        self.front = 0
        self.size = k + 1  # use an extra space to tell teh different between empty and full
        self.queue = [0] * self.size

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.back = (self.back + 1) % self.size
            self.queue[self.back] = value
            return True
        return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.queue[self.back]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if (self.back + 1) % self.size == self.front:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (self.back + 2) % self.size == self.front:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()