# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    大O分析
"""

def example3(S):
    n = len(S)  # 1

    total = 0  # 1

    for j in range(n):
        for k in range(1+j):
            total += S[k]  # 1, 2, 3, n

    return total  # 1

"""
    O(n^2)
"""