# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个递归求解元素唯一性, 不能用排序, 最坏时间复杂度O(n^2)
"""

"""
    分析: [1, 2, 3, 8, -1, 200, 8]
    循环思路, 用每一个元素往后遍历, 本质上是C(n, 2)
    递归思路1:
        [1, 2, 3, 8, -1, 200, 8] 唯一 当且仅当[2, 3, 8, -1, 200, 8]唯一且1不在右侧序列里
        这俩条件先后顺序的不同可以有两种递归写法
        
    递归思路2:
        [1, 2, 3, 8, -1, 200, 8] 唯一 当且仅当[1, 2, 3, 8, -1, 200]唯一且8不在左侧序列里
"""

s = [1, 2, 3, 8, -1, 200, 8]

def f1():

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]: return False
    return True
print(f1())

from helloutils.tracker import Track
@Track
def f1(k):
    if k >= len(s)-1: return True

    for i in range(k+1, len(s)):
        if s[k] == s[i]: return False
    return f1(k+1)
f1(0)
print("======")
@Track
def f11(k):
    if k >= len(s)-1: return True

    next = f11(k+1)
    if not next: return next

    for i in range(k+1, len(s)):
        if s[k] == s[i]: return False

    return True

f11(0)
print("======")

@Track
def f2(k):
    if k <= 0: return True
    for i in range(0, k):
        if s[k] == s[i]: return False

    return f2(k-1)
f2(len(s)-1)
print("======")

@Track
def f22(k):
    if k <= 0: return True

    pre = f22(k-1)
    if not pre: return pre

    for i in range(0, k):
        if s[k] == s[i]: return False
    return True

f22(len(s)-1)