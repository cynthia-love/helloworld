# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用collection.deque实现队列
"""
from collections import deque

class EmptyError(Exception):
    pass

class Queue:

    def __init__(self):

        self._data = deque()

    def __len__(self):
        return len(self._data)

    def empty(self):
        return len(self) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.empty():
            raise EmptyError
        return self._data.popleft()

    def first(self):
        if self.empty():
            raise EmptyError

        return self._data[0]

    def show(self):
        print(self._data)

q = Queue()

q.enqueue(5); q.show()
q.enqueue(3); q.show()
q.dequeue(); q.show()
q.dequeue(); q.show()

# q.dequeue()

q.enqueue(7); q.show()
q.enqueue(9); q.show()
print(q.first())

q.enqueue(4); q.show()

q.dequeue(); q.show()