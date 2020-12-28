# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个完整的基于数组的双端队列的实现方法(不限制大小)
"""

class EmptyError(Exception):
    pass

class Deque:

    CAPACITY = 5

    def __init__(self):
        self._data = [None]*Deque.CAPACITY

        self._head = 0
        self._count = 0

    def empty(self):
        return self._count == 0

    def resize(self, c):
        data2 = [None]*c
        head2 = 0

        for i in range(self._count):
            data2[(head2+1+i) % c] = self._data[(self._head+1+i) % len(self._data)]

        self._data = data2
        self._head = head2

    def append_right(self, e):

        if self._count == len(self._data):
            self.resize(2*len(self._data))

        self._data[(self._head+1+self._count) % len(self._data)] = e

        self._count += 1

    def right(self):
        if self.empty():
            raise EmptyError

        return self._data[(self._head+self._count) % len(self._data)]

    def pop_right(self):
        if self.empty():
            raise EmptyError

        pos = (self._head+self._count) % len(self._data)

        res = self._data[pos]
        self._data[pos] = None

        self._count -= 1

        return res

    def append_left(self, e):
        if self._count == len(self._data):
            self.resize(2*len(self._data))

        self._data[self._head] = e

        self._head = (self._head-1) % len(self._data)

        self._count += 1

    def left(self):
        if self.empty():
            raise EmptyError

        return self._data[(self._head+1) % len(self._data)]

    def pop_left(self):
        if self.empty():
            raise EmptyError

        res = self._data[(self._head+1) % len(self._data)]

        self._data[(self._head+1) % len(self._data)] = None
        self._head = (self._head+1) % len(self._data)

        self._count -= 1

        return res

    def show(self):
        print(self._data, self._head)

dq = Deque(); dq.show()

dq.append_left(1); dq.show()
dq.append_right(2); dq.show()
dq.append_right(3); dq.show()
dq.append_left(4); dq.show()
print(dq.left())
print(dq.right())
print(dq.pop_left()); dq.show()
print(dq.pop_right()); dq.show()
dq.append_left(5); dq.show()
dq.append_left(5); dq.show()
dq.append_left(5); dq.show()
# dq.append_left(6); dq.show()
dq.append_right(6); dq.show()