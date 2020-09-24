# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    从n个数字中找到最大值和最小值, 要求比较次数少于3n/2

    外层n, 意味着每次比较小于1.5次
"""

def f():
    l = [1, 2, 8, 100, -19, -2, 3]

    vmax, vmin = l[0], l[0]

    for i in range(2, len(l)):
        if l[i] >= vmax:  # 1/2*1
            vmax = l[i]
        elif l[i] <= vmin:  # 1/2*2
            vmin = l[i]

