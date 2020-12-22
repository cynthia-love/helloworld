# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    使用两个栈实现队列, 使得队列操作的平均时间开销为O(1)
"""

"""
    分析
    
    最直接的思路
    
    1
    2来了, 借助栈2清空栈1, 2 1
    3来了, 借助栈2清空栈1, 入3, 栈2是12, 再放回去, 3 2 1
    
    但是这种入队操作为O(n), 显然不符合要求
    
    更优的思路:
    插入
    1
    插入
    1 2
    插入
    1 2 3
    出
    -                   3 2-1
    出
    -                   3-2
    入
    4                   3
    入
    4 5                 3
    出
    4 5                 -
    出
    -                   5-4
    看出什么了?
    即备用栈不是简单地作为翻转栈,而是作为出栈
    翻过去之后就不翻回去了, 等着出
    如果没了, 再从入栈里翻一些进去
    
    怎么证明是O(1)???
    首先, enqueue肯定是O(1)
    当self._out里有值时dequeue和head是O(1)
    当self._out里没有值时: 假设当前k个, 则该k个会摊销到k次dequeue中去
    其dequeue为O(2)
    
"""

class EmptyError(Exception):
    pass

class Queue:

    def __init__(self):
        self._data = list()
        self._assist = list()

    def __len__(self):
        return len(self._data)

    def empty(self):
        return len(self) == 0

    def enqueue(self, e):
        while self._data:
            self._assist.append(self._data.pop())

        self._data.append(e)

        while self._assist:
            self._data.append(self._assist.pop())

    def dequeue(self):
        if self.empty():
            raise EmptyError

        return self._data.pop()

    def head(self):
        if self.empty():
            raise EmptyError

        return self._data[-1]

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.head())
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())

class Queue:

    def __init__(self):
        self._in = list()
        self._out = list()

    def __len__(self):
        return len(self._in)+len(self._out)

    def empty(self):
        return len(self) == 0

    def enqueue(self, e):
        self._in.append(e)

    def dequeue(self):
        if self.empty():
            raise EmptyError

        if self._out:
            return self._out.pop()

        while self._in:
            self._out.append(self._in.pop())

        return self._out.pop()

    def head(self):
        if self.empty():
            raise EmptyError

        if self._out:
            return self._out[-1]

        while self._in:
            self._out.append(self._in.pop())

        return self._out[-1]

    def show(self):
        print(self._in, self._out)

print("=====")
q = Queue()
q.enqueue(1); q.show()
q.enqueue(2); q.show()
q.enqueue(3); q.show()
q.head(); q.show()
q.enqueue(4); q.show()
q.enqueue(5); q.show()
print(q.dequeue()); q.show()
print(q.dequeue()); q.show()
print(q.dequeue()); q.show()
q.enqueue(6); q.show()
print(q.dequeue()); q.show()
print(q.dequeue()); q.show()
print(q.dequeue()); q.show()
q.enqueue(7); q.show()
