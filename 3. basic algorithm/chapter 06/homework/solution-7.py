# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在一个空队列上执行下面一系列操作, 结果是什么

    队列用 可扩展/缩小的循环数组 实现
"""

class EmptyError(Exception):
    pass

class Queue:

    CAPACITY = 5

    def __init__(self):

        self._data = [None] * Queue.CAPACITY

        self._head = 0

        self._count = 0

    def __len__(self):

        return self._count

    def empty(self):

        return len(self) == 0

    def resize(self, c):

        data2 = [None] * c
        head2 = 0

        for i in range(self._count):

            data2[(head2+1+i) % c] = self._data[(self._head+1+i) % len(self._data)]

        self._data = data2
        self._head = head2

    def enqueue(self, e):

        if len(self) == len(self._data):

            self.resize(len(self._data)*2)

        self._data[(self._head+1+self._count) % len(self._data)] = e

        self._count += 1

    def dequeue(self):

        if self.empty():
            raise EmptyError

        head2 = (self._head+1) % len(self._data)
        res = self._data[head2]
        self._data[head2] = None

        self._head = head2

        self._count -= 1

        if self._count <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def first(self):

        if self.empty():
            raise EmptyError

        return self._data[(self._head+1) % len(self._data)]

    def show(self):
        print([self._data[(self._head+1+i) % len(self._data)] for i in range(self._count)])

q = Queue()

q.enqueue(5); q.show()
q.enqueue(3); q.show()
q.dequeue(); q.show()
q.enqueue(2); q.show()
q.enqueue(8); q.show()
q.dequeue(); q.show()
q.dequeue(); q.show()
q.enqueue(9); q.show()
q.enqueue(1); q.show()
q.dequeue(); q.show()
q.enqueue(7); q.show()
q.enqueue(6); q.show()
q.dequeue(); q.show()
q.dequeue(); q.show()
q.enqueue(4); q.show()
q.dequeue(); q.show()
q.dequeue(); q.show()