# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在仅给出两个节点x和y的指针的情况下, 怎样在单链表中交换这俩节点
    双链表呢?

    不能直接交换内容

    分析各自耗时

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
        self._c = 0

    def __len__(self):
        return self._c

    def empty(self):
        return self._c == 0

    def _insert_after(self, left, e):

        node = e if isinstance(e, self._Node) else self._Node(e)

        node._next = left._next
        left._next = node

        self._c += 1

        return node

    def add_first(self, e):

        return self._insert_after(self._head, e)

    def __iter__(self):

        cursor = self._head._next

        while cursor:

            yield cursor._e

            cursor = cursor._next

    def swap(self, x, y):
        if x is y: return

        # 单链表, 必须找其前置节点
        # O(n)

        x_pre = y_pre = None

        cursor = self._head

        while cursor:

            if cursor._next == x:
                x_pre = cursor

            if cursor._next == y:
                y_pre = cursor

            if x_pre and y_pre:
                break

            cursor = cursor._next

        # 这里注意要考虑相邻的特殊情况
        # 画个图, 指针怎么操作就清晰了
        if x._next is y:

            x._next = y._next

            self._insert_after(x_pre, y)

        elif y._next is x:

            y._next = x._next

            self._insert_after(y_pre, x)

        else:

            x_pre._next = x._next
            y_pre._next = y._next

            self._insert_after(x_pre, y)
            self._insert_after(y_pre, x)


l = LinkedList()

n5 = l.add_first(5)
n4 = l.add_first(4)
n3 = l.add_first(3)
n2 = l.add_first(2)
n1 = l.add_first(1)

print(list(l))

l.swap(n2, n2)
print(list(l))

class DoubleLinkedList:

    class _Node:

        def __init__(self, e=None):
            self._e = e
            self._prev = None
            self._next = None

    def __init__(self):

        self._head = self._Node()
        self._tail = self._Node()

        self._head._next = self._tail
        self._tail._prev = self._head

        self._c = 0

    def __len__(self):
        return self._c

    def empty(self):
        return self._c == 0

    def _insert_after(self, left, e):

        node = e if isinstance(e, self._Node) else self._Node(e)

        node._next = left._next
        node._prev = left

        node._next._prev = node
        left._next = node

        self._c += 1

        return node

    def add_first(self, e):

        return self._insert_after(self._head, e)

    def __iter__(self):

        cursor = self._head._next

        while cursor is not self._tail:

            yield cursor._e

            cursor = cursor._next

    def swap(self, x, y):

        if x is y: return

        # O(1)

        if x._next is y:

            # 把y删掉放x前面去
            x._next = y._next
            y._next._prev = x

            self._insert_after(x._prev, y)

        elif y._next is x:

            # 把x删掉放y前面去
            y._next = x._next
            x._next._prev = y

            self._insert_after(y._prev, x)

        else:

            # 不相邻, 可以同时删
            x_before = x._prev
            y_before = y._prev

            x_before._next = x._next
            x._next._prev = x_before

            y_before._next = y._next
            y._next._prev = y_before

            self._insert_after(x_before, y)
            self._insert_after(y_before, x)


dll = DoubleLinkedList()
p6 = dll.add_first(6)
p5 = dll.add_first(5)
p4 = dll.add_first(4)
p3 = dll.add_first(3)
p2 = dll.add_first(2)
p1 = dll.add_first(1)
print(list(dll))

dll.swap(p1, p6)
print(list(dll))