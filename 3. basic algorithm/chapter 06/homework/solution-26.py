# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    再写一遍双端队列实现
"""

class EmptyError(Exception):
    pass

class Deque:
    CAPACITY = 5

    def __init__(self):
        self._data = [None]*Deque.CAPACITY
        self._head = 0
        self._count = 0

    def __len__(self):
        return self._count

    def empty(self):
        return len(self) == 0

    def add_left(self, e):
        if self._count == len(self._data):
            self.resize(len(self._data)*2)

        self._data[self._head] = e

        self._head = (self._head-1) % len(self._data)

        self._count += 1

    def pop_left(self):
        if self.empty():
            raise EmptyError

        res = self._data[(self._head+1) % len(self._data)]

        self._data[(self._head + 1) % len(self._data)] = None

        self._head = (self._head+1) % len(self._data)

        self._count -= 1

        if self._count <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def left(self):
        if self.empty():
            raise EmptyError

        return self._data[(self._head+1) % len(self._data)]

    def add_right(self, e):
        if self._count == len(self._data):
            self.resize(len(self._data)*2)

        self._data[(self._head+1+self._count) % len(self._data)] = e

        self._count += 1

    def pop_right(self):
        if self.empty():
            raise EmptyError

        res = self._data[(self._head+self._count) % len(self._data)]
        self._data[(self._head + self._count) % len(self._data)] = None

        self._count -= 1

        if self._count <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def right(self):
        if self.empty():
            raise EmptyError

        return self._data[(self._head+self._count) % len(self._data)]

    def resize(self, c):
        data2 = [None]*c
        head2 = 0

        for i in range(self._count):

            data2[(head2+1+i) % c] = self._data[(self._head+1+i) % len(self._data)]

        self._data = data2
        self._head = head2

    def show(self):
        print(self._data)

dq = Deque()

dq.add_right(5); dq.show()
dq.add_left(3); dq.show()
dq.add_left(7); dq.show()
print(dq.left())
dq.pop_right(); dq.show()
print(len(dq))
dq.pop_right(); dq.show()
dq.pop_right(); dq.show()
dq.add_left(6); dq.show()
print(dq.right())
dq.add_left(8); dq.show()
print(dq.empty())
print(dq.right())

