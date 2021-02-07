# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个计算单链表所有节点数量的递归算法
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

    def __len__(self):

        """
        :return:

        f(k) = :
            节点k为空, 0
            节点k不为空, 1+f(k的下一个)

        """
        # def rf(node):
        #
        #     if node:
        #         return 1+rf(node._next)
        #     else:
        #         return 0

        def rf(n, node):
            if node:
                return rf(n+1, node._next)
            else:
                return n

        return rf(0, self._head._next)

    def empty(self):
        return len(self) == 0

    def add_first(self, e):
        node = self._Node(e)

        node._next = self._head._next
        self._head._next = node

    def __iter__(self):
        cursor = self._head._next

        while cursor:

            yield cursor._e

            cursor = cursor._next

ll = LinkedList()
ll.add_first(1)
ll.add_first(2)
ll.add_first(3)
ll.add_first(8)
print(list(ll))
print(len(ll))