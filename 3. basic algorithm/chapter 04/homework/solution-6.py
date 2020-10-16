# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个递归 计算第n个调和数
    第一个: 1/1
    第二个: 1/1+1/2
    第三个: 1/1+1/2+1/3
"""
from helloutils.tracker import Track

@Track
def f1(n):
    if n == 1: return 1/1
    return 1/n+f1(n-1)

print(f1(3))

# 上面的线性递归最好理解, 但是不是尾递归
def f2(n):
    @Track
    def f(res, n):
        res = res + 1 / n
        if n == 1: return res
        return f(res, n - 1)
    return f(0, n)

print(f2(3))

# 除了f2的尾递归, 还可以正序加
def f3(n):
    @Track
    def f(res, k, n):
        res = res + 1 / k
        if k == n: return res
        return f(res, k+1, n)
    return f(0, 1, n)
print(f3(3))