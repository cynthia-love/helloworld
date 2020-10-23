# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给定一个未排序的整数序列和整数k, 设计一个递归算法
    对序列重排序, 使得所有小于等于k的元素在所有大于等于k的元素之前

    比如[1, 2, 3, 4, -1, -2], k选定3
    则结果之一为: [1, 2, 3, -1, -2, 4]

"""
from helloutils.tracker import Track

"""
    思路1, 非递归, 感觉和solution-19差不多, 双指针
"""

def f1():
    s = [1, 2, 3, 4, -1, -2]
    k = 2

    left, right = 0, len(s)-1

    while left < right:
        while s[left] <= k: left += 1
        while s[right] > k: right -= 1

        if left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    print(s)

f1()

"""
    思路2, 双指针思路转成的递归
    分析时间复杂度: 实际上是线性递归
    rf(l, r) 下一步是四个判断对应四种子递归, 最差情况下是1个1个变
    即O(n)
"""
def f2():
    s = [1, 2, 3, 4, -1, -2]
    k = 2

    @Track
    def rf(l, r):
        if l >= r: return

        if s[l] <= k:
            if s[r] > k:
                rf(l+1, r-1)
            else:
                rf(l+1, r)
        else:
            if s[r] > k:
                rf(l, r-1)
            else:
                s[l], s[r] = s[r], s[l]
                rf(l+1, r-1)
    rf(0, len(s)-1)
    print(s)

f2()

"""
    思路3, k == 2
    [1, 2, 3, 4, -1, -2]

    [1, 2, 3, 4, -1, -2] = -2+[1, 2, 3, 4, -1]
"""
def f3():
    s = [1, 2, 3, 4, -1, -2]
    k = 3

    def rf(vars):
        if not vars: return []
        if vars[-1] <= k:
            return [vars[-1]]+rf(vars[:-1])
        else:
            return rf(vars[:-1])+[vars[-1]]

    print(rf(s))
f3()

"""
    还有思路吗? k == 2
    [1, 2, 3, 4, -1, -2]
    
    1 小于等于2, 处理[2, 3, 4, -1, -2]
    2 小于等于2, 处理[3, 4, -1, -2]
    3 大于, 应该和-1替换, 有两种情况:
    (1) -1位置的小于等于2, [-2, 4, -1, 3], 换完左右都移动
    (2) -1位置的也大于2, 那左边不动右边动
    
    其实这里和上面的双指针是同一种思路...
"""