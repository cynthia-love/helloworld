# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    用单向链表实现栈
"""

class EmptyError(Exception):
    pass

class Stack:

    class _Node:
        """
        由于结点数量可能会非常多
        这里把e和next声明为slots, 这样就不会每个实例生成个__dict__了

        slots声明, 用descriptor代替__dict__
        1. 可以提升属性访问速度
        正常情况下, o.x -> o.__dict__ -> o.__dict__['x']->结果
        slots情况下: o.x -> descriptor直接get->结果
        比正常情况下少了o.__dict__['x']这步, 一个哈希函数的速度消耗

        2. 减少内存消耗
        __dict__是一个哈希表, 哈希以空间换时间, 当字典使用量超过2/3时
        python会根据情况进行2-4倍的扩容, 所以取消__dict__的使用可以大幅减少空间消耗

        """
        __slots__ = ['e', 'next']

        def __init__(self, e=None):
            self.e = e
            self.next = None

    def __init__(self):
        # 带头结点
        self._head = self._Node()
        self._c = 0

    def empty(self):
        return self._c == 0

    def push(self, e):
        node = self._Node(e)
        node.next = self._head.next
        self._head.next = node
        self._c += 1

    def pop(self):
        if self.empty():
            raise EmptyError

        r = self._head.next

        self._head.next = self._head.next.next

        self._c -= 1

        return r.e

    def top(self):
        if self.empty():
            raise EmptyError

        return self._head.next.e

s = Stack()
s.push(1)
s.push(2)
print(s.top())
s.push(3)
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())
s.pop()
# print(s.top())
