# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    之前的FavoritesListMTF移动元素是先把节点删了, 再根据其值进行新节点插入
    增加方法, 使得原节点直接移动到头部

    (不要去修改原有的delete, delete_node方法, 正常的删除还是要清理的)

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
            raise IllegalNode

        node = self.Node(e)

        right = left.next

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

    def _move_first(self, node):
        if not self._validate(node):
            raise IllegalNode

        if node in [self.head, self.tail]:
            raise IllegalNode

        node.prev.next = node.next
        node.next.prev = node.prev

        left, right = self.head, self.head.next

        node.prev, node.next = left, right
        left.next, right.prev = node, node

        return node

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
                raise IllegalPosition

            if other.container is not self.container:
                return False

            if other.node is not self.node:
                return False

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

    def move_first(self, p):

        if not self.validate(p):
            raise IllegalPosition

        return self.n2p(self._move_first(p.node))

class FavoritesList:

    class ElementType:

        __slots__ = 'value', 'count'

        def __init__(self, value, count=0):
            self.value = value
            self.count = count

    def __init__(self):
        self.data = PositionLinkedList()

    def __len__(self):
        return len(self.data)

    def empty(self):
        return self.data.empty()

    def __iter__(self):

        for each in self.data:

            yield each.value, each.count

    # 返回位置
    def find(self, value):

        cursor = self.data.first()

        while cursor:
            if cursor.element.value is value:
                return cursor

            cursor = self.data.after(cursor)

        return None

    def move(self, p):

        q = self.data.before(p)

        while q and q.element.count <= p.element.count:
            q = self.data.before(q)

        if not q:
            self.data.add_first(self.data.delete(p))

        else:
            self.data.add_after(q, self.data.delete(p))

    def access(self, v):

        p = self.find(v)

        if p:
            p.element.count += 1

        else:
            p = self.data.add_last(self.ElementType(v, 1))

        self.move(p)

    def remove(self, v):

        p = self.find(v)

        if p:
            self.data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise IndexError

        cursor = self.data.first()

        for i in range(k):
            yield cursor.element.value, cursor.element.count

            cursor = self.data.after(cursor)

class FavoritesListMTF(FavoritesList):

    def move(self, p):

        # self.data.add_first(self.data.delete(p))
        self.data.move_first(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise IndexError

        t = PositionLinkedList()

        for item in self.data:
            t.add_last(item)

        for i in range(k):
            cursor = highest = t.first()

            while cursor:
                if cursor.element.count > highest.element.count:
                    highest = cursor

                cursor = t.after(cursor)

            yield highest.element.value

            t.delete(highest)

fl = FavoritesListMTF()
fl.access('a')
fl.access('a')
fl.access('b')
fl.access('b')
fl.access('a')
fl.access('c')
fl.access('d')
fl.access('d')
fl.access('d')
fl.access('c')
print(list(fl))
print(list(fl.top(3)))