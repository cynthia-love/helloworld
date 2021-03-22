# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    非递归, 固定空间, 实现单链表逆置

    (其实solution-28已经实现了)
"""

class EmptyError(Exception):
    pass

class LinkedList:

    class Node:

        def __init__(self, e=None):
            self.e = e
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.c = 0

    def __len__(self):

        return self.c

    def empty(self):
        return self.c == 0

    def __iter__(self):
        cursor = self.head.next

        while cursor:
            yield cursor.e

            cursor = cursor.next

    def _add_after(self, left, e):

        node = self.Node(e)

        node.next = left.next
        left.next = node

        self.c += 1

        return node

    def _delete_next(self, left):

        node = left.next

        left.next = node.next

        self.c -= 1

        return node.e

    def add_first(self, e):

        return self._add_after(self.head, e)

    def delete_first(self):
        if self.empty():
            raise EmptyError

        return self._delete_next(self.head)

    def reverse(self):

        if self.c <= 1: return

        # h->4->3->2->1

        pre = self.head.next
        p = pre.next

        while p:

            pre2, p2 = p, p.next

            p.next = pre

            pre, p = pre2, p2

        self.head.next.next = None

        # 注意循环退出条件为p为None, 这里要指向pre
        self.head.next = pre

ll = LinkedList()
ll.add_first(1)
ll.add_first(2)
ll.add_first(3)
ll.add_first(4)
ll.add_first(5)
ll.delete_first()
print(list(ll))
ll.reverse()
print(list(ll))

