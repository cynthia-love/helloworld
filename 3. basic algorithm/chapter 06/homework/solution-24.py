# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    描述如何用一个简单的队列作为实例变量实现堆栈
    在方法体中只有常量占用本地内存
    并评估push, pop, top的时间复杂度

"""
"""
    用队列实现栈???
    
    1
    12, push的时候得做处理, 把现有元素出队加到后面
    21, 遇到3, 21-3变成321
    
"""

from collections import deque

class EmptyError(Exception):
    pass

class Stack:

    def __init__(self):

        self._data = deque()

    def __len__(self):
        return len(self._data)

    def empty(self):
        return len(self) == 0

    def push(self, e):
        # 只能用popleft和append, O(n)
        self._data.append(e)
        for _ in range(len(self)-1):
            self._data.append(self._data.popleft())

    def pop(self):
        # O(1)
        if self.empty():
            raise EmptyError

        return self._data.popleft()

    def top(self):
        # O(1)
        if self.empty():
            raise EmptyError

        return self._data[0]

    def show(self):
        print(self._data)

s = Stack()
s.push(5); s.show()
s.push(3); s.show()
s.push(2); s.show()

while not s.empty():
    print(s.pop())
