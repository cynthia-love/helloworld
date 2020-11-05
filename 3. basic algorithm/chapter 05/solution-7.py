# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Python列表类
    摊销和时间分析
"""
import time

def f(n):
    vl = list()
    t1 = time.time()

    for i in range(n):
        vl.append(i)

    t2 = time.time()

    print((t2-t1)*1000000/n)

f(1000)  # 0.08
f(10000)  # 0.09
f(100000)  # 0.09
f(1000000)  # 0.09
# 说明单次append平均时间复杂度是O(1)的
