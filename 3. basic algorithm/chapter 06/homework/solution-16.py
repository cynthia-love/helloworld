# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改基于数组的栈的实现方法,可选初始定义最大容量

    如果定义了, 那么栈满时抛异常
    如果没定义, 动态扩展

    关键, 把各操作甚至一些变量的逻辑全都用if else分俩分支

    比如self._count, 只在容量定义时用, 比混一起逻辑更清晰

"""

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Stack:

    def __init__(self, c=None):

        self._data = [None]*c if c else []

        self._c = c  # self._c存储最大支持空间

        self._count = 0

    # len()返回元素个数
    def __len__(self):
        if self._c:
            return self._count
        else:
            return len(self._data)

    def empty(self):
        return len(self) == 0

    def push(self, e):
        if self._c:
            if self._count == self._c:
                raise FullError

            else:
                self._data[self._count] = e
                self._count += 1

        else:

            self._data.append(e)

    def pop(self):
        if self.empty():
            raise EmptyError

        if self._c:

            res = self._data[self._count-1]
            self._data[self._count-1] = None

            self._count -= 1

            return res

        else:
            # 非限定大小的pop注意直接pop, 而不是只改count
            # 否则下次再append的时候会有问题
            return self._data.pop()

    def top(self):

        if self.empty():
            raise EmptyError

        if self._c:

            return self._data[self._count-1]

        else:

            return self._data[-1]

    def show(self):
        print(self._data)

s = Stack()
for i in range(100):
    s.push(i)

s.show()

for i in range(50):
    s.pop()

s.show()

print(s.top())


s2 = Stack(3)
s2.push(1)
s2.push(2)
s2.show()
s2.push(3)
s2.show()
# s2.push(4)
print(s2.top())

s2.pop()
s2.show()
