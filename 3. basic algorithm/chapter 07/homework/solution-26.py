# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现单链表的拼接concatenate(Q2), 要求时间复杂度O(1), 拼接后Q2为空
"""

class EmptyError(Exception):
    pass

class IllegalNode(Exception):
    pass

class LinkedList:

    class Node:

        def __init__(self, e=None):
            self.e = e
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.nodes = {self.head}

    def __len__(self):
        return len(self.nodes)-1

    def empty(self):
        return len(self) == 0

    def __iter__(self):
        cursor = self.head.next

        while cursor:
            yield cursor.e
            cursor = cursor.next

    def _validate(self, node):
        if node not in self.nodes:
            return False

        return True

    def _add_after(self, left, e):

        if not self._validate(left):
            raise IllegalNode

        node = self.Node(e)

        node.next = left.next
        left.next = node

        self.nodes.add(node)

        return node

    def _delete_next(self, left):
        if not self._validate(left):
            raise IllegalNode

        if not left.next:
            raise IllegalNode

        node = left.next

        left.next = node.next
        self.nodes.remove(node)

        return node.e

    def add_first(self, e):

        return self._add_after(self.head, e)

    def delete_first(self):
        if self.empty():
            raise EmptyError

        return self._delete_next(self.head)

    def concatenate(self, ll2):

        if type(ll2) is not type(self):
            raise TypeError

        cursor = self.head

        while cursor.next:
            cursor = cursor.next

        cursor.next = ll2.head.next
        # 不设置nodes的话这里会简单很多
        # set交集&, 并集|, 差集-
        self.nodes = self.nodes | ll2.nodes-{ll2.head}

        ll2.head.next = None
        ll2.nodes = {ll2.head}

ll1 = LinkedList()
ll2 = LinkedList()

ll1.add_first(1)
ll1.add_first(-1)
ll1.add_first(-2)

ll2.add_first(8)
ll2.add_first(7)
ll2.add_first(6)

print(list(ll1))
print(list(ll2))

ll1.delete_first()
ll2.delete_first()
print(list(ll1))
print(list(ll2))

ll1.concatenate(ll2)
print(len(ll1))
print(len(ll2))
print(list(ll1))
print(list(ll2))