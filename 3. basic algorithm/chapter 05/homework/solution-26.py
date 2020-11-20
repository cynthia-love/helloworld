# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设B为数组, 恰有5个重复元素, 设计算法, 找出这5个重复的整数

"""
"""
    思路, 一次遍历, 哈希计数
"""
from collections import defaultdict

l = [1, 2, 3, 4, 4, 3, 2, 1, 1, 1, 1, 2, 1, 8, 9, 2, 2, 100]

dd = defaultdict(int)

for e in l:

    dd[e] += 1

for k, v in dd.items():
    if v == 5:
        print(k)
        break