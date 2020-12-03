# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个用于从栈中移除所有元素的递归方法
"""

from collections import deque

d = deque(i for i in range(10))

def f(dq: deque):
    if dq:
        dq.pop()
        f(dq)
f(d)
print(d)  # ???题目不是让做这吧, 应该是自实现clear算法

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Stack:
    def __init__(self, capacity):
        self._data = [None]*capacity

        self._n = 0

    def __len__(self):
        return self._n

    def empty(self):
        return self._n == 0

    def push(self, e):
        if self._n == len(self._data):
            raise FullError

        self._data[self._n] = e
        self._n += 1

    def pop(self):
        if self.empty():
            raise EmptyError

        res = self._data[self._n-1]

        self._data[self._n-1] = None

        self._n -= 1
        return res

    def top(self):
        if self.empty():
            raise EmptyError

        return self._data[self._n-1]

    def show(self):
        print(self._data)

    def clear(self):
        if self._n == 0: return
        self.pop()
        self.clear()

s = Stack(10)

for i in range(10):
    s.push(i)

s.show()

s.clear()
s.show()