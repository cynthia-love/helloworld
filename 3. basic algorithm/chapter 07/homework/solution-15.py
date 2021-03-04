# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对PositionLinkedList实现__reversed__

    reversed(xxx)返回的也是个迭代器
"""

class IllegalNode(Exception):
    pass

class IllegalPosition(Exception):
    pass

class DoubleLinkedList:

    class Node:

        __slots__ = 'e', 'prev', 'next'

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
        return len(self.nodes) - 2

    def _empty(self):
        return len(self) == 0

    def _validate(self, node):
        if node in self.nodes:
            return True

        return False

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
        def element(self):
            return self.node.e

        def __eq__(self, other):
            if type(other) is not type(self):
                return False

            if other.container is not self.container:
                return False

            if other.node is not self.node:
                return False

            return True

    def empty(self):
        return self._empty()

    def validate(self, p):
        if not isinstance(p, self.Position):
            return False

        if p.container is not self:
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

    def __iter__(self):

        cursor = self.first()

        while cursor:
            yield cursor.element

            cursor = self.after(cursor)

    def __reversed__(self):
        cursor = self.last()

        while cursor:
            yield cursor.element
            cursor = self.before(cursor)

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

        r = self._delete(p.node)

        p.container = p.node = None

        return r

pll = PositionLinkedList()
for e in pll: print(e)
print(pll.empty())
print(pll.first(), pll.last())
p1 = pll.add_first(1)
p2 = pll.add_last(2)
for e in pll: print(e)
print(pll.first().element, pll.last().element)
pll.add_before(p1, 0)
pll.add_after(p1, 1.5)
print(list(pll))
print(pll.before(p2).element)
print(pll.after(pll.after(p1)).element)
pll.delete(pll.after(p1))
print(list(pll))
print(len(pll))
print(max(pll))

print(list(reversed(pll)))