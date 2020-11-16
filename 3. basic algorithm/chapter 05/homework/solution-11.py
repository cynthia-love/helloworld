# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    计算nxn数组的和
"""

l = [[i for i in range(100)] for _ in range(100)]

res = 0
for i in range(100):
    for j in range(100):
        res += l[i][j]

print(res)