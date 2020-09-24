# -*- coding: utf-8 -*-
# Author: Cynthia


"""
    大O分析
"""

def example5(A, B):

    n = len(A)  # 1
    count = 0  # 1

    for i in range(n):
        total = 0  # n
        for j in range(n):
            for k in range(1+j):
                total += A[k]  # n*(1+2+..+n) = n*n*(n+1)/2
            if B[i] == total:
                count += 1  # n*n
    return count


# O(n^3)
