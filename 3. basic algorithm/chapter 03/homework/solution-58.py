# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对解决元素唯一性的算法进行试验分析, 确定1分钟内能执行完的最大n
    1分钟就算了吧...1s吧
"""
import timeit
import random
from matplotlib import pyplot as pt

def f(n):
    s = [random.randint(1, n*100) for _ in range(n)]

    s.sort()  # n*log(n)

    for i in range(n-1):
        if s[i] == s[i+1]:
            return False

    return True

x = [_+10 for _ in range(1000)]
y = [timeit.timeit(stmt=lambda :f(_), number=1) for _ in x]

for i in range(555555, 10000000):
    t = timeit.timeit(stmt=lambda :f(i), number=1)
    print(t)
    if t >= 1:
        print(i)  # 555567
        break