# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    假定x和y是循环列表的节点, 但不必属于同一个链表
    设计算法, 判断x、y是否来自同一个链表
"""

class EmptyError(Exception):
    pass

class CircularLinkedList:

    class _Node:

        def __init__(self, e=None):
            self._e = e
            self._next = None

    def __init__(self):
        self._tail = None

    def __len__(self):

        if not self._tail:
            return 0

        cursor = self._tail._text

        count = 0

        while True:
            count += 1

            if cursor is self._tail:
                break

            cursor = cursor._next

        return count

    def empty(self):
        return len(self) == 0

    def add_last(self, e):

        node = self._Node(e)

        if not self._tail:

            self._tail = node

            node._next = node

        else:

            node._next = self._tail._next
            self._tail._next = node

            self._tail = node

        return node

    def __iter__(self):

        if not self.empty():

            cursor = self._tail._next

            while True:

                yield cursor._e

                if cursor is self._tail:
                    break

                cursor = cursor._next

    @classmethod
    def cmp(cls, x, y):
        if not isinstance(x, cls._Node):
            raise TypeError

        if not isinstance(y, cls._Node):
            raise TypeError

        cursor = x._next

        while True:

            if cursor is y:
                return True

            # 从x的下一个位置开始循环
            # 一直处理到x, 还未return True
            # 说明x所在的循环链表里无y节点
            if cursor is x:
                return False

            cursor = cursor._next

l1 = CircularLinkedList()

l2 = CircularLinkedList()

n11 = l1.add_last(1)
n12 = l1.add_last(2)

n21 = l2.add_last(1)
n22 = l2.add_last(2)

print(CircularLinkedList.cmp(n11, n12))
print(CircularLinkedList.cmp(n11, n11))

print(CircularLinkedList.cmp(n11, n21))

