# -*- coding; utf-8 -*-
# Author: Cynthia

"""
    验证sorted方法为n*log(n)的
"""
from matplotlib import pyplot as pt
import math
import random
import timeit

def f(n):
    s = [random.random() for _ in range(n)]
    s.sort()

xs = [_+1 for _ in range(1000)]

ys = [timeit.timeit(stmt=lambda :f(_), number=1) for _ in xs]

ys2 = [_*math.log(_, 2)/50000000 for _ in xs]

pt.plot(xs, ys)
pt.plot(xs, ys2)
pt.show()


