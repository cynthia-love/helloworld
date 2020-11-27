# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    队列实现改进方法2-固定大小循环数组

    比如固定队列长度5

    1, 2, 3, 4, 5

    出两个变成:
          3, 4, 5

    再进一个新元素

    6,   3, 4, 5

    这种方法需要存储队首指针, 实际元素个数, 总空间大小
    插入的时候根据首指针, 实际元素个数, 总空间大小, 去算队尾插入位置

    另外, 这里我们只关心逻辑实现原理, 并不需要去研究实际占空间大小
    所以底层直接用list就行, 不需要用 (n*ctypes.py_object)()

    搞明白这几个值的关系:

    底层数组100->len(list) 60->实际元素个数20

    平时用list的时候, len(list)直接等价于元素个数

    而这里, 我们把len(list)作为数组大小, 实际元素个数通过自定义变量存储
"""

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Queue:
    CAPACITY = 5

    def __init__(self):
        self._data = [0]*Queue.CAPACITY
        # 循环队列里, 因为元素可以循环用
        # 头指针初始指向0, 不用指向-1
        # 首轮从1号位开始插入, 这样插入, 删除等指针移动逻辑更统一
        self._head = 0
        self._count = 0

    def __len__(self):
        return self._count

    def empty(self):
        return len(self) == 0

    def enqueue(self, e):
        if self._count == Queue.CAPACITY:
            raise FullError('Queue is full')

        """
        如果不满, 怎么计算插入位置, 以大小为5为例
        第一种情况:
        ↓
          0 1 2 3, -1+4+1 = 4
          
        第二种情况:
          ↓
          0 1 2 3 4, (0+4+1)%5 = 0
        
        """
        self._data[(self._head+self._count+1) % Queue.CAPACITY] = e
        self._count += 1

        print(self._data, self._head)

    def dequeue(self):
        if self.empty():
            raise EmptyError('Queue is empty')
        """
        删除元素需要移动队首指针, 还是以空间大小为5为例:
        情况1:
        ↓
          0 1 2 3 4, -1+1 = 0
        情况2:
                  ↓
          0 1 2 3 4
        情况2需要细致考虑
        比如0号位1号位都有元素, 删除一个, 显然head要指向0
        而如果只有0号位有元素有两种选择:
        (1) head指向0
        (2) head指向-1, 同时置count-1
        
        显然, 循环队列里, head初始指向-1并不是一个好的设计, 逻辑上不统一
        
        init里, 令head初始化为0, 而不是-1, 第一轮插入从1开始插入
        
        这样队首元素出队时head的变化逻辑就统一了
        self._head = (self._head+1) % Queue.CAPACITY
        
        """
        self._head = (self._head+1) % Queue.CAPACITY
        self._count -= 1

        print(self._data, self._head)
        return self._data[self._head]

    def first(self):
        if self.empty():
            raise EmptyError('Queue is empty')

        return self._data[(self._head+1) % Queue.CAPACITY]

    def __str__(self):

        res = []

        for i in range(self._count):
            res.append(self._data[(self._head+1+i) % Queue.CAPACITY])

        return ', '.join(str(e) for e in res)

q = Queue()
q.enqueue(1); print(q)
q.enqueue(2); print(q)
q.enqueue(3); print(q)
q.enqueue(4); print(q)
q.enqueue(5); print(q)
# q.enqueue(6)
print(q.dequeue()); print(q)
print(q.dequeue()); print(q)
q.enqueue(6); print(q)
print(q.dequeue()); print(q)
print(q.dequeue()); print(q)
print(q.dequeue()); print(q)
print(q.dequeue()); print(q)
# q.dequeue()
q.enqueue(7); print(q)