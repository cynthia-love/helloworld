# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现一个函数, 通过将一个列表内的元素顺序压入堆栈然后逆序写入列表
    从而实现列表元素的逆序

    1 2 3 4 5

    5
    4
    3
    2
    1

    5 4 3 2 1
"""
from collections import deque
l = [1, 2, 3, 4, 5]

d = deque()

for e in l:
    d.append(e)

for i in range(len(l)):

    l[i] = d.pop()

print(l)