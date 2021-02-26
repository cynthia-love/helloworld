# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    合并两个双向链表
"""

class EmptyError(Exception):
    pass

class DoubleLinkedList:

    class Node:

        def __init__(self, e=None):

            self.e = e
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.c = 0

    def __len__(self):
        return self.c

    def empty(self):
        return self.c == 0

    def _insert_between(self, left, right, e):

        node = self.Node(e)

        node.prev, node.next = left, right

        left.next, right.prev = node, node

        self.c += 1

        return node

    def add_before(self, node, e):

        return self._insert_between(node.prev, node, e)

    def add_after(self, node, e):

        return self._insert_between(node, node.next, e)

    def add_first(self, e):

        return self._insert_between(self.head, self.head.next, e)

    def add_last(self, e):

        return self._insert_between(self.tail.prev, self.tail, e)

    def __iter__(self):

        cursor = self.head.next

        while cursor is not self.tail:

            yield cursor.e
            cursor = cursor.next

    @classmethod
    def merge(cls, dll1, dll2):

        res = cls()

        for e in dll1:
            res.add_last(e)

        for e in dll2:
            res.add_last(e)

        return res

dll = DoubleLinkedList()
dll.add_first(1)
dll.add_first(0)
dll.add_last(2)
dll.add_last(3)

print(list(dll))

dll2 = DoubleLinkedList()
dll2.add_first(-1)
dll2.add_first(-0)
dll2.add_last(-2)
dll2.add_last(-3)
print(list(dll2))

dll3 = DoubleLinkedList.merge(dll, dll2)

print(list(dll3))