# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    假设一个包含n个元素的栈S和一个初始为空的队列Q
    判断S中是否包含特定元素, 处理完之后S必须回到初始状态
    该算法只能使用S, Q和固定数量的变量

"""
"""
    分析
    1 2 3 4 5
    遍历出栈进到队列  5 4 3 2
    如果直接入栈会变成: 1 5 4 3 2
    
    来两次?
    12345->54321->54321
    
"""
from collections import deque

s = [1, 2, 3, 4, 5]
d = deque()

x = 2
r = False

while s:
    t = s.pop()
    if t == x: r = True

    d.append(t)

while d:
    s.append(d.popleft())

while s:
    d.append(s.pop())

while d:
    s.append(d.popleft())

print(s, d)

"""
    还有其它办法吗?
    
    12345
    好像没有, 最多加个计数器, 找到目标值就停止出栈
"""

c = 0

while s:
    t = s.pop()
    d.append(t)
    c += 1

    if t == x:
        r = True
        break

print(c, r)

for _ in range(c):
    s.append(d.popleft())

for _ in range(c):
    d.append(s.pop())

for _ in range(c):
    s.append(d.popleft())

print(s, d)