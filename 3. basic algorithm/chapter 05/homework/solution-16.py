# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现DynamicArray的pop方法
    每当元素小于n/4时, 将数组大小缩小为原来的一半
"""

import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1

        self._A = self._make_array(self._capacity)

    def _make_array(self, c):

        return (c*ctypes.py_object)()

    def _resize(self, c):

        B = self._make_array(c)

        for i in range(self._n):
            B[i] = self._A[i]

        self._A = B
        self._capacity = c

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k <= self._n-1:
            raise IndexError

        return self._A[k]

    def append(self, obj):

        if self._n == self._capacity:
            # 这里capacity重新赋值在resize里做了
            self._resize(self._capacity*2)

        self._A[self._n] = obj

        self._n += 1

    def pop(self):

        self._A[self._n] = None
        self._n -= 1

        if self._n < self._capacity/4:
            self._resize(self._capacity//2)


o = DynamicArray()

for i in range(100):
    o.append(i)
    print(o._n, o._capacity)


print('===')

for i in range(100):
    o.pop()
    print(o._n, o._capacity)

# 32-128, 31-64
# 31小于1/4*capacity, 缩小为64
# 4-16, 3-8, 1-4, 0-2
# 由于始终是小于1/4*n才缩小到1/2*n, 不会出现元素较小的时候空间比元素个数小
