# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    双向链表

    及基于双向链表的双端队列

    分析:
    1. 基于普通单向链表/循环单向链表的双端队列
    左插, 左删, 右插都是O(1), 但是右删, 由于找不到前驱节点, O(n)
    2. 基于双向链表的双端队列
    由于右侧能找到前驱节点, 所以删除也是O(1)

    另外, 双向链表设置头, 尾结点后, 可以实现逻辑一致的任意位置的O(1)插入和删除
    所以可以单独封装两个元素插入、删除底层函数为栈、队列等更高一级数据结构提供支持
"""

class EmptyError(Exception):
    pass

class DoubleLinkedList:

    class _Node:

        __slots__ = 'e', 'prev', 'next'

        def __init__(self, e=None):
            self.e = e
            self.prev = None
            self.next = None

    def __init__(self):
        # 设置头尾结点, 从而所有的插入、删除都是两元素之间, 即逻辑统一
        # 注意初始头、尾结点互指
        self._head = self._Node()
        self._tail = self._Node()

        self._head.next = self._tail
        self._tail.next = self._head

        self._c = 0

    def __len__(self):
        return self._c

    def _empty(self):
        return self._c == 0

    def _insert_between(self, e, left, right):
        node = self._Node(e)

        node.prev, node.next = left, right
        left.next, right.prev = node, node

        self._c += 1

        # 写底层支撑函数的时候注意, 不能操作完就完了
        # 要考虑到上层调用时可能需要拿到的东西, 返回之
        return node

    def _delete_node(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        self._c -= 1

        r = node.e

        # 彻底斩断关联, 需要都赋成None
        node.prev = node.next = node.e = None

        return r

    def show(self):
        p = self._head
        for i in range(self._c):
            p = p.next
            print(p.e, end=' ')
        print("")


class Deque(DoubleLinkedList):

    def add_left(self, e):
        # 即使为空, 下面这行逻辑也是适用的, 这就是为什么要同时设置头、尾结点
        self._insert_between(e, self._head, self._head.next)

    def left(self):
        if self._empty():
            raise EmptyError

        return self._head.next.e

    def del_left(self):
        if self._empty():
            raise EmptyError

        return self._delete_node(self._head.next)

    def add_right(self, e):
        self._insert_between(e, self._tail.prev, self._tail)

    def right(self):
        if self._empty():
            raise EmptyError
        return self._tail.prev.e

    def del_right(self):
        if self._empty():
            raise EmptyError

        return self._delete_node(self._tail.prev)

dq = Deque()
dq.add_left(1)
dq.add_right(2)
dq.show()
dq.add_left(11)
dq.add_right(22)
dq.show()
print(dq.left(), dq.right())
dq.del_left(); dq.show()
dq.del_right(); dq.show()
dq.del_left(); dq.show()
dq.del_right(); dq.show()
dq.add_left(8); dq.show()
dq.add_right(9); dq.show()

