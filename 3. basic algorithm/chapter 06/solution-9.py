# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    队列实现改进方法3-可扩展/缩小的循环数组

    比如: 初始大小5
        ↓
    0 1 2 3 4

    假如append的时候发现满了, 即3-4-0-1-2

    动态扩展两倍

    0 1 2 3 4 5 6 7 8 9

    注意这里的扩展不能直接把0-4位置的元素复制到新的0-4
    而是要按照新的capacity插入5个元素的方式把原元素复制进去
      3 4 0 1 2
    0 1 2 3 4 5 6 7 8 9

    动态收缩时同理
"""

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Queue:

    CAPACITY = 5

    def __init__(self):
        self._data = [None]*Queue.CAPACITY

        self._head = 0  # 初始指向0比-1逻辑上更统一
        self._count = 0

    def __len__(self):
        return self._count

    def empty(self):
        return len(self) == 0

    # 满了就扩大两倍, 摊销时间复杂度O(1), 空间复杂度O(n)
    def enqueue(self, e):
        # 数组大小调整的时候不建议再用CAPACITY, 直接去改类变量会影响其他的实例初始化
        # 这里建议直接用len(self._data)去获取数组的空间大小
        if self._count == len(self._data):
            self.resize(len(self._data)*2)

        self._data[(self._head+1+self._count) % len(self._data)] = e

        self._count += 1

    # 删除要缩减, O(1), 空间复杂度O(n)
    # 注意, 如果不缩减, 那么会导致空间大小和当前元素个数脱节, 空间复杂度就不是O(n)了
    def dequeue(self):
        if self.empty():
            raise EmptyError('Queue is empty')

        self._head = (self._head+1) % len(self._data)
        # 这里一定要临时存储, 因为数组收缩后出队的值就没了
        res = self._data[self._head]
        # 把删除的数组元素置为None, 目的是去掉引用, 从而python可以对其进行垃圾回收
        self._data[self._head] = None

        self._count -= 1

        if self._count <= len(self._data) / 4:

            self.resize(len(self._data) // 2)

        return res

    def first(self):
        if self.empty():
            raise EmptyError('Queue is empty')

        return self._data[(self._head+1) % len(self._data)]

    def resize(self, c):

        data2 = [None]*c
        head2 = 0

        for i in range(self._count):

            data2[(head2+1+i) % c] = self._data[(self._head+1+i) % len(self._data)]

        self._data = data2
        self._head = head2

q = Queue()

for i in range(11):
    q.enqueue(i)
    print(q._count, q.CAPACITY)

for i in range(11):
    q.dequeue()
    print(q._count, q.CAPACITY)
# 这里的收缩最终会收缩到0元素-1 CAPACITY

for i in range(11):
    q.enqueue(i)
    print(q._count, q.CAPACITY)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(0)
print(q._data, q._count, q.CAPACITY)
q.dequeue()
print(q._data, q._count, q.CAPACITY)
q.enqueue(5)
print(q._data, q._count, q.CAPACITY)
q.enqueue(6)
print(q._data, q._count, q.CAPACITY)
q.dequeue()
print(q._data, q._count, q.CAPACITY)
q.dequeue()
print(q._data, q._count, q.CAPACITY)
q.dequeue()
print(q._data, q._count, q.CAPACITY)
q.dequeue()
print(q._data, q._count, q.CAPACITY)
