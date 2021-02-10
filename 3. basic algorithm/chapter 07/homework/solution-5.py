# -*- coding; utf-8 -*-
# Author: Cynthia

"""
    统计循环列表节点个数

"""

class EmptyError(Exception):
    pass

class CircularLinkedList:

    class _Node:

        def __init__(self, e=None):

            self._e = e
            self._next = None

    def __init__(self):
        # 循环链表只存储一个尾指针
        # 既方便尾部插入又能很容易找到头部节点

        self._tail = None

    def __len__(self):

        if not self._tail: return 0

        # 从头部第一个元素开始计
        cursor = self._tail._next
        count = 0

        # 先+1, 再判断是否计到了尾结点
        while True:
            count += 1

            if cursor == self._tail:
                break

            cursor = cursor._next

        # 指到尾节点的时候循环退出, 少记一个元素

        return count

    def empty(self):
        return len(self) == 0

    def add_last(self, e):

        node = self._Node(e)

        if self.empty():
            self._tail = node
            node._next = self._tail

        else:

            node._next = self._tail._next
            self._tail._next = node

            # 插入完将尾指针后移一位
            self._tail = self._tail._next

    def __iter__(self):

        if not self.empty():

            cursor = self._tail._next

            while True:

                # 先访问, 再判断是否是尾结点
                yield cursor._e

                if cursor is self._tail:
                    break

                cursor = cursor._next

cll = CircularLinkedList()
print(len(cll))
print(list(cll))

cll.add_last(1)
cll.add_last(2)
cll.add_last(3)
print(len(cll))
print(list(cll))