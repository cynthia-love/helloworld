# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现队列的rotate操作, 它的执行效率应该比分别调dequeue和enqueue高
"""

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Queue:

    def __init__(self, c):
        self._data = [None]*c
        self._head = 0
        self._count = 0

    def __len__(self):
        return self._count

    def enqueue(self, e):
        if len(self) == len(self._data):
            raise FullError

        self._data[(self._head+1+self._count) % len(self._data)] = e

        self._count += 1

    def dequeue(self):
        if len(self) == 0:
            raise EmptyError

        res = self._data[(self._head+1) % len(self._data)]
        self._data[(self._head + 1) % len(self._data)] = None

        self._head = (self._head + 1) % len(self._data)

        self._count -= 1

        return res

    def rotate(self, x):
        for i in range(x):
            l = (self._head+1) % len(self._data)
            r = (self._head+1+self._count) % len(self._data)

            self._data[r], self._data[l] = self._data[l], None

            self._head += 1

    def show(self):
        print(self._data)

q = Queue(5)

q.enqueue(1); q.show()
q.enqueue(2); q.show()
q.dequeue(); q.show()
q.enqueue(3); q.show()
q.enqueue(4); q.show()
q.rotate(1); q.show()
q.rotate(3); q.show()
