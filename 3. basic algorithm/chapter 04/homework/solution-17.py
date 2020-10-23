# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个递归, 判断一个字符串是否是它的一个回文字符串
    比如: abcba就是
"""

"""
    算法1, 循环
"""
def f1(s:str):
    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(f1("abcbad"))

"""
    算法2, 递归
    abcba对称当且仅当s[0] == s[-1], 且bcb是
"""
from helloutils.tracker import Track

def f2(s: str):
    @Track
    def rf(left, right):
        if left >= right: return True

        if s[left] == s[right]:
            return rf(left+1, right-1)
        else:
            return False

    return rf(0, len(s)-1)

f2("abcba")