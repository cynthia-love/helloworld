# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出在单链表中找到第二个结点到最后一个结点的算法,
    其中最后一个结点的next指针指向空
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

    def add_first(self, e):

        node = self._Node(e)

        node._next = self._head._next
        self._head._next = node

        self._c += 1

    def del_first(self):
        if self.empty():
            raise EmptyError

        r = self._head._next._e

        self._head._next = self._head._next._next

        self._c -= 1

        return r

    def first(self):
        if self.empty():
            raise EmptyError

        return self._head._next._e

    def add_last(self, e):
        # 插入, 考虑空的情况, 初始指向头结点
        # 下一个有值才后移, 保证退出时指向最后一个结点(可能为头结点)

        cursor = self._head

        while cursor._next:

            cursor = cursor._next

        node = self._Node(e)

        cursor._next = node

    def del_last(self):

        if self.empty():
            raise EmptyError

        # 删除, 排除空的情况
        # 初始指向头结点, 下下个有值才后移
        # 保证退出时下下个没值, 即指向倒数第二个结点, 可能为头结点

        cursor = self._head

        while cursor._next._next:
            cursor = cursor._next

        r = cursor._next._e

        cursor._next = None

        return r

    def last(self):
        if self.empty():
            raise EmptyError

        # 访问, 排除空的情况, 初始设置第一个元素节点
        # 下一个有值才后移, 保证退出时指向最后一个元素节点
        cursor = self._head._next

        while cursor._next:
            cursor = cursor._next

        return cursor._e

    def __iter__(self):

        cursor = self._head._next

        while cursor:
            yield cursor._e
            cursor = cursor._next

    def not_first1(self):

        cursor = self._head

        r = []

        # 初始设置满足条件节点的上一个, 有下一个才移动指针, 然后拼接返回
        while cursor._next:
            cursor = cursor._next
            r.append(cursor._e)

        return r

    def not_first2(self):

        cursor = self._head._next

        r = []

        # 初始设置满足条件节点的第一个, 有才拼接, 然后移动指针
        # 比较和上一个函数之间的逻辑区别
        while cursor:
            r.append(cursor._e)

            cursor = cursor._next

        return r

ll = LinkedList()

ll.add_first(1)
ll.add_last(2)
ll.add_first(-1)
ll.add_last(3)
print(list(ll))
print(ll.first(), ll.last())
print(ll.del_first())
print(list(ll))
print(ll.del_last())
print(list(ll))

ll.add_first(1)
ll.add_last(2)
ll.add_first(-1)
ll.add_last(3)

print(ll.not_first1())
print(ll.not_first2())