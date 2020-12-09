# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    一个双端队列1 2 3 4 5 6 7 8
    利用一个空队列, 把双端队列中的值变成1 2 3 5 4 6 7 8

    不可以使用其他变量
"""

from collections import deque

dq = deque([1, 2, 3, 4, 5, 6, 7, 8])

q = deque()  # 只允许使用popleft和append

dq.append(dq.popleft())
dq.append(dq.popleft())
dq.append(dq.popleft())
print(dq, q)

q.append(dq.popleft())

dq.append(dq.popleft())
dq.append(q.popleft())
print(dq, q)

dq.append(dq.popleft())
dq.append(dq.popleft())
dq.append(dq.popleft())
print(dq)


