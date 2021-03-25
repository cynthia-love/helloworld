# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在循环链表上实现PositionList
"""

class EmptyError(Exception):
    pass

class IllegalNode(Exception):
    pass

class IllegalPosition(Exception):
    pass

class CircularLinkedList:

    class Node:

        def __init__(self, e=None):
            self.e = e
            self.next = None

    def __init__(self):

        self.tail = None

        self.nodes = set()

    def __len__(self):
        return len(self.nodes)

    def empty(self):
        return len(self) == 0

    def __iter__(self):

        cursor = self.tail

        for _ in range(len(self)):

            cursor = cursor.next

            yield cursor.e

    def _validate(self, node):

        if node not in self.nodes:
            return False

        return True

    def _add_first(self, e):

        node = self.Node(e)

        if not self.tail:

            node.next = node
            self.tail = node

        else:
            node.next = self.tail.next
            self.tail.next = node

        self.nodes.add(node)

        return node

    def _add_last(self, e):

        node = self.Node(e)

        if not self.tail:
            node.next = node
            self.tail = node

        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node

        self.nodes.add(node)

        return node

    def _add_after(self, left, e):

        if not self._validate(left):
            raise IllegalNode

        node = self.Node(e)

        node.next = left.next
        left.next = node

        self.nodes.add(node)

        if left is self.tail:
            self.tail = node

        return node

    def _del_first(self):

        if self.empty():
            raise EmptyError

        if len(self) == 1:
            self.tail = None
            self.nodes.clear()
            return

        node = self.tail.next

        self.tail.next = node.next
        self.nodes.remove(node)

        return node.e

    def _del_last(self):

        if self.empty():
            raise EmptyError

        if len(self) == 1:
            self.tail = None
            self.nodes.clear()
            return

        cursor = self.tail

        while cursor.next != self.tail:

            cursor = cursor.next

        r = self.tail

        cursor.next = r.next
        self.tail = cursor
        self.nodes.remove(r)

        return r.e

    def _del_after(self, left):

        if not self._validate(left):
            raise IllegalNode

        if len(self) == 1:
            self.tail = None
            self.nodes.clear()
            return

        node = left.next

        left.next = node.next

        if node is self.tail:

            self.tail = left
        self.nodes.remove(node)

        return node.e

class PositionList(CircularLinkedList):

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

        return self.Position(self, node)

    # ===accessor===
    def first(self):
        if self.empty():
            raise EmptyError

        return self.n2p(self.tail.next)

    def last(self):
        if self.empty():
            raise EmptyError

        return self.n2p(self.tail)

    def after(self, left):
        if not self.validate(left):
            raise IllegalPosition

        return self.n2p(left.node.next)

    # ===mutator===

    def add_first(self, e):
        return self.n2p(self._add_first(e))

    def add_last(self, e):
        return self.n2p(self._add_last(e))

    def add_after(self, left, e):

        if not self.validate(left):
            raise IllegalPosition

        return self.n2p(self._add_after(left.node, e))

    def del_first(self):
        if self.empty():
            raise EmptyError

        return self._del_first()

    def del_last(self):
        if self.empty():
            raise EmptyError

        return self._del_last()

    def del_after(self, left):

        if not self.validate(left):
            raise IllegalPosition

        return self._del_after(left.node)

pl = PositionList()
print(pl.empty())
p1 = pl.add_first(1)  # 1
p2 = pl.add_first(-1)  # -1, 1
p3 = pl.add_last(2)  # -1, 1, 2
p4 = pl.add_after(p1, 1.1)  # -1, 1, 1.1, 2
p5 = pl.add_after(p3, 2.1)  # -1, 1, 1.1, 2, 2.1
print(list(pl))
print(pl.first().e)
print(pl.last().e)
print(pl.after(p1).e)

# pl.del_first()
# print(list(pl))
# pl.del_last()
# print(list(pl))
pl.del_after(p1)
print(list(pl))
pl.del_after(p3)
print(list(pl))
pl.del_after(p3)
print(list(pl))
