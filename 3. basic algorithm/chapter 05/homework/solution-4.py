# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改自定义动态引用数组的__getitem__方法, 使其支持负索引
"""

import ctypes

class DynamicQuoteArray:
    """A Dynamic Quote Array class"""
    def __init__(self):
        """Create am empty array size of 1"""
        self.size = 1
        self.len = 0

        self.array = self.make_array(self.size)

    def __len__(self):
        """Return the number of elements stored in the array"""
        return self.len

    def __getitem__(self, k):
        """Return element at index k"""
        # 这里用self.len和len(self)都行
        # 加工k, 支持负值, -n对应0, -1对应n-1
        k = k if k >= 0 else self.len+k
        if not 0 <= k <= self.len:
            raise IndexError

        return self.array[k]

    def make_array(self, size):
        """Return new array with capacity size"""
        return (ctypes.py_object*size)()

    def resize(self):
        """Resize internal array to capacity self.size*2"""
        cur_array = self.array

        self.array = self.make_array(self.size*2)

        for i in range(self.len):
            self.array[i] = cur_array[i]

        self.size *= 2

    def append(self, obj):
        """Add object to the end of the array"""
        if self.len == self.size:
            self.resize()
        self.array[self.len] = obj
        self.len += 1

o = DynamicQuoteArray()

for i in range(100):
    print(o.len, o.size)
    o.append(i)

print(o[-1])
