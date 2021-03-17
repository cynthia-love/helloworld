# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用带头结点的单向链表实现列表
"""

class EmptyError(Exception):
    pass

class Queue:

    class Node:

        __slots__ = 'e', 'next'

        def __init__(self, e=None):

            self.e = e
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.count = 0

    def __len__(self):
        return self.count

    def __iter__(self):

        cursor = self.head.next

        while cursor:
            yield cursor.e

            cursor = cursor.next

    def empty(self):
        return self.count == 0

    def enqueue(self, e):

        cursor = self.head

        for _ in range(self.count):
            cursor = cursor.next

        node = self.Node(e)

        cursor.next = node
        self.count += 1

        return node

    def dequeue(self):
        if self.empty():
            raise EmptyError

        r = self.head.next

        self.head.next = r.next
        self.count -= 1

        return r.e

    def first(self):
        if self.empty():
            raise EmptyError

        return self.head.next.e


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(8)
print(list(q))
print(q.count)
print(q.first())
q.dequeue()
print(list(q))
print(q.count)
print(q.first())