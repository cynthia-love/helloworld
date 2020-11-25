# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对solution-1中自定义的栈进行改进, 固定大小, 而不是动态扩展
"""

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Stack:

    def __init__(self, capacity):

        self._data = [0]*capacity

        self._c = capacity
        self._n = 0

    def __len__(self):

        return self._n

    def empty(self):

        return self._n == 0

    def push(self, e):

        if self._n == self._c:
            raise FullError

        self._data[self._n] = e
        self._n += 1

    def pop(self):

        if self.empty():
            raise EmptyError

        res = self._data[self._n - 1]

        self._data[self._n - 1] = 0  # 这一步不赋值0也可以

        self._n -= 1

        return res

    def top(self):

        if self.empty():
            raise EmptyError

        return self._data[self._n-1]

    def __str__(self):

        return ', '.join(str(e) for e in self._data[:self._n])


s = Stack(10)

s.push(5)
print(s)
s.push(3)
print(s)
print(len(s))
s.pop()
print(s)
print(s.empty())
s.pop()
print(s.empty())
# s.pop()
s.push(7)
s.push(9)
print(s.top())
print(s)
s.push(4)
print(s)
print(len(s))
print(s.pop())
print(s)
s.push(6)
s.push(8)
print(s)
s.pop()
print(s)