# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    3^5 = (3^2)^2*3
    实现这种求power方式的非递归形式
"""
from helloutils.tracker import Track

@Track
def f1(base, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return f1(base, n//2) ** 2

    else:
        return f1(base, n//2) ** 2 * base

# print(f1(2, 5))

"""
    非递归形式
    5-2-1-0, 显然是不可逆的...
    5 = 2*2+1
    2 = 2*1
    1 = 2*0+1
    
    一个思路是把每一步是否余1给记下来
    
"""

def f2(base, n):

    left, t = [], n
    while t >= 1:
        left.append(1 if t % 2 == 1 else 0)
        t = t // 2

    res = 1

    for each in left[::-1]:
        res = res*res*base**each

    print(res)

f2(2, 4)

"""
    第二个思路, 比如2^5
    [5]
    [2, 2, 1]
    [1, 1, 2, 1]
    [0, 0, 1, 1, 2, 1]
"""
from collections import deque
def f3(base, n):
    d = {0: 1, 1: base}
    q = deque()
    q.append(n)
    k = 0
    res = 1

    while q:
        t = q.popleft()
        if t in d:
            res *= d[t]
            k += t
            d[k] = res
        else:
            l = t % 2
            if l:
                q.appendleft(t//2)
                q.appendleft(t//2)
                q.appendleft(1)
            else:
                q.appendleft(t//2)
                q.appendleft(t//2)
    return res

print(f3(2, 5))