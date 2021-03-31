# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    使用不带头尾结点的双向链表实现PositionList

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
        self.head = self.tail = None

        self.nodes = set()

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        cursor = self.head

        while cursor:
            yield cursor.e
            cursor = cursor.next

    def empty(self):
        return len(self) == 0

    def _validate(self, node):

        if node not in self.nodes:
            return False

        return True

    def _add_first(self, e):

        node = self.Node(e)

        if self.empty():
            self.head = self.tail = node

        else:
            node.next = self.head
            self.head.prev = node

            self.head = node

        self.nodes.add(node)

        return node

    def _add_last(self, e):
        node = self.Node(e)

        if self.empty():
            self.head = self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail

            self.tail = node

        self.nodes.add(node)

        return node

    def _add_before(self, right, e):

        if not self._validate(right):
            raise IllegalNode

        if right is self.head:

            return self._add_first(e)

        else:

            node = self.Node(e)

            left = right.prev

            node.prev, node.next = left, right
            left.next, right.prev = node, node

            self.nodes.add(node)

            return node

    def _add_after(self, left, e):

        if not self._validate(left):
            raise IllegalNode

        if left is self.tail:
            return self._add_last(e)

        else:

            node = self.Node(e)

            right = left.next

            node.prev, node.next = left, right
            left.next, right.prev = node, node

            self.nodes.add(node)

            return node

    def _delete(self, node):

        if not self._validate(node):
            raise IllegalNode

        if len(self) == 1:

            self.head = self.tail = None

        # 元素个数至少为2个
        elif node is self.head:

            node.next.prev = None
            self.head = node.next

        elif node is self.tail:

            node.prev.next = None
            self.tail = node.prev

        else:
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

        if node is None:
            return None

        if not self._validate(node):
            raise IllegalNode

        return self.Position(self, node)

    # ===accessor===
    def first(self):
        return self.n2p(self.head)

    def last(self):
        return self.n2p(self.tail)

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
        return self.n2p(self._add_first(e))

    def add_last(self, e):
        return self.n2p(self._add_last(e))

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


pl = PositionList()
print(list(pl))

p1 = pl.add_first(1)
p2 = pl.add_last(2)
print(list(pl))
p3 = pl.add_before(p1, 0.4)
p4 = pl.add_after(p1, 1.3)
p5 = pl.add_after(p2, 8)
print(list(pl))

print(pl.first().e, pl.last().e, pl.before(p1).e, pl.after(p2).e)

pl.delete(p3)
print(list(pl))

pl.delete(p5)
print(list(pl))

pl.delete(p4)
print(list(pl))