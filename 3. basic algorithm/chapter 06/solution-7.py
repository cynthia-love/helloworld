# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    队列实现改进方法1-以空间换时间
    关键思路是绕开pop(0)的O(n), pop(0)方法改为队首指针后移

    缺点: 队首出去的元素在底层存储上并没出去, 还在数组里
    随着时间的推移, 数组会越来越大

"""

class EmptyError(Exception):
    pass

class Queue:
    """FIFO queue implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty queue
        Head pointer pointed to -1 (始终指向队首的前一个位置)
        """
        self._data = list()
        self._head = -1

    def __len__(self):
        """Return the number of element in the queue"""
        return len(self._data)-1-self._head

    def empty(self):
        """Return True if the queue is empty"""
        return len(self) == 0

    def enqueue(self, e):
        """Add an element to the back of queue"""
        self._data.append(e)

    def dequeue(self):
        """Remove and return the first element of queue
        Raise Empty Exception if the queue is empty"""

        if self.empty():
            raise EmptyError('Queue is empty')

        self._head += 1

        return self._data[self._head]

    def first(self):
        """Return (but do not remove) the element at the front of the queue
        Raise Empty Exception if the queue is empty"""

        if self.empty():
            raise EmptyError('Queue is empty')

        return self._data[self._head+1]

    def __str__(self):
        return ', '.join(str(e) for e in self._data[self._head+1: len(self._data)])

q = Queue()
q.enqueue(5); print(q)

q.enqueue(3); print(q)
print(len(q))

q.dequeue(); print(q)
print(q.empty())

q.dequeue(); print(q)
print(q.empty())

# q.dequeue()

q.enqueue(7)
q.enqueue(9)
print(q.first())

q.enqueue(4); print(len(q))

q.dequeue(); print(q)