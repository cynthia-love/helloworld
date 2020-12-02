# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    空栈执行如下操作, 分析输出情况
"""
class EmptyError(Exception):
    pass

class Stack:

    def __init__(self):

        self._data = []

    def __len__(self):
        return len(self._data)

    def empty(self):
        return len(self) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.empty():
            raise EmptyError

        return self._data.pop()

    def top(self):
        if self.empty():
            raise EmptyError

        return self._data[-1]

    def show(self):
        print(self._data)

s = Stack()

s.push(5); s.show()
s.push(3); s.show()
s.pop(); s.show()
s.push(2); s.show()
s.push(8); s.show()
s.pop(); s.show()
s.pop(); s.show()
s.push(9); s.show()
s.push(1); s.show()
s.pop(); s.show()
s.push(7); s.show()
s.push(6); s.show()
s.pop(); s.show()
s.pop(); s.show()
s.push(4); s.show()
s.pop(); s.show()
s.pop(); s.show()
