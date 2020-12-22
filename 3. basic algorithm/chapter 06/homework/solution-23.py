# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    三个非空栈RST
    将, 将S的元素以原始顺序加到T的原有元素后面
    比如: [1, 2, 3], [4, 5], [6, 7, 8, 9]
    变成 [1, 2, 3], [], [6, 7, 8, 9, 4, 5]

"""

r = [1, 2, 3]
s = [4, 5]
t = [6, 7, 8, 9]

"""
    直接把s的全部压到r里, 再到t里
"""
def f1():

    c = 0
    while s:
        r.append(s.pop())
        c += 1

    while c > 0:
        t.append(r.pop())
        c -= 1
f1()
print(r, s, t)
