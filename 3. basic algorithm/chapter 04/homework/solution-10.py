# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    只使用加法和整数除法, 设计一个递归, 计算log2(n)的整数部分
    比如log2(8) = 3, log2(9) = 3
    (/为浮点数除法, //为整数除法)
"""

"""
    分析: 
    log2(n)的整数部分即看n除以2能除以几次直到得到的商小于1
    
    f(n) = 
            0, if n < 2
            1+f(n//2), if n >= 2
"""
from helloutils.tracker import Track

@Track
def f(n):
    if n < 2: return 0
    return 1+f(n//2)

# f(10)

# 改成尾递归
@Track
def rf(r, n):
    if n < 2: return r
    return rf(r+1, n//2)

def f(n):
    return rf(0, n)

f(10)