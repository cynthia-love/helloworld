# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    重写自定义动态引用数组的insert的方法, 使得大小调整的时候新元素就插入完毕而不是复制+插入两遍O(n)
"""

import ctypes

class DynamicQuotedArray:

    def __init__(self):

        self._n = 0
        self._size = 1

        self._array = self.make_array(self._size)

    def make_array(self, size):

        return (size*ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k <= self._n-1:
            raise IndexError
        return self._array[k]

    def resize(self):
        cur = self.make_array(self._size*2)
        for i in range(self._n):
            cur[i] = self._array[i]

        self._array = cur
        self._size *= 2

    def append(self, obj):
        if self._n == self._size:
            self.resize()

        self._array[self._n] = obj
        self._n += 1

    def insert(self, index, obj):
        """
        0, 1, 2, 3, 4
        :param index:
        :param obj:
        :return:
        """
        # 如果元素没满, 直接把索引 >= index的元素右移一位, 最后空出来index
        if not self._n == self._size:
            for i in range(self._n-1, index-1, -1):
                self._array[i+1] = self._array[i]

            self._array[index] = obj
            self._n += 1

        else:
            # 如果元素满了, 扩展的同时把元素插进去
            self._size *= 2
            cur_array = self.make_array(self._size)

            # 0, 1, 2, 3, 4, 比如插入3号位, 0, 1, 2, 8, 3, 4
            # 则先复制0-2位置的元素
            for i in range(index):
                cur_array[i] = self._array[i]
            # 把3号位赋值为新的元素
            cur_array[index] = obj
            # 再复制剩余部分, 新数组的i位置对应老数组的i-1位置
            for i in range(index+1, self._n+1):
                cur_array[i] = self._array[i-1]
            self._array = cur_array
            self._n += 1

o = DynamicQuotedArray()
o.append(1)
o.append(2)
o.append(3)
o.insert(0, 8)
o.insert(0, 88)
for i in range(len(o)):
    print(o[i])
