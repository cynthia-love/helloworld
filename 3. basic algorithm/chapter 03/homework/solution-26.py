# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    大O分析
"""

def example4(S):
    n = len(S)

    prefix = 0
    total = 0

    for j in range(n):
        prefix += S[j]  # n*2
        total += prefix

    return total

# O(n)