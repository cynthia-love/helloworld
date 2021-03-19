# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出实现单链表的递归算法

    这里有点绕, 普通的单链表区分链表类和节点类
    而递归单链表不区分, 比如:
    1->2->3->4

    = 存储1+链表2->3->4

    这里LinkedList直接指向自己, 所以不要设置头结点

"""

class LinkedList:

    def __init__(self, e):

        self.e = e
        self.next = None

    def __iter__(self):

        yield self.e

        if self.next:
            # yield from x表示从x的迭代器里返回
            yield from self.next

    # 单次拼接
    def append(self, e):

        if not self.next:
            self.next = LinkedList(e)
        else:
            # 有下一个结点, 调下一个结点的append
            # 直到找到尾结点
            self.next.append(e)

    # 一次性构建
    def extend(self, es):

        def f(t, k):

            if not es[k:]: return

            t.next = LinkedList(es[k])

            f(t.next, k+1)

        f(self, 0)

es = [1, 8, 10, 100, 2000]
ll1 = LinkedList(-1)

for e in es: ll1.append(e)
print(list(ll1))

ll2 = LinkedList(-1)
ll2.extend(es)
print(list(ll2))