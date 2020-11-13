# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改solution-1中的代码
    仅当列表需要扩展时, 才输出当前要插入的索引值
    0, 4, 8, 16, 25...
"""

import sys

l = list()

for i in range(100):

    s1 = sys.getsizeof(l)
    l.append(i)
    s2 = sys.getsizeof(l)

    if s2 > s1: print(i)