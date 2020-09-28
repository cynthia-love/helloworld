# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    二分查找
"""

def f():
    s = [1, 2, 3, 4, 5, 8, 10, 11, 20, 80, 100, 110, 120]
    l, r = 0, len(s)-1
    while l <= r:
        m = (l+r) // 2
        if s[m] == 20:
            return m
        elif s[m] > 20:
            r = m-1
        else:
            l = m+1
    return -1

print(f())

def f():
    s = [1, 2, 3, 4, 5, 8, 10, 11, 20, 80, 100, 110, 120]

    def rf(l, r):
        if l > r: return -1
        m = (l+r)//2
        if s[m] == 20:
            return m
        elif s[m] > 20:
            return rf(l, m-1)
        else:
            return rf(m+1, r)

    return rf(0, len(s)-1)
print(f())
