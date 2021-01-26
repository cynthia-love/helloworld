# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    位置双向链表排序
"""
import copy

class DoubleLinkedList:

    class _Node:

        __slots__ = '_e', '_prev', '_next'

        def __init__(self, e=None):
            self._e = e
            self._prev = None

            self._next = None

    def __init__(self):

        self._head = self._Node()
        self._tail = self._Node()

        self._head._next = self._tail
        self._tail._prev = self._head

        self._c = 0

    def __len__(self):
        return self._c

    def empty(self):
        return self._c == 0

    def _insert_between(self, left, right, e):

        node = self._Node(e)

        node._prev, node._next = left, right
        left._next, right._prev = node, node

        self._c += 1

        return node

    def _delete_node(self, node):

        node._prev._next = node._next
        node._next._prev = node._prev

        node._prev = node._next = None

        self._c -= 1

        return node._e

class PositionLinkedList(DoubleLinkedList):

    # 对外不暴露_node, 包一层再给外面
    # 注意, 只有元素才有位置概念
    class _Position:

        def __init__(self, container, node):

            self._container = container
            self._node = node

        @property
        def element(self):
            return self._node._e

        @element.setter
        def element(self, e):
            self._node._e = e

        def __eq__(self, other):

            if type(other) is not type(self):
                return False

            if other._container is not self._container:
                return False

            if other._node is not self._node:
                return False

            return True

    def _validate(self, p):

        if not isinstance(p, self._Position):
            return False

        if p._container is not self:
            return False

        return True

    def _n2p(self, node):

        if node in [self._head, self._tail]:
            return None

        return self._Position(self, node)

    def __iter__(self):
        cursor = self.first()

        while cursor:
            yield cursor.element
            cursor = self.after(cursor)

    # -------------------------------accessor----------------------------
    def first(self):
        return self._n2p(self._head._next)

    def last(self):
        return self._n2p(self._tail._prev)

    def before(self, p):
        if not self._validate(p):

            raise TypeError
        return self._n2p(p._node._prev)

    def after(self, p):
        if not self._validate(p):
            raise TypeError

        return self._n2p(p._node._next)

    # -------------------------------mutator----------------------------
    def add_first(self, e):

        return self._n2p(self._insert_between(self._head, self._head._next, e))

    def add_last(self, e):
        return self._n2p(self._insert_between(self._tail._prev, self._tail, e))

    def add_before(self, p, e):
        if not self._validate(p):
            raise TypeError

        return self._n2p(self._insert_between(p._node._prev, p._node, e))

    def add_after(self, p, e):
        if not self._validate(p):
            raise TypeError

        return self._n2p(self._insert_between(p._node, p._node._next, e))

    def add_between(self, left, right, e):
        # 若left为None, 认为是头部插入
        # 若right为None, 认为是尾部插入
        if not left:
            if right != self.first():
                raise ValueError
            else:
                return self.add_first(e)
        if not right:
            if left != self.last():
                raise ValueError
            else:
                return self.add_last(e)

        if not self._validate(left): raise TypeError
        if not self._validate(right): raise TypeError

        if not self.after(left) == right: raise ValueError

        return self._n2p(self._insert_between(left._node, right._node, e))

    def delete(self, p):
        if not self._validate(p):
            raise TypeError

        r = self._delete_node(p._node)

        p._container = p._node = None

        return r

    # -------------------------------sortor----------------------------
    def bubble_sort1(self):
        # 不动位置

        flag = self.last()  # 由于尾结点为None不好找前驱, 这里flag置为无序部分的最后一个结点

        first = self.first()

        while first != flag:

            p = first

            # 循环只到无序部分的倒数第二个结点
            while p != flag:

                q = self.after(p)

                if p.element > q.element:
                    p.element, q.element = q.element, p.element

                p = q

            flag = self.before(flag)

    def bubble_sort2(self):
        flag = None  # 这里最后两个元素有可能交换, 所以flag设置有序部分的最左一个而非无序最后一个

        while self.first() != flag:

            p = self.first()

            while self.after(p) != flag:

                q = self.after(p)

                if p.element > q.element:

                    self.add_between(self.before(p), p, self.delete(q))

                else:
                    p = q

            # 无论最后一步是否交换, 退出条件都是self.after(p) == flag
            flag = p

    def selection_sort1(self):

        flag = self.first()  # 标记无序部分左边界

        while flag != self.last():  # 知道选的只剩最后一个元素, 循环退出

            p = flag

            while p:

                if p.element < flag.element:
                    flag.element, p.element = p.element, flag.element

                p = self.after(p)

            flag = self.after(flag)

    def selection_sort2(self):
        flag = self.first()  # 无序部分的左界

        while flag != self.last():

            p = pmin = flag

            while p:

                if p.element < pmin.element:
                    pmin = p

                p = self.after(p)

            if pmin == flag:
                flag = self.after(flag)
            else:
                v = self.delete(pmin)
                self.add_before(flag, v)

    def insertion_sort(self):
        flag = self.first()  # 无序部分左边界

        while flag:  # 注意, 插入排序, 最后一个元素也要处理, 不像选择, 剩下那个就是其目标位置

            p = self.first()

            while p != flag:

                if p.element < flag.element:
                    p = self.after(p)
                else:
                    break

            # 如果循环正常退出, 即待插入元素比有序部分所有元素都大
            if p == flag:
                flag = self.after(flag)
            else:

                flag, v = self.after(flag), self.delete(flag)
                self.add_before(p, v)


pll = PositionLinkedList()
p1 = pll.add_first(1)
p2 = pll.add_last(2)
p3 = pll.add_before(p1, 8)
p4 = pll.add_after(p2, -8)
p5 = pll.add_after(p4, 1000)
p6 = pll.add_after(p5, 10)
pll.add_between(p2, p4, 16)

print(list(pll))

ll = copy.deepcopy(pll)
ll.bubble_sort1()
print(list(ll))

ll = copy.deepcopy(pll)
ll.bubble_sort2()
print(list(ll))

ll = copy.deepcopy(pll)
ll.selection_sort1()
print(list(ll))

ll = copy.deepcopy(pll)
ll.selection_sort2()
print(list(ll))

ll = copy.deepcopy(pll)
ll.insertion_sort()
print(list(ll))
