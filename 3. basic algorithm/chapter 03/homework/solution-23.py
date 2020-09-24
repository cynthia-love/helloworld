# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对下列代码进行大O描述
"""

def example1(S):
    n = len(S)  # 1
    total = 0  # 1
    for j in range(n):
        total += S[j]  # n*1
    return total  # 1

"""
    f(n) = n+3 = O(n)
"""