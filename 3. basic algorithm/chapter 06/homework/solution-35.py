# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    栈, 有限大小
    栈满的时候入栈, 则底下漏出去一个

    ...这不就是个单侧的双向循环队列吗...
"""

class EmptyError(Exception):
    pass

class Stack:

    def __init__(self, c):
        self._data = [None]*c
        self._head = 0

        self._count = 0

    def empty(self):
        return self._count == 0

    # 哪边当栈顶是个问题
    # 还是头部吧, 少一步计算
    def push(self, e):

        if self._count != len(self._data):

            self._data[self._head] = e
            self._head = (self._head-1) % len(self._data)
            self._count += 1

        else:
            self._data[self._head] = e
            self._head = (self._head-1) % len(self._data)

    def top(self):
        if self.empty():
            raise EmptyError

        return self._data[(self._head+1) % len(self._data)]

    def pop(self):
        if self.empty():
            raise EmptyError

        p = (self._head+1) % len(self._data)

        res = self._data[p]
        self._data[p] = None

        self._head = p

        return res

    def show(self):
        print(self._data, self._head)

s = Stack(5); s.show()

s.push(1); s.show()
s.push(2); s.show()
s.push(3); s.show()
s.push(4); s.show()
s.push(5); s.show()
print(s.top(), s.pop())
s.show()