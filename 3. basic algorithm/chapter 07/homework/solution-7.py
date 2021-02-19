# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    LinkedQueue实现rotate方法

    不能创建新节点
"""

class EmptyError(Exception):
    pass

class LinkedList:

    class _Node:

        __slots__ = '_e', '_next'

        def __init__(self, e=None):

            self._e = e
            self._next = None

    def __init__(self):

        self._head = self._Node()

        # 带头结点, 初始尾结点指向头结点
        self._tail = self._head

        self._c = 0

    def __len__(self):
        return self._c

    def empty(self):
        return self._c == 0

    def _insert_after(self, left, e):

        # insert同时支持插入值和节点
        node = e if isinstance(e, self._Node) else self._Node(e)

        node._next = left._next
        left._next = node

        # 兼容空和非空的情况
        if left is self._tail:

            self._tail = node

        self._c += 1

        return node

    def _del_node(self, node):

        # 指定了node, 假定链表不为空

        cursor = self._head

        # 退出条件为cursor的下一个结点是node结点
        while cursor._next is not node:

            cursor = cursor._next

        cursor._next = node._next

        # 兼容删除的是尾结点和非尾结点的情况
        if self._tail is node:

            self._tail = cursor

        self._c -= 1

        return node

    def __iter__(self):

        cursor = self._head

        while cursor._next:

            cursor = cursor._next

            yield cursor._e

class LinkedQueue(LinkedList):

    def enqueue(self, e):

        return self._insert_after(self._tail, e)

    def dequeue(self):

        if self.empty():
            raise EmptyError

        return self._del_node(self._head._next)._e

    def first(self):
        if self.empty():
            raise EmptyError

        return self._head._next._e

    def rotate(self, k):
        if self.empty():
            raise EmptyError

        # 不断地删除头部结点接到尾部
        # 可以兼容只有一个元素的情况, 删除后tail指向头结点
        for _ in range(k):

            # 注意这里不能这么写, 因为需要拿到的是tail的新值, 这么写传过去的是旧值
            # self._insert_after(self._tail, self._del_node(self._head._next))

            node = self._del_node(self._head._next)
            self._insert_after(self._tail, node)

lq = LinkedQueue()
print(list(lq))
lq.enqueue(8)
lq.enqueue(10)
lq.enqueue(12)
print(list(lq))
print(lq.empty())
print(lq.first())
print(lq.dequeue())
print(list(lq))
lq.enqueue(16)
lq.enqueue(18)
print(list(lq))
lq.rotate(2)
print(list(lq))
lq.dequeue()
lq.dequeue()
lq.dequeue()
print(list(lq))
lq.rotate(3)
print(list(lq))
