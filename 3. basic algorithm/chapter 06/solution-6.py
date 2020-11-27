# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    队列
    先进先出, FIFO, 比如游乐场排队, 队头出, 队尾进
    典型的应用场景有: 各种讲求先来后到的地方, 网络打印机, 响应请求的web服务器等
"""

"""
    队列的抽象类型支持的操作:
    
    enqueue(e), 队尾插入一个元素
    dequeue(), 队首出一个元素, 为空, 触发空错误
    first(), 查看队首的第一个元素, 不出队, 为空, 触发空错误
    empty(), 是否为空
    len(q), 返回队列中元素的数量
    
"""

# 最简单的实现思路, 借用适配器模式, 直接利用list的append和pop(0), 不限制大小
# 显然, 这种思路效率最差, 因为pop(0)

class EmptyError(Exception):
    pass

class Queue:
    """FIFO queue implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty queue"""
        self._data = list()

    def __len__(self):
        """Return the number of elements in the queue"""
        return len(self._data)

    def empty(self):
        """Return True if the queue is empty"""
        return len(self) == 0

    def enqueue(self, e):
        """Add an element to the back of queue"""

        self._data.append(e)

    def dequeue(self):
        """Remove and return the first element of queue
        Raise Empty Exception if the queue is empty"""

        if self.empty():
            raise EmptyError('Queue is empty')

        return self._data.pop(0)

    def first(self):
        """Return (but do not remove) the element at the front of the queue
        Raise Empty Exception if the queue is empty"""

        if self.empty():
            raise EmptyError('Queue is empty')

        return self._data[0]

    def __str__(self):
        return ', '.join(str(e) for e in self._data)

q = Queue()
q.enqueue(5); print(q)

q.enqueue(3); print(q)
print(len(q))

q.dequeue(); print(q)
print(q.empty())

q.dequeue(); print(q)
print(q.empty())

# q.dequeue()

q.enqueue(7)
q.enqueue(9)
print(q.first())

q.enqueue(4); print(len(q))

q.dequeue(); print(q)