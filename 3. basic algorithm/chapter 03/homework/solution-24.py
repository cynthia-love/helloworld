# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    大O描述
"""

def example2(S):
    n = len(S)  # 1
    total = 0  # 1

    for j in range(0, n, 2):
        total += S[j]  # n/2*1

    return total  # 1

# O(n)