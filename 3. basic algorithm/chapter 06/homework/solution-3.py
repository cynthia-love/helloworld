# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现函数transfer(S, T), 将栈S的所有元素转移到栈T中, 转移后顺序倒转

    此例用固定大小的栈类

    栈和队列不同, 不会删除头部, 不存在元素移动, 所以不用头指针

    一个元素个数即可算出栈顶位置
"""

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Stack:

    def __init__(self, capacity):

        self._data = [None]*capacity

        self._n = 0

        # capacity可以通过len(self._data)获得
        # 就不要单独再去设置个变量了

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
        # 别忘了置None便于垃圾回收
        self._data[self._n-1] = None

        self._n -= 1

        return res

    def top(self):
        if self.empty():
            raise EmptyError

        return self._data[self._n-1]

    def show(self):
        print(self._data)

s = Stack(10)
s.push(1)
s.push(2)
s.push(3)
s.push(4)

s2 = Stack(10)

s.show()
s2.show()

while not s.empty():
    s2.push(s.pop())

s.show()
s2.show()

