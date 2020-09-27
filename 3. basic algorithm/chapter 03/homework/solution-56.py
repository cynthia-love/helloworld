# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对以下几个函数进行试验分析
"""
import math
import random
import timeit
from matplotlib import pyplot as pt

def f1(n):
    S = [random.random() for _ in range(n)]
    total = 0  # 1
    for j in range(n):
        total += S[j]  # n*1
    return total  # 1

def f2(n):
    S = [random.random() for _ in range(n)]
    total = 0  # 1

    for j in range(0, n, 2):
        total += S[j]  # n/2*1

    return total  # 1

def f3(n):
    S = [random.random() for _ in range(n)]

    total = 0  # 1

    for j in range(n):
        for k in range(1+j):
            total += S[k]  # 1, 2, 3, n

    return total  # 1

def f4(n):
    S = [random.random() for _ in range(n)]

    prefix = 0
    total = 0

    for j in range(n):
        prefix += S[j]  # n*2
        total += prefix

    return total

def f5(n):

    A = [random.randint(10, 1000) for _ in range(n)]
    B = [random.randint(10, 1000) for _ in range(n)]

    count = 0  # 1

    for i in range(n):
        total = 0  # n
        for j in range(n):
            for k in range(1+j):
                total += A[k]  # n*(1+2+..+n) = n*n*(n+1)/2
            if B[i] == total:
                count += 1  # n*n
    return count

xs = [_ + 1 for _ in range(100)]  # n取1-100

y1 = [timeit.timeit(lambda: f1(_), number=1) for _ in xs]
y2 = [timeit.timeit(lambda: f2(_), number=1) for _ in xs]
y3 = [timeit.timeit(lambda: f3(_), number=1) for _ in xs]
y4 = [timeit.timeit(lambda: f4(_), number=1) for _ in xs]
y5 = [timeit.timeit(lambda: f5(_), number=1) for _ in xs]

y1 = [math.log(x, 2) for x in y1]
y2 = [math.log(x, 2) for x in y2]
y3 = [math.log(x, 2) for x in y3]
y4 = [math.log(x, 2) for x in y4]
y5 = [math.log(x, 2) for x in y5]


pt.figure(1)
pt.plot(xs, y1, label='y1')
pt.plot(xs, y2, label='y2')
pt.plot(xs, y3, label='y3')
pt.plot(xs, y4, label='y4')
pt.plot(xs, y5, label='y5')
pt.legend()
pt.show()