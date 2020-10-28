# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    用非递归方式实现draw_interval

    -
    --
    -
    ---
    -
    --
    -
"""

# 先回忆一下递归方式
from helloutils.tracker import Track
@Track
def f1(length):
    if length < 0: return

    f1(length-1)
    print('-'*length)
    f1(length-1)

# f1(3)

# 非递归方式
# 二路递归转循环, 直接转肯定是不行的
# 要想办法去模拟递归调用栈
# 这里用数字表示递归函数, ---表示函数输出
# 比如f(3), 相当于 2, '---', 2
"""
    3
    2, '---', 2
    1, '--', 1, '---', 2
    '-', '--', 1, '---', 2
    输出-
    输出--
    1, '---', 2
    '-', '---', 2
    输出-
    输出---
    2
    121
    ...
    
"""

from collections import deque
def f2(length):

    d = deque()
    d.appendleft(length)
    while d:
        t = d.popleft()
        # 为数字, 代表是子递归函数
        if isinstance(t, int):
            # 为1, 代表递归边界
            if t == 1:
                d.appendleft('-')
            else:
                d.appendleft(t-1)
                d.appendleft('-'*t)
                d.appendleft(t-1)
        # 不为数字, 表示该输出当前递归函数的内容了
        else:
            print(t)
f2(4)


