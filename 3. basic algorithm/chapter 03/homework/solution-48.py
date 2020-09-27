# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    斐波那契
    证明f(n)是O(n)的, 即存在k, 当n>=k时, f(n) <= c*n

    注意, 证明F(n) = F(n-1)+F(n-2) < 2^n, 即大小的范围
    和证明其时间复杂度是两码事, 时间复杂度是依赖于算法的


"""

def f(index):
    if index == 1:
        return 0  # 1
    if index == 2:
        return 1  # 1

    x1, x2 = 0, 1
    for i in range(3, index+1):
        x1, x2 = x2, x1+x2  # 2*n

    return x2

# 1+1+2*n = O(n)
print(f(1), f(2), f(3), f(4), f(5))

def f2(index):
    x, next = 0, 1
    for i in range(2, index+1):
        x, next = next, x+next

    return x

print(f(1), f(2), f(3), f(4), f(5))