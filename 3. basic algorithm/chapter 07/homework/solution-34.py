# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给PositionList增加swap(p, q)方法, 将p位置和q位置的节点互换

    区分两种情况, 一种是位置没换, 值换了
    一种是指向位置也跟着换了

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

    def _swap1(self, n1, n2):
        if not self._validate(n1):
            raise IllegalNode

        if not self._validate(n2):
            raise IllegalNode

        if n1 in [self.head, self.tail]:
            raise IllegalNode

        if n2 in [self.head, self.tail]:
            raise IllegalNode

        if n1 is n2: return

        n1.e, n2.e = n2.e, n1.e

    def _swap2(self, n1, n2):
        if not self._validate(n1):
            raise IllegalNode

        if not self._validate(n2):
            raise IllegalNode

        if n1 in [self.head, self.tail]:
            raise IllegalNode

        if n2 in [self.head, self.tail]:
            raise IllegalNode

        if n1 is n2: return

        # 为了避免两个结点挨着, 往外侧找基准位置
        # 但有一个问题, 需要确保n1在n2左边, 才能继续找'外侧'
        cursor = self.head.next
        while cursor is not self.tail:

            if cursor is n1: break
            if cursor is n2:
                n1, n2 = n2, n1
                break
            cursor = cursor.next

        # 找到n1左侧, n2右侧锚点
        n1_before = n1.prev
        n2_after = n2.next

        # 删除n1
        n1.prev.next = n1.next
        n1.next.prev = n1.prev

        # 删除n2
        n2.prev.next = n2.next
        n2.next.prev = n2.prev

        n1_after = n1_before.next
        n2_before = n2_after.prev

        # 插入n2到原n1位置
        n2.prev, n2.next = n1_before, n1_after
        n1_before.next, n1_after.prev = n2, n2

        # 插入n1到原n2位置
        n1.prev, n1.next = n2_before, n2_after
        n2_before.next, n2_after.prev = n1, n1


class PositionLinkedList(DoubleLinkedList):

    class Position:

        def __init__(self, container , node):
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

        return self._delete(p.node)

    def swap1(self, p, q):

        if not self.validate(p):
            raise IllegalPosition
        if not self.validate(q):
            raise IllegalPosition

        self._swap1(p.node, q.node)

    def swap2(self, p, q):

        if not self.validate(p):
            raise IllegalPosition
        if not self.validate(q):
            raise IllegalPosition

        self._swap2(p.node, q.node)

pl = PositionLinkedList()
print(list(pl))

p1 = pl.add_first(-1)
p2 = pl.add_last(10)
p3 = pl.add_first(-2)
p4 = pl.add_last(100)
p5 = pl.add_before(p2, 8)
p6 = pl.add_after(p1, -0.5)
p7 = pl.add_before(p3, -3)
p8 = pl.add_after(p4, 1000)
print(list(pl))

print(pl.first().e, pl.last().e)

print(pl.before(p1).e, pl.after(p8))

print(pl.delete(p1))
print(list(pl))

pl.swap1(p3, p4)
print(list(pl))
print(pl.after(p3).e, pl.before(p4).e)

pl.swap2(p3, p4)
print(list(pl))
print(pl.after(p3).e, pl.before(p4).e)
