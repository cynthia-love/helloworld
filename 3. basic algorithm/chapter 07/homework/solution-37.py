# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在PositionList里找到是否存在两个元素和为V

    如果找到, 返回位置信息; 未找到, 返回None

    要求时间复杂度为O(n)

"""

"""
    思路:
    O(n)说明只能遍历一次, 还得要位置信息
    
    {value: 位置}
    
    每遍历到一个值去之前的hash表里找, 是否有V-value
    有则直接返回两者位置, 没有则add后继续遍历下一个位置
    
"""

class IllegalNode(Exception):
    pass

class IllegalPosition(Exception):
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

        self.nodes = {self.head, self.tail}

    def __len__(self):

        return len(self.nodes)-2

    def empty(self):
        return len(self) == 0

    def __iter__(self):
        cursor = self.head.next

        while cursor is not self.tail:
            yield cursor.e

            cursor = cursor.next

    def _validate(self, node):

        if node not in self.nodes:
            return False

        return True

    def _add_after(self, left, e):

        if not self._validate(left):
            raise IllegalNode

        if left is self.tail:

            raise IllegalNode

        node = self.Node(e)

        right = left.next

        node.prev, node.next = left, right
        left.next, right.prev = node, node

        self.nodes.add(node)

        return node

    def _add_before(self, right, e):

        if not self._validate(right):
            raise IllegalNode

        if right is self.head:
            raise IllegalNode

        node = self.Node(e)

        left = right.prev

        node.prev, node.next = left, right
        left.next, right.prev = node, node

        self.nodes.add(node)

        return node

    def _delete(self, node):

        if not self._validate(node):
            raise IllegalNode

        if node in [self.head, self.tail]:
            raise IllegalNode

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = node.next = None

        self.nodes.remove(node)

        return node.e

class PositionLinkedList(DoubleLinkedList):

    class Position:

        def __init__(self, container, node):

            self.container = container
            self.node = node

        @property
        def e(self):
            return self.node.e

    def validate(self, p):
        if not isinstance(p, self.Position):
            return False

        if p.container is not self:
            return False

        if not self._validate(p.node):
            return False

        return True

    def n2p(self, node):

        if not self._validate(node):
            raise IllegalNode

        if node in [self.head, self.tail]:
            return None

        return self.Position(self, node)

    # ---accessor---
    def first(self):
        return self.n2p(self.head.next)

    def last(self):
        return self.n2p(self.tail.prev)

    def before(self, p):
        if not self.validate(p):
            raise IllegalPosition

        return self.n2p(p.node.prev)

    def after(self, p):
        if not self.validate(p):
            raise IllegalPosition

        return self.n2p(p.node.next)

    # ---mutator---
    def add_first(self, e):
        return self.n2p(self._add_after(self.head, e))

    def add_last(self, e):
        return self.n2p(self._add_before(self.tail, e))

    def add_before(self, right, e):
        if not self.validate(right):
            raise IllegalPosition

        return self.n2p(self._add_before(right.node, e))

    def add_after(self, left, e):
        if not self.validate(left):
            raise IllegalPosition

        return self.n2p(self._add_after(left.node, e))

    def delete(self, p):
        if not self.validate(p):
            raise IllegalPosition

        return self._delete(p.node)

    def find_sum(self, v):

        h = dict()

        cursor = self.first()

        while cursor:

            if v-cursor.e in h:

                return h[v-cursor.e], cursor

            else:

                h[cursor.e] = cursor
                cursor = self.after(cursor)

        return None

pl = PositionLinkedList()

for i in range(100):
    pl.add_first(i)

print([v.e for v in pl.find_sum(20)])

print(pl.find_sum(1000))