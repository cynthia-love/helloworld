# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    单链表排序
"""

class EmptyError(Exception):
    pass

class LinkedList:

    class _Node:

        def __init__(self, e=None):
            self._e = e
            self._next = None

    def __init__(self):

        self._head = self._Node()  # 头结点

        self._count = 0

    def __len__(self):
        return self._count

    def empty(self):
        return self._count == 0

    def __iter__(self):

        n = self._head
        for _ in range(self._count):

            n = n._next

            yield n._e

    def add_first(self, e):

        node = self._Node(e)

        node._next = self._head._next

        self._head._next = node

        self._count += 1

    def bubble_sort1(self):

        # x 个数冒泡 x-1 次即可
        # 下面这段代码本质上还是数组冒泡排序那一套思路
        for i in range(self._count-1):

            p = self._head._next
            for j in range(self._count-1-i):

                if p._e > p._next._e:
                    p._e, p._next._e = p._next._e, p._e

                p = p._next

    def bubble_sort2(self):

        # 试一下纯指针的写法, 当然还是换值不是换结点

        finished = None  # 代表最新的一个冒到顶的结点, 即有序的最左位置

        # 这里其实应该判断第二个元素
        # 如果判断第一个, 会多循环一次, 不过就不用特别判断空情况了
        while finished is not self._head._next:

            p = self._head._next

            while p._next is not finished:

                if p._e > p._next._e:
                    p._e, p._next._e = p._next._e, p._e

                p = p._next

                print(list(self))

            # 退出条件为, p._next为finished
            finished = p

    def selection_sort1(self):
        # 同样, 可以不动节点直接交换值

        def rf(left):
            if not left:
                return

            p = left

            # 遇到小的就和最左坑位值交换
            while p._next:
                p = p._next
                if p._e < left._e:
                    left._e, p._e = p._e, left._e

            rf(left._next)

        rf(self._head._next)

    def selection_sort2(self):

        # 单链表的结点删除需要存储指向上一个结点的指针而非指向目标结点的指针
        # 在这种情况下, 在原链表上同时做查找、删除、插入会很乱, 新设个头结点

        head2 = self._Node()

        # 只要原链表还有元素, 就继续循环
        while self._head._next:

            p = node_prev = self._head

            # 剩余大于等于2个元素
            while p._next._next:

                if p._next._next._e > node_prev._next._e:

                    node_prev = p._next

                p = p._next

            node = node_prev._next

            node_prev._next = node._next  # 从原链表中删除

            node._next = head2._next    # 插入新链表
            head2._next = node

        self._head = head2

    def insertion_sort(self):
        # 单链表不要直接在原结点上同时操作删除和插入
        head2 = self._Node()

        while self._head._next:

            node = self._head._next

            self._head._next = node._next  # 从原链中删掉结点

            p = head2

            while p._next and p._next._e < node._e:

                p = p._next

            # 循环退出条件为, p指向刚好大于node值的结点的上一个结点
            node._next = p._next
            p._next = node

        self._head = head2

ll = LinkedList()
ll.add_first(8)
ll.add_first(1)
ll.add_first(9)
ll.add_first(100)
ll.add_first(0)
ll.add_first(10)
print(list(ll))

# ll.bubble_sort1()
# print(list(ll))

# ll.bubble_sort2()
# print(list(ll))

# ll.selection_sort1()
# print(list(ll))

# ll.selection_sort2()
# print(list(ll))

ll.insertion_sort()
print(list(ll))



