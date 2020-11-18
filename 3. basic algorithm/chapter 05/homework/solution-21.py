# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    评估以下几种字符串拼接方法的效率
"""
import sys
import timeit
def f1():
    s = 'hello world'
    r = ''
    for e in s:
        r += e
    return r

print(timeit.timeit(f1, number=1000000))  # 0.89

def f2():
    s = 'hello world'
    r = []
    for e in s:
        r.append(e)
    return ''.join(r)
print(timeit.timeit(f2, number=1000000))  # 1.20

def f3():
    s = 'hello world'
    return ''.join([e for e in s])

print(timeit.timeit(f3, number=1000000))  # 0.80

def f4():
    s = 'hello world'
    return ''.join(e for e in s)
print(timeit.timeit(f4, number=1000000))  # 1.11