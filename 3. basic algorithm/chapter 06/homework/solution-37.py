# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个双向栈, 一侧是红栈一侧是蓝栈, 栈操作带颜色参数
    用一个限定容量为N的单个数组来实现, 假定N始终大于红栈+蓝栈之和
"""

"""
    分析, 直接的思路是用中间作为栈底, 一个往上加, 一个往下加
    但是这么有个问题, 其中一个到头怎么办, 还得处理这种特殊逻辑
    
    进一步, 可以以0作为其中一个栈的栈底, -1作为另一个栈的栈底
    
"""

class EmptyError(Exception):
    pass

class DeStack:

    CAPACITY = 10

    def __init__(self):

        self._data = [None]*DeStack.CAPACITY

        self._headRed = 0
        self._headBlue = -1
        # 其实这俩不用存

        self._countRed = 0
        self._countBlue = 0

    def empty(self, color):

        if color == 'r':
            return self._countRed == 0
        else:
            return self._countBlue == 0

    def resize(self, c):
        data2 = [None]*c
        for i in range(self._countRed):
            data2[i] = self._data[i]

        for i in range(self._countBlue):
            data2[-1-i] = self._data[-1-i]

        self._data = data2

    def push(self, e, color):
        if self._countRed+self._countBlue >= len(self._data):
            self.resize(2*len(self._data))

        if color == 'r':
            self._data[self._headRed+self._countRed] = e

            self._countRed += 1

        else:
            self._data[self._headBlue-self._countBlue] = e
            self._countBlue += 1

    def pop(self, color):
        if self.empty(color):
            raise EmptyError

        if color == 'r':
            res = self._data[self._headRed+self._countRed-1]
            self._data[self._headRed + self._countRed - 1] = None

            self._countRed -= 1

        else:
            res = self._data[self._headBlue-self._countBlue+1]
            self._data[self._headBlue - self._countBlue + 1] = None

            self._countBlue -= 1

        if self._countRed+self._countBlue <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def top(self, color):
        if self.empty(color):
            raise EmptyError

        if color == 'r':
            return self._data[self._headRed+self._countRed-1]

        else:
            return self._data[self._headBlue-self._countBlue+1]

    def show(self):
        print(self._data, self._countRed, self._countBlue)

s = DeStack(); s.show()
s.push('red1', 'r'); s.show()
s.push('blue1', 'b'); s.show()
s.push('red2', 'r'); s.show()
s.push('blue2', 'b'); s.show()

s.pop('r'); s.show()
s.pop('b'); s.show()

s.push('red3', 'r'); s.show()
s.push('blue3', 'b'); s.show()

print(s.top('r'), s.top('b'))

s.push('red3', 'r'); s.show()
s.push('blue3', 'b'); s.show()
s.push('red3', 'r'); s.show()
s.push('blue3', 'b'); s.show()
s.push('red3', 'r'); s.show()
s.push('blue3', 'b'); s.show()

s.push('red5', 'r'); s.show()
s.push('blue5', 'b'); s.show()

s.pop('r'); s.show()
s.pop('b'); s.show()

s.pop('r'); s.show()
s.pop('b'); s.show()

s.pop('r'); s.show()
s.pop('b'); s.show()

s.pop('r'); s.show()
s.pop('b'); s.show()