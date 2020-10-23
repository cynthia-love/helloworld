# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    只使用加法和减法, 设计递归, 计算m*n
"""

"""
    分析:
    m*n = m+m*(n-1)
    即f(n) = m+f(n-1)
    
    时间复杂度: O(n)
"""

from helloutils.tracker import Track

def f1(m, n):
    @Track
    def rf(k):
        if k == 0: return 0
        return m+rf(k-1)

    return rf(n)

f1(2, 8)

# 改成尾递归
def f2(m, n):
    @Track
    def rf(r, k):
        if k == 0: return r
        return rf(r+m, k-1)
    return rf(0, n)

f2(2, 8)

