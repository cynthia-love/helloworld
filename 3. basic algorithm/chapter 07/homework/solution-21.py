# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Move-to-Front收藏夹, n个元素
    设计长度为n^2的访问序列, 使得时间复杂度为O(n^3)

    分析:
    总时间复杂度n^3, 那么每个元素访问时间复杂度O(n)

    1-2-3-4-5, 以左为头, 那么访问顺序为:
    5: 5-1-2-3-4
    4: 4-5-1-2-3
    3...

    即按最近一次访问时间计, 每次都去访问最早的那个元素

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

    def _move_first(self, node):

        if not self._validate(node):
            raise IllegalNode

        node.left.right = node.right
        node.right.left = node.left

        left, right = self.head, self.head.right

        node.left, node.right = left, right
        left.right, right.left = node, node

        return node

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

        return self._add_before(p.node, e)

    def add_after(self, p, e):
        if not self.validate(p):
            raise IllegalPosition

        return self._add_after(p.node, e)

    def delete(self, p):

        if not self.validate(p):
            raise IllegalPosition

        r = self._delete(p.node)

        p.container = p.node = None

        return r

    def move_first(self, p):

        if not self.validate(p):
            raise IllegalPosition

        self._move_first(p.node)

class FavoritesListMTF:

    class ElementType:

        __slots__ = 'v', 'c'

        def __init__(self, v=None, c=1):

            self.v = v
            self.c = c

    def __init__(self):
        self.data = PositionLinkedList()

    def __len__(self):
        return len(self.data)

    def empty(self):
        return self.data.empty()

    def __iter__(self):

        for e in self.data:
            yield e.v, e.c

    def find(self, v):

        def rf(p):
            if not p: return None

            if p.e.v is v:
                return p
            else:
                return rf(self.data.after(p))

        return rf(self.data.first())

    def move(self, p):

        self.data.move_first(p)

    def access(self, v):

        p = self.find(v)

        if p:
            p.e.c += 1
            self.move(p)

        else:
            e = self.ElementType(v)

            self.data.add_first(e)

    def remove(self, v):

        p = self.find(v)

        if p:
            self.data.delete(p)

    def top(self, k):

        if not 1 <= k <= len(self):
            raise KeyError

        t = list(self)

        t.sort(key=lambda x:x[1], reverse=True)

        return t[:k]


fl = FavoritesListMTF()

l1 = ['a', 'b', 'c', 'd', 'e', 'f']
for e in reversed(l1): fl.access(e)
print(list(fl))

l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'c', 'f', 'b', 'd', 'e']
for e in l2: fl.access(e)

fl.access('a')
fl.access('a')
fl.access('b')

print(list(fl))
print(fl.top(3))