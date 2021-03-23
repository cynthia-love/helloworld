# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用单链表实现固定大小的栈; 栈满时入栈则从栈底压出一个元素

    涉及一侧插入, 两侧删除, 其实单链表不是很合适

"""

class EmptyError(Exception):
    pass

class Stack:

    class Node:
        def __init__(self, e=None):
            self.e = e
            self.next = None

    def __init__(self, size=5):

        self.head = self.Node()

        self.size = size

        self.c = 0

    def __len__(self):
        return self.c

    def __iter__(self):

        cursor = self.head.next

        for _ in range(self.c):
            yield cursor.e
            cursor = cursor.next

    def _add_after(self, left, e):

        node = self.Node(e)

        node.next = left.next
        left.next = node

        self.c += 1

    def _del_after(self, left):
        node = left.next

        left.next = node.next
        self.c -= 1

        return node.e

    def last2(self):
        cursor = self.head

        for _ in range(self.c-1):
            cursor = cursor.next

        return cursor

    def empty(self):
        return self.c == 0

    def full(self):
        return self.c == self.size

    def push(self, e):

        if self.full():
            self._add_after(self.head, e)
            self._del_after(self.last2())
        else:
            self._add_after(self.head, e)

    def top(self):
        if self.empty():
            raise EmptyError

        return self.head.next.e

    def pop(self):
        if self.empty():
            raise EmptyError

        return self._del_after(self.head)

s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(list(s))
print(s.top())

print(s.pop())
print(list(s))

