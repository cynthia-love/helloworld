
# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    多重递归
"""

# 排列问题, 比如从10个字母里选3个排列
# a-b-c-d-e-f-g-h-i-j
"""
    时间复杂度评估, 取极限情况, n和s长度相等
    n*(n-1)*(n-2)*..*1
    
    n为k时, res长度为n-k, s循环m-(n-k), m取n相等, s循环k次
    t(k) = k*t(k-1)
    注意事件递推公式是直接算, 而不是累加和
    t(n) = n*(n-1)*...*1, 所以为O(n!)
    
    空间复杂度看递归深度, O(n)
"""
def f(n, res, s):
    if n == 0:
        print(res)
        return

    for each in s:
        if each not in res:
            f(n-1, res+each, s)

f(3, "", "abcd")

# 如果不用字符串, 用set呢
"""
    时间复杂度和空间复杂度和上面的没区别
"""
def f2(n, res:list, s: set):
    if n == 0:
        print(res)
        return

    for each in s.copy():
        # 注意这里要用copy, 不然循环体里会动s, 导致发生不可预知的结果
        s.remove(each)
        res.append(each)
        f2(n-1, res, s)

        res.remove(each)
        s.add(each)

f2(3, list(), {'a', 'b', 'c'})
