# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    做实验评估remove方法的效率
"""
import time

def f1(n):

    l = [i for i in range(n)]

    t1 = time.time()

    l.remove(0)  # 删开头

    t2 = time.time()

    print(t2-t1)

def f2(n):
    l = [i for i in range(n)]

    t1 = time.time()

    l.remove(n//2)  # 删中间

    t2 = time.time()

    print(t2-t1)

def f3(n):

    l = [i for i in range(n)]

    t1 = time.time()

    l.remove(n-1)

    t2 = time.time()

    print(t2-t1)

for e in [100, 1000, 10000, 100000, 1000000]:
    f1(e)
    f2(e)
    f3(e)
    print('===')

# 貌似第一个最快, 第二个次之, 第三个最慢
# 也就是说, 同样次数, 比较语句效率低于赋值语句