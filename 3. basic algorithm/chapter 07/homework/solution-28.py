# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个快速高效的逆置单链表的递归算法
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

        # h->1->2->3->4->5
        # 最快的方式应该是直接倒转指针

        if len(self) <= 1: return

        pre, p = self.head.next, self.head.next.next

        while p:

            pre2, p2 = p, p.next

            p.next = pre

            pre, p = pre2, p2

        self.head.next.next = None
        self.head.next = pre

    def reverse2(self):
        """
        递归思路
        1->2->3->4
           2->3->4
              3->4
                 4<-head
              3<-4<-head, 这里的4可以返回也可以上一级取next
           2<-3<-4<-head

        :return:
        """

        def rf(p):

            if not p.next:
                self.head.next = p
                p.next = None

            else:
                rf(p.next)
                p.next.next = p

                p.next = None

        rf(self.head.next)

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
ll.reverse2()
print(list(ll))