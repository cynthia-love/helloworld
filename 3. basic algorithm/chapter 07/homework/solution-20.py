# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    逆序实现Move-to-Front收藏夹
    (即每次访问完移动到末尾, 查找也从末尾开始)
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

        if right is self.head:
            raise IllegalNode

        left = right.left
        node = self.Node(e)

        node.left, node.right = left, right
        left.right, right.left = node, node

        self.nodes.add(node)

        return node

    def _add_after(self, left, e):

        if not self._validate(left):
            raise IllegalNode

        if left is self.tail:
            raise IllegalNode

        right = left.right
        node = self.Node(e)

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

        r = node.e

        node.left = node.right = node.e = None

        self.nodes.remove(node)

        return r

    def _move_last(self, node):

        if not self._validate(node):
            raise IllegalNode

        if node in [self.head, self.tail]:
            raise IllegalNode

        node.left.right = node.right
        node.right.left = node.left

        left, right = self.tail.left, self.tail

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
            raise IllegalNode

        return self.n2p(p.node.left)

    def after(self, p):
        if not self.validate(p):
            raise IllegalNode

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

    def move_last(self, p):
        if not self.validate(p):
            raise IllegalPosition

        self._move_last(p.node)

class FavoritesListMTF:

    class ElementType:

        __slots__ = 'v', 'c'

        def __init__(self, v, c=1):
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
        # 逆序, 从末尾开始查找, 返回data的位置对象
        cursor = self.data.last()

        while cursor:

            if cursor.e.v is v:
                return cursor

            cursor = self.data.before(cursor)

        return None

    def move(self, p):
        # 逆序, 移动到末尾
        self.data.move_last(p)

    def access(self, v):

        p = self.find(v)

        if p:
            p.e.c += 1

        else:
            e = self.ElementType(v)

            p = self.data.add_first(e)

        self.move(p)

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