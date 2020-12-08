# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在一个初始空的双端队列里执行下面操作, 结果是什么
"""

class EmptyError(Exception):
    pass

class FullError(Exception):
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

    def resize(self, c):
        data2 = [None]*c
        head2 = 0

        for i in range(len(self)):

            data2[(head2+1+i)%c] = self._data[(self._head+1+i)%len(self._data)]

        self._data = data2
        self._head = head2

    def add_left(self, e):

        if len(self) == len(self._data):
            self.resize(len(self._data)*2)

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

        k = (self._head+1) % len(self._data)
        res = self._data[k]
        self._data[k] = None
        self._head = k
        self._count -= 1

        if self._count <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def add_right(self, e):
        if len(self) == len(self._data):
            self.resize(len(self._data)*2)

        k = (self._head+1+len(self)) % len(self._data)

        self._data[k] = e

        self._count += 1

    def right(self):

        if self.empty():
            raise EmptyError

        return self._data[(self._head+len(self)) % len(self._data)]

    def pop_right(self):

        if self.empty():
            raise EmptyError

        k = (self._head+len(self)) % len(self._data)
        res = self._data[k]

        self._data[k] = None

        self._count -= 1

        if len(self) <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def show(self):
        print(self._data, self._head)


dq = Deque()

dq.add_left(4); dq.show()
dq.add_right(8); dq.show()
dq.add_right(9); dq.show()
dq.add_left(5); dq.show()
print(dq.right())
dq.pop_left(); dq.show()
dq.pop_right(); dq.show()
dq.add_right(7); dq.show()
print(dq.left())
print(dq.right())
dq.add_right(6); dq.show()
dq.pop_left(); dq.show()
dq.pop_left(); dq.show()
