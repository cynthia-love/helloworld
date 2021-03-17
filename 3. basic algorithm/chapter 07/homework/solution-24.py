# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用带头结点的单向链表实现栈
"""
class EmptyError(Exception):
    pass

class Stack:

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

    def empty(self):
        return len(self) == 0

    def __iter__(self):
        cursor = self.head.next

        while cursor:
            yield cursor.e
            cursor = cursor.next

    def push(self, e):
        node = self.Node(e)
        node.next = self.head.next
        self.head.next = node

        self.count += 1

    def pop(self):
        if self.empty():
            raise EmptyError

        r = self.head.next

        self.head.next = r.next

        self.count -= 1

        return r.e

    def top(self):
        if self.empty():
            raise EmptyError

        return self.head.next.e

s = Stack()
s.push(1)
s.push(2)
s.push(-1)
s.push(8)
print(list(s))
s.pop()
print(list(s))
print(s.top())
print(s.count)
print(s.empty())