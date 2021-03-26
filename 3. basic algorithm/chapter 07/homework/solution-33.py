# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    双向链表实现reverse(), 而不生成或破坏任何一个结点

    多少算破坏...

    思路1, 双指针前后对调值
    思路2, 每个结点交换prev, next, 然后交换head, tail

"""
class EmptyError(Exception):
    pass

class IllegalNode(Exception):
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

    def _add_after(self, left, e):

        if left not in self.nodes:
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
        if right not in self.nodes:
            raise IllegalNode

        if right is self.head:
            raise IllegalNode

        node = self.Node(e)

        left = right.prev

        node.prev, node.next = left, right
        left.next, right.prev = node, node

        self.nodes.add(node)

        return node

    def add_first(self, e):
        return self._add_after(self.head, e)

    def delete(self, node):

        if node not in self.nodes:
            raise IllegalNode

        if node in [self.head, self.tail]:
            raise IllegalNode

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = node.next = None

        self.nodes.remove(node)

        return node.e

    def reverse1(self):
        if self.empty(): return

        l, r = self.head.next, self.tail.prev

        p = set()

        while l not in p and r not in p:

            l.e, r.e = r.e, l.e

            p.add(l)
            p.add(r)

            l, r = l.next, r.prev

    def reverse2(self):

        if self.empty(): return

        cursor = self.head

        while cursor:

            cursor.prev, cursor.next = cursor.next, cursor.prev

            cursor = cursor.prev

        self.head, self.tail = self.tail, self.head


dl = DoubleLinkedList()
n = None
for i in range(10):
    n = dl.add_first(i)

print(list(dl))

print(dl.delete(n))
print(list(dl))

dl.reverse1()
print(list(dl))

dl.reverse2()
print(list(dl))

