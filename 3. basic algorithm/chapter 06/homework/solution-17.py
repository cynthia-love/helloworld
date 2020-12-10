# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    solution-16中的栈, 要么不限制大小由系统去扩展
    要么限制大小不能扩展

    现实现一种预分配大小但支持动态扩展的栈

    即把list.append的系统扩展工作自己去模拟实现

"""

class EmptyError(Exception):
    pass

class Stack:
    CAPACITY = 5

    def __init__(self):
        self._data = [None]*Stack.CAPACITY

        self._count = 0

    def __len__(self):
        return self._count

    def empty(self):
        return len(self) == 0

    def resize(self, c):
        data2 = [None]*c

        for i in range(len(self)):
            data2[i] = self._data[i]

        self._data = data2

    def push(self, e):

        if len(self) == len(self._data):
            self.resize(len(self._data)*2)

        self._data[self._count] = e
        self._count += 1

    def pop(self):
        if self.empty():
            raise EmptyError

        res = self._data[self._count-1]
        self._data[self._count-1] = None

        self._count -= 1

        if self._count <= len(self._data) / 4:

            self.resize(len(self._data) // 2)

        return res

    def top(self):
        if self.empty():
            raise EmptyError

        return self._data[self._count-1]

    def show(self):
        print(self._data)

s = Stack()
s.show()
s.push(1)
s.show()
s.push(2)
s.show()
s.push(3)
s.push(4)
s.push(5)
s.show()
s.push(6)
s.show()
print(s.top())
s.pop()
s.show()
s.pop()
s.show()
s.pop()
s.show()
s.pop()
s.show()