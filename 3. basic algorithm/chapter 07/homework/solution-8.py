# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    不采用计数器, 找到链表的中间节点
    双指针, 一个每次跳两步 一个每次跳一步
    ↓
    1-2-3-4-5
    ↑
        ↓
    1 2 3 4 5
      ↑
            ↓
    1 2 3 4 5
        ↑

            ↓
    1-2-3-4-5-6
        ↑

"""
class EmptyError(Exception):
    pass

class LinkedList:

    class _Node:

        def __init__(self, e=None):

            self._e = e
            self._next = None

    def __init__(self):
        self._head = self._Node()

        self._c = 0

    def __len__(self):
        return self._c

    def empty(self):
        return self._c == 0

    def __iter__(self):

        cursor = self._head

        while cursor._next:

            cursor = cursor._next
            yield cursor._e

    def _insert_after(self, left, e):
        node = e if isinstance(e, self._Node) else self._Node(e)

        node._next = left._next
        left._next = node

        self._c += 1

        return node

    def add_first(self, e):

        return self._insert_after(self._head, e)

    def get_middle(self):

        # O(n)

        if self.empty():
            raise EmptyError

        c2 = c1 = self._head._next

        while c2._next and c2._next._next:

            c2 = c2._next._next
            c1 = c1._next

        return c1._e

ll = LinkedList()
# ll.add_first(5)
# ll.add_first(4)
# ll.add_first(3)
# ll.add_first(2)
ll.add_first(1)
print(list(ll))
print(ll.get_middle())