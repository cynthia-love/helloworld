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
    非递归形式, 思路1, 记住每一步的余数
    比如5 / 2 = 2 ... 1, 把这个1记住
    2 / 2 = 1 ... 0, 把这个0记住
    
    5: [1, 0], 5 = (1*2+0)*2+1
    4: [0, 0], 还原: (base**2*base**0)**2*base**0
    3: [1], 还原: base**2*base**1
"""
def f2(base, n):
    # 所有数的0次幂都是1, 有信息丢失
    # 建议这种特殊情况单独处理, 宁可代码多几行, 避免后续逻辑混乱
    if n == 0: return 1

    l = []
    while n > 1:
        l.append(n % 2)
        n = n // 2

    res = base

    for each in l[::-1]:
        res = res*res*(base**each)

    print(res)

f2(2, 5)

"""
    思路2, 递归和队列有着很类似的结构, 递归是深度优先, 所以同侧进出
    对应地, 对于广度优先的场景, 一侧进另一侧出
    
    [10] -> [5, 5] -> [5, 1, 2, 2]->[5, 1, 2, 1, 1]
    
    然后右边开始, base*base, 下一个2出来了, 直接从之前的解里取
"""
from collections import deque
def f3(base, n):
    if n == 0: return 1

    d = deque()
    d.append(n)

    while True:
        t = d.pop()
        if t == 1:
            d.append(1)
            break
        if t % 2 == 1: d.append(1)
        d.append(t // 2)
        d.append(t // 2)

    r = 1
    k = 0
    mem = {1: base}

    # 其实按照上面的逻辑, 右边完事左边的值mem里一定是有的
    # 可以先把mem[1]存了, 省去几行代码
    # while d:
    #     t = d.pop()
    #     k += t
    #     if t in mem:
    #         r = r*mem[t]
    #     else:
    #         r = r*base**t
    #     mem[k] = r

    while d:
        t = d.pop()
        k += t
        r = r*mem[t]
        mem[k] = r

    print(r)

f3(2, 10)