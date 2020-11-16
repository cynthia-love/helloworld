# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    数组中恰有一个整数重复
    比如1, 2, 3, 4, 3
    设计算法找到这个整数
"""

l = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9]

"""
    思路1, 暴力枚举
    时间复杂度: 9+8+7+6+...+1 = O(n^2)
"""
def f1():
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                return l[i]
print(f1())

"""
    思路2, 哈希一次遍历
"""
def f2():
    h = set()
    for e in l:
        if e in h:
            return e
        else:
            h.add(e)
print(f2())

"""
    思路3, 先排序, O(n*log(n))
    再一次遍历
"""
def f3():
    l.sort()
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return l[i]
print(f3())