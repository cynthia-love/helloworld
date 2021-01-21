# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    双链表排序
"""
import copy
class EmptyError(Exception):
    pass

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

    def _empty(self):
        return self._c == 0

    def _insert_between(self, left, right, e):

        # 有时是直接插入结点, 而非传值, 注意兼容
        node = self._Node(e) if not isinstance(e, self._Node) else e

        node._prev, node._next = left, right

        left._next, right._prev = node, node

        self._c += 1

        return node

    def _delete_node(self, node):

        node._prev._next = node._next
        node._next._prev = node._prev

        self._c -= 1

        r = node._e

        node._prev = node._next = None  # 有时候结点删除后还要插入, e值不要改了

        return r

    def add_left(self, e):

        return self._insert_between(self._head, self._head._next, e)

    def __iter__(self):

        node = self._head._next

        for _ in range(self._c):

            yield node._e

            node = node._next

    def bubble_sort1(self):
        # 双向链表不用考虑'上一个结点'的问题
        flag = self._tail

        # 只要第一个元素还没有进入右边有序部分, 继续循环
        while self._head._next != flag:

            p = self._head._next

            # 内层循环处理到有序最左元素的上上个元素
            while p._next != flag:

                if p._e > p._next._e:
                    p._e, p._next._e = p._next._e, p._e

                p = p._next

            flag = flag._prev  # 双向链表左移flag很方便

    def bubble_sort2(self):
        # 尝试一下交换结点而非值
        flag = self._tail

        while self._head._next != flag:

            p = self._head._next

            # 没到有序部分左界才继续循环
            # 即退出条件为: p._next == flag
            while p._next != flag:

                if p._e > p._next._e:

                    # 交换结点而非值, 删左往右插
                    next = p._next
                    self._delete_node(p)
                    self._insert_between(next, next._next, p)
                    # 注意这种情况, p已经移到右边去了
                else:
                    p = p._next

            flag = flag._prev

    def selection_sort1(self):
        # 先试下换值不换结点
        # 这里left为无序部分的第一个位置
        left = self._head._next

        while left != self._tail:

            p = left

            while p._next != self._tail:

                p = p._next

                # 这里也可以不每次都换, 找到最小后再和最左换
                if p._e < left._e:
                    left._e, p._e = p._e, left._e

            left = left._next  # 指向下一个待定位置

    def selection_sort2(self):
        # 记左侧有序部分最后一个位置
        left = self._head

        # 注意有尾结点, 判断最后一个元素不能用None
        while left._next != self._tail:

            m = p = left._next

            while p._next != self._tail:
                p = p._next
                if p._e < m._e:
                    m = p
            # 得到右边最小的结点

            self._delete_node(m)

            self._insert_between(left, left._next, m)

            left = left._next  # left指向新的有序部分最后结点

    def insertion_sort(self):
        # 双向链表没必要再整个新头结点
        flag = self._head  # flag有序部分的最后一个结点, flag._next为无序部分的第一个元素

        while flag._next != self._tail:

            node = flag._next

            self._delete_node(node)

            p = self._head._next  # 从有序部分的第一个元素开始, 一直比到最后一个

            while p != flag._next:

                if p._e < node._e:
                    p = p._next
                else:
                    break

            else:
                # 如果循环正常退出, 说明p指向了有序部分的下一个位置, 那么下一次循环flag指向拼接的node
                # 如果非正常退出, 说明往有序部分中间查, 那么flag的位置不变
                flag = node

            # 循环退出条件, p为第一个大于node的位置或者到了有序部分的下一个位置
            self._insert_between(p._prev, p, node)


dll = DoubleLinkedList()

dll.add_left(10)
dll.add_left(12)
dll.add_left(100)
dll.add_left(-1)
dll.add_left(8)
dll.add_left(13)

ll = copy.deepcopy(dll)
ll.bubble_sort1()
print(list(ll))

ll = copy.deepcopy(dll)
ll.bubble_sort2()
print(list(ll))

ll = copy.deepcopy(dll)
ll.selection_sort1()
print(list(ll))

ll = copy.deepcopy(dll)
ll.selection_sort2()
print(list(ll))

ll = copy.deepcopy(dll)
ll.insertion_sort()
print(list(ll))