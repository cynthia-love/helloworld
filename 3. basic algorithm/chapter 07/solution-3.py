# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    用单向链表实现队列
"""

class EmptyError(Exception):
    pass

class Queue:

    class _Node:

        __slots__ = ['e', 'next']

        def __init__(self, e=None):

            self.e = e
            self.next = None

    def __init__(self):

        self._head = self._Node()

        # 为空时, 尾指针指向头结点, 方便插入逻辑统一
        self._tail = self._head

        self._c = 0

    def empty(self):
        return self._c == 0

    def enqueue(self, e):
        node = self._Node(e)

        self._tail.next = node

        self._tail = node

        self._c += 1

    def dequeue(self):
        if self.empty():
            raise EmptyError

        r = self._head.next

        self._head.next = r.next

        # 如果出队的恰好是尾结点
        if self._tail == r:
            self._tail = self._head

        self._c -= 1

        return r.e

    def first(self):
        if self.empty():
            raise EmptyError

        return self._head.next.e


q = Queue()

q.enqueue(1)
print(q.first())
print(q.dequeue())
# print(q.first())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.first())