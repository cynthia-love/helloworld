# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    合并单链表L1和L2, 生成新的单链表L3
    L2的所有节点都在L1的节点之后
"""

class EmptyError(Exception):
    pass

class LinkedList:

    class _Node:

        def __init__(self, e=None):
            self._e = e
            self._next = None

    def __init__(self):
        self._head = self._Node()

    def empty(self):
        return self._head._next is None

    def first(self):
        if self.empty():
            raise EmptyError

        return self._head._next._e

    def add_first(self, e):
        node = self._Node(e)

        node._next = self._head._next
        self._head._next = node

    def del_first(self):

        if self.empty():
            raise EmptyError

        r = self._head._next

        self._head._next = r._next

        return r._e

    def __iter__(self):

        cursor = self._head._next

        while cursor:

            yield cursor._e

            cursor = cursor._next

    @classmethod
    def merge(cls, l1, l2):
        if not isinstance(l1, cls):
            raise TypeError
        if not isinstance(l2, cls):
            raise TypeError

        l = cls()

        c = l._head
        c1 = l1._head._next
        c2 = l2._head._next

        while c1:
            node = cls._Node(c1._e)

            c._next = node
            c = c._next

            c1 = c1._next

        while c2:
            node = cls._Node(c2._e)

            c._next = node
            c = c._next

            c2 = c2._next

        return l

ll = LinkedList()
ll.add_first(1)
ll.add_first(2)
ll.add_first(3)
print(list(ll))

ll2 = LinkedList()
ll2.add_first(10)
ll2.add_first(20)
ll2.add_first(30)
print(list(ll2))

ll3 = LinkedList.merge(ll, ll2)
print(list(ll3))
