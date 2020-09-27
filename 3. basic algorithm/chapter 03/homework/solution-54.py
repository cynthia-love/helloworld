# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    序列S包含n个整数, 整数范围[0, 4n], 可以有重复值
    设计一个算法, 找出其中出现次数最多的值k
"""

"""
    扫描一遍统计, 再来一遍取最大, 2*n, O(n)
"""

def f1():
    s = [1, 2, 3, 4, 3, 2, 1, 2]
    d = [0]*(len(s)+1)

    for each in s:
        d[each] += 1

    vmax, imax = -1, -1

    for i in range(len(d)):
        if d[i] > vmax:
            vmax, imax = d[i], i

    print(imax)

f1()