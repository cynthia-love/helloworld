# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    用Iterator类嵌套的方式而非自身__iter__()实现PositionList的迭代
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
        return len(self.nodes) - 2

    def empty(self):
        return len(self) == 0

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


class PositionList(DoubleLinkedList):

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

    # ===accessor===
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

    # ===mutator===
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


class Iterator:

    def __init__(self, sequence):

        self.sequence = sequence

        self.pos = self.sequence.first()

    """
    直接这么写是generator的写法, 需要显式iter(o)才能转化成iterator
    要想直接是iterator, 还得实现__next__方法
    def __iter__(self):

        cursor = self.sequence.first()

        while cursor:
            yield cursor.e
            cursor = self.sequence.after(cursor)
    """

    def __next__(self):
        if not self.pos:
            raise StopIteration

        r = self.pos.e

        self.pos = self.sequence.after(self.pos)

        return r

    def __iter__(self):
        return self


pl = PositionList()

p1 = pl.add_first(1)
p2 = pl.add_last(10)

p3 = pl.add_before(p1, -1)
p4 = pl.add_after(p1, 3)

it = Iterator(pl)

print(list(it))

it = Iterator(pl)
print(it, next(it))

