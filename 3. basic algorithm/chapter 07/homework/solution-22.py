# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    为FavoritesList实现clear方法, 清空列表

"""

class IllegalNode(Exception):
    pass

class IllegalPosition(Exception):
    pass

class DoubleLinkedList:

    class Node:

        __slots__ = 'e', 'left', 'right'

        def __init__(self, e=None):

            self.e = e
            self.left = None

            self.right = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()

        self.head.right = self.tail
        self.tail.left = self.head

        self.nodes = {self.head, self.tail}

    def __len__(self):

        return len(self.nodes)-2

    def empty(self):
        return len(self) == 0

    def _validate(self, node):
        if node not in self.nodes:
            return False

        return True

    def _add_before(self, right, e):

        if not self._validate(right):
            raise IllegalNode

        node = self.Node(e)

        left = right.left

        node.left, node.right = left, right
        left.right, right.left = node, node

        self.nodes.add(node)

        return node

    def _add_after(self, left, e):

        if not self._validate(left):
            raise IllegalNode

        node = self.Node(e)

        right = left.right

        node.left, node.right = left, right
        left.right, right.left = node, node

        self.nodes.add(node)

        return node

    def _delete(self, node):
        if not self._validate(node):
            raise IllegalNode

        if node in [self.head, self.tail]:
            raise IllegalNode

        node.left.right = node.right
        node.right.left = node.left

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

        return True

    def n2p(self, node):
        if not self._validate(node):
            raise IllegalNode

        if node in [self.head, self.tail]:
            return None

        return self.Position(self, node)

    # ===accessor===
    def first(self):
        return self.n2p(self.head.right)

    def last(self):
        return self.n2p(self.tail.left)

    def before(self, p):
        if not self.validate(p):
            raise IllegalPosition

        return self.n2p(p.node.left)

    def after(self, p):
        if not self.validate(p):
            raise IllegalPosition

        return self.n2p(p.node.right)

    def __iter__(self):

        cursor = self.first()

        while cursor:
            yield cursor.e
            cursor = self.after(cursor)

    # ===mutator===
    def add_first(self, e):
        return self.n2p(self._add_after(self.head, e))

    def add_last(self, e):
        return self.n2p(self._add_before(self.tail, e))

    def add_before(self, p, e):
        if not self.validate(p):
            raise IllegalPosition

        return self.n2p(self._add_before(p.node, e))

    def add_after(self, p, e):
        if not self.validate(p):
            raise IllegalPosition

        return self.n2p(self._add_after(p.node, e))

    def delete(self, p):

        if not self.validate(p):
            raise IllegalPosition

        r = self._delete(p.node)
        p.container = p.node = None

        return r

class FavoritesList:

    class ElementType:

        __slots__ = 'k', 'v'

        def __init__(self, k=None, v=0):
            self.k = k
            self.v = v

    def __init__(self):
        self.data = PositionLinkedList()

    def __len__(self):
        return len(self.data)

    def empty(self):
        return self.data.empty()

    def __iter__(self):

        for e in self.data:
            yield e.k, e.v

    def find(self, k):

        cursor = self.data.first()

        while cursor:

            if cursor.e.k is k:
                return cursor

            cursor = self.data.after(cursor)

        return None

    def move(self, p):

        q = self.data.before(p)

        while q and q.e.v < p.e.v:

            q = self.data.before(q)

        if q:
            self.data.add_after(q, self.data.delete(p))

        else:
            self.data.add_first(self.data.delete(p))

    def access(self, k):

        p = self.find(k)

        if p:

            p.e.v += 1
            self.move(p)

        else:

            self.data.add_last(self.ElementType(k, 1))

    def remove(self, k):

        p = self.find(k)

        if p:
            self.data.delete(p)

    def top(self, k):

        if not 1 <= k <= len(self):
            raise KeyError

        return list(self)[:k]

    def clear(self):

        cursor = self.data.first()

        while cursor:

            right = self.data.after(cursor)

            self.data.delete(cursor)

            cursor = right

fl = FavoritesList()

l1 = ['a', 'b', 'c', 'd', 'e', 'f']
for e in l1: fl.access(e)
print(list(fl))

l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'c', 'f', 'b', 'd', 'e']
for e in l2: fl.access(e)

fl.access('a')
fl.access('a')
fl.access('b')

print(list(fl))
print(fl.top(3))

fl.clear()
print(list(fl))