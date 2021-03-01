# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对Position实现max()函数, 返回最大元素

"""

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
        return len(self.nodes)-2

    def _empty(self):
        return len(self) == 0

    def _validate(self, node):

        if node in self.nodes:
            return True

        return False

    def _add_after(self, left, e):

        if not self._validate(left):
            raise KeyError

        if left is self.tail:
            raise KeyError

        node = self.Node(e)

        right = left.next

        node.prev, node.next = left, right
        left.next, right.prev = node, node

        self.nodes.add(node)

        return node

    def _add_before(self, right, e):

        if not self._validate(right):
            raise KeyError

        if right is self.head:
            raise KeyError

        left = right.prev
        node = self.Node(e)

        node.prev, node.next = left, right
        left.next, right.prev = node, node

        self.nodes.add(node)

        return node

    def _delete(self, node):

        if not self._validate(node):
            raise KeyError

        if node in [self.head, self.tail]:
            raise KeyError

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

        # max(l)函数需要元素实现__gt__方法
        def __gt__(self, other):

            if type(other) is not type(self):
                raise KeyError

            return self.element > other.element

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
            raise KeyError

        if node in [self.head, self.tail]:
            return None

        return self.Position(self, node)

    # -----accessor-----
    def first(self):

        return self.n2p(self.head.next)

    def last(self):
        return self.n2p(self.tail.prev)

    def before(self, p):

        if not self.validate(p):
            raise KeyError

        return self.n2p(p.node.prev)

    def after(self, p):

        if not self.validate(p):
            raise KeyError

        return self.n2p(p.node.next)

    def __iter__(self):
        # 返回位置, 而非value
        cursor = self.first()

        while cursor:
            yield cursor
            cursor = self.after(cursor)

    # -----mutator-----
    def add_first(self, e):

        return self.n2p(self._add_after(self.head, e))

    def add_last(self, e):
        return self.n2p(self._add_before(self.tail, e))

    def add_before(self, right, e):

        if not self.validate(right):
            raise KeyError

        return self.n2p(self._add_before(right.node, e))

    def add_after(self, left, e):

        if not self.validate(left):
            raise KeyError

        return self.n2p(self._add_after(left.node, e))

    def delete(self, p):

        if not self.validate(p):
            raise KeyError

        r = self._delete(p.node)

        p.container = p.node = None

        return r


pll = PositionLinkedList()
p1 = pll.add_first(1)
p2 = pll.add_last(2)
p3 = pll.add_last(3)
p4 = pll.add_last(2)
pll.add_before(p1, 0)
pll.add_after(p1, 1.5)

# max要求实现对象的枚举和每个元素的__gt__
print(max(pll).element)