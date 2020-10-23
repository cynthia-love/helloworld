# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    一个序列含有n个元素, 不重复, 升序
    给定一个数k, 设计一个递归, 找到一对和为k的数(假设一定存在, 且找到一对就行)
"""

"""
    分析: 1, 2, 3, 4, 5, 6, k=8
    非递归, 双指针, O(n), 对应递归形式
"""

s = [1, 2, 3, 4, 5, 6]
k = 8

def f1(left, right):
    if s[left]+s[right] == k:
        return s[left], s[right]
    elif s[left]+s[right] < k:
        return f1(left+1, right)
    else:
        return f1(left, right-1)

print(f1(0, len(s)-1))


# 非有序也可以O(n)
def f2():
    s = [1, 2, 3, 4, 5, 6]
    k = 9
    ss = set(s)

    for each in ss:
        if k-each in ss:
            return each, k-each
print(f2())