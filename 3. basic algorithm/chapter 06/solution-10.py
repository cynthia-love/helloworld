# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    双端队列, double-ended queue, 简写deque

    并不是栈+队列
    栈: 尾进尾出, 队列: 尾进头出
    而双端队列是两边都能进都能出

"""
"""
    双端队列的ADT
    add_left(e)
    pop_left()
    left()
    add_right(e)
    pop_right()
    right()
    
    empty()
    len(d)
"""
"""
    实现方案:
    类似队列实现改进方法3-可扩展/缩小的循环数组
    
    注意, 头部, 尾部, 元素个数三个存其二即可算出来剩下那个
    
    建议存头部, 元素个数, 逻辑上更好理解
"""

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Deque:
    CAPACITY = 5

    def __init__(self):
        self._data = [None]*Deque.CAPACITY
        # 注意, 头部, 尾部, 元素个数三个存其二即可算出来剩下那个
        # 不要三个都存, 容易出现conflict
        self._head = 0
        self._count = 0

    def __len__(self):
        return self._count

    def empty(self):
        return self._count == 0

    def add_left(self, e):
        # 队首插入, 由于头指针指向当前元素的上一个位置
        # 所以直接在队首位置插入, 并把头指针前移一位
        if self._count == len(self._data):
            self.resize(2*len(self._data))

        self._data[self._head] = e
        self._head = (self._head-1) % len(self._data)
        self._count += 1  # 插入完别忘了计数+1

    def pop_left(self):
        if self.empty():
            raise EmptyError('DeQue is empty')

        # 队首出队, 队首指针的下一位为待出元素
        # 考虑回收机制要设置None, 且有数组收缩的情况, 把该元素赋给个临时变量
        res = self._data[(self._head+1) % len(self._data)]
        self._data[(self._head + 1) % len(self._data)] = None
        self._head = (self._head+1) % len(self._data)

        # 出队处理完之后, 再去看是否要收缩
        if self._count <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def left(self):
        if self.empty():
            raise EmptyError('Deque is empty')

        return self._data[(self._head+1) % len(self._data)]

    def add_right(self, e):
        if self._count == len(self._data):
            self.resize(2*len(self._data))

        # 右插入, 头指针不移动
        self._data[(self._head+self._count+1) % len(self._data)] = e
        self._count += 1

    def pop_right(self):
        if self.empty():
            raise EmptyError('Deque is empty')

        # 注意, 最右元素的位置是self._head+self._count
        res = self._data[(self._head+self._count) % len(self._data)]

        # 置None以方便垃圾回收
        self._data[(self._head + self._count) % len(self._data)] = None

        self._count -= 1

        if self._count <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def right(self):
        if self.empty():
            raise EmptyError('Deque is empty')
        return self._data[(self._head+self._count) % len(self._data)]

    def resize(self, c):
        data2 = [None]*c
        head2 = 0  # 头指针指向0, 表示从1号位开始插入

        for i in range(self._count):
            data2[(head2+1+i) % c] = self._data[(self._head+1+i) % len(self._data)]

        self._data = data2
        self._head = head2

    def show(self):
        print(self._data, [self._data[(self._head+1+i) % len(self._data)] for i in range(self._count)])

dq = Deque()

dq.add_right(5); dq.show()
dq.add_left(3); dq.show()
dq.add_left(7); dq.show()
print(dq.left())
dq.pop_right(); dq.show()
print(len(dq))
dq.pop_right(); dq.show()
dq.pop_right(); dq.show()
dq.add_left(6); dq.show()
print(dq.right())
dq.add_left(8); dq.show()
print(dq.empty())
print(dq.right())
