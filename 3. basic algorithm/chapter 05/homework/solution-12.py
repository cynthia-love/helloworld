# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    计算nxn数组的和

    利用sum, 一行实现
"""

l = [[i for i in range(100)] for _ in range(100)]

print(sum(sum(e) for e in l))