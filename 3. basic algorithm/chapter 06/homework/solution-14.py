# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    一个双端队列1 2 3 4 5 6 7 8
    利用一个空栈, 把双端队列中的值变成1 2 3 5 4 6 7 8

    不可以使用其他变量

    ???和solution-13没区别吧, 队列/栈只用存一个4
"""

from collections import deque

dq = deque([1, 2, 3, 4, 5, 6, 7, 8])

s = list()

dq.append(dq.popleft())
dq.append(dq.popleft())
dq.append(dq.popleft())

s.append(dq.popleft())

dq.append(dq.popleft())

dq.append(s.pop())

dq.append(dq.popleft())
dq.append(dq.popleft())
dq.append(dq.popleft())

print(dq)