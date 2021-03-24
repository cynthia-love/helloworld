# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在一个单向链表上抽象操作, 以设计一个forward_list抽象数据结构

    类似于在双向链表上实现的PositionLinkedList

    补充个知识点:

    class A:
        def f():
            pass
        def g():
            self.f()

    class B(A):
        def f():
            pass

    注意, 对于类B的实例, 其调g函数, 里面的self.f()实际调的是子类的f而非父类的f
    所以子类轻易不要覆盖父类的同名方法

"""
class IllegalNode(Exception):
    pass

class IllegalPosition(Exception):
    pass

class LinkedList:

    class Node:

        __slots__ = 'e', 'next'

        def __init__(self, e=None):

            self.e = e
            self.next = None

    def __init__(self):
        self.head = self.Node()

        self.nodes = {self.head}

    def __iter__(self):
        cursor = self.head.next

        while cursor:
            yield cursor.e

            cursor = cursor.next

    def _validate(self, node):

        if node in self.nodes:
            return True

        return False

    def empty(self):
        return self.head.next is None

    def _add_after(self, left, e):

        if not self._validate(left):

            raise IllegalNode

        node = self.Node(e)

        node.next = left.next
        left.next = node

        self.nodes.add(node)

        return node

    def _del_after(self, left):

        if not self._validate(left):
            raise IllegalNode

        if not self._validate(left.next):
            raise IllegalNode

        node = left.next

        left.next = node.next
        self.nodes.remove(node)

        return node.e

class ForwardList(LinkedList):

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

        # 由于底层是单链表, 无尾结点, 需要对None特殊处理
        if node is None: return None

        if not self._validate(node):
            raise IllegalNode

        if node is self.head:
            return None

        else:
            return self.Position(self, node)

    def add_after(self, left, e):
        if not self.validate(left):
            raise IllegalPosition

        return self.n2p(self._add_after(left.node, e))

    def del_after(self, left):

        if not self.validate(left):
            raise IllegalPosition

        # 这里其实是有问题的, 如果外部已经有了对于
        # 下一个位置的引用, 那么是无法清理其信息的
        # 不过validate里加了node校验, 至少保证该引用后续不可用

        return self._del_after(left.node)

    # ===accessor===
    def first(self):
        return self.n2p(self.head.next)

    def after(self, left):

        if not self.validate(left):
            raise IllegalPosition

        return self.n2p(left.node.next)

    # ===mutator===
    def add_first(self, e):

        return self.n2p(self._add_after(self.head, e))

    def del_first(self):

        return self._del_after(self.head)

fl = ForwardList()
print(list(fl), fl.empty())
p1 = fl.add_first(1)
p2 = fl.add_first(-1)
p3 = fl.add_first(-2)
print(list(fl), fl.empty())
print(fl.del_after(p2))
print(list(fl), fl.empty())
p4 = fl.add_after(p2, 8)
print(p4.e)
print(list(fl), fl.empty())
print(fl.first().e)
print(fl.after(p3).e)
print(fl.del_first())
print(list(fl), fl.empty())
print(fl.del_after(p2))
print(list(fl), fl.empty())
print(fl.del_first())
print(list(fl), fl.empty())

