# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    链表

    数组利用一个大的内存块为许多元素提供存储(直接存值或存指向该元素的指针/引用)

    而链表, 采用称作节点的轻量级对象, 每个节点维护元素值或指向该元素的指针/引用
    外加一个或多个指向相邻节点的指针/引用

"""

"""
    单向链表
    
"""

class EmptyError(Exception):
    pass

# 最简单的单向链表, 无头结点, 无尾指针, 无计数器
class LinkedList:

    class Node:

        def __init__(self, e):
            self.e = e
            self.next = None

    def __init__(self):

        self._head = None

    def add_first(self, e):
        node = LinkedList.Node(e)

        # 无头结点, head指向第一个元素或None
        # 不涉及head.next, 无需特殊处理为空的情况
        node.next = self._head
        self._head = node

    def del_first(self):
        # 为空抛异常
        if not self._head:
            raise EmptyError

        # 至少有一个元素, head指向第一个
        res = self._head.e
        self._head = self._head.next

        return res

    def first(self):
        # 为空抛异常
        if not self._head:
            raise EmptyError

        return self._head.e

    def add_last(self, e):
        node = LinkedList.Node(e)

        # 涉及p.next判断, 要处理空的情况
        if not self._head:
            self._head = node

        else:
            # 退出条件为, p没有下一个, 即p是最后一个元素
            p = self._head
            while p.next:
                p = p.next

            p.next = node

    def del_last(self):
        # 为空抛异常
        if not self._head:
            raise EmptyError

        # 由于删除要找到倒数第二个元素
        # 所以只有一个元素的情况也得特殊处理
        if not self._head.next:
            self._head = None

        else:
            # 退出条件为p的下一个为最后一个元素, 即p倒数第二
            p = self._head
            while p.next.next:
                p = p.next

            p.next = None

    def last(self):
        # 为空抛异常
        if not self._head:
            raise EmptyError

        # 只是获取最后一个元素值, 找倒数第一个元素接口
        p = self._head
        while p.next:
            p = p.next

        return p.e

    def show(self):

        p = self._head

        while p:
            print(p.e, end=', ')
            p = p.next

        print('')

ll = LinkedList(); ll.show()
ll.add_first('left1'); ll.show()
ll.add_first('left2'); ll.show()
ll.add_first('left3'); ll.show()
ll.add_last('right1'); ll.show()
ll.add_last('right2'); ll.show()
ll.add_last('right3'); ll.show()
print(ll.first(), ll.last())
ll.del_first(); ll.show()
ll.del_last(); ll.show()
ll.del_first(); ll.show()
ll.del_first(); ll.del_first()
ll.show()

print("======")

# 更方便的单向链表, 加入头结点, 尾指针, 计数器
# 不建议设置这么多, 连带修改需要考虑的特殊情况太多
# 建议只设置一个头结点就行
class LinkedList:

    class Node:

        def __init__(self, e=None):

            self.e = e
            self.next = None

    def __init__(self):

        self._head = LinkedList.Node()

        self._tail = self._head

        self._count = 0

    def empty(self):
        return self._count == 0

    def add_first(self, e):
        node = LinkedList.Node(e)

        # 如果初始为空, 需要把尾指针指过去
        if self._count == 0:
            self._tail = node

        node.next = self._head.next
        self._head.next = node
        self._count += 1

    def del_first(self):
        # 为空抛异常
        if self.empty():
            raise EmptyError

        # 如果只有一个元素, 别忘了把尾指针前移, 否则不动
        if self._count == 1:
            self._tail = self._head

        # 这里至少一个元素, 所以self._head.next和.next.next都可以取到
        res = self._head.next.e

        self._head.next = self._head.next.next

        self._count -= 1

        return res

    def first(self):
        if self.empty():
            raise EmptyError

        return self._head.next.e

    def add_last(self, e):
        # tail指向最后一个元素或头结点
        # 两种情况处理逻辑一样
        node = LinkedList.Node(e)

        self._tail.next = node
        self._tail = node

        self._count += 1

    def del_last(self):
        if self.empty():
            raise EmptyError

        # 删最后一个还是得从头遍历
        # 找倒数第二个结点
        # 这里不为空, 算上头结点, 至少有俩结点
        p = self._head

        # 退出条件为p的下一个元素为倒数第一个, 即p倒数第二个
        # p可能为头结点, 处理逻辑一样
        while p.next.next:
            p = p.next

        res = p.next.e
        p.next = None

        # 别忘了尾指针前移
        self._tail = p

        self._count -= 1

        return res

    def last(self):
        if self.empty():
            raise EmptyError

        return self._tail.e

    def show(self):

        p = self._head
        for _ in range(self._count):

            p = p.next

            print(p.e, end=' ')

        print('')


ll = LinkedList(); ll.show()
ll.add_first('left1'); ll.show()
ll.add_first('left2'); ll.show()
ll.add_first('left3'); ll.show()
ll.add_last('right1'); ll.show()
ll.add_last('right2'); ll.show()
ll.add_last('right3'); ll.show()
print(ll.first(), ll.last())
ll.del_first(); ll.show()
ll.del_last(); ll.show()
ll.del_first(); ll.show()
ll.del_first(); ll.del_first()
ll.show()
# ll.del_first(); print(ll._count)
ll.del_last(); print(ll._count)

ll.add_first('l1'); ll.add_first('l2')
ll.add_last('r1'); ll.add_last('r2')
ll.show()

