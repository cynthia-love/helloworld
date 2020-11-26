# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    栈的应用-成对括号匹配

    ([[]]){}, 都能匹配上返回True, 否则返回False
"""
from collections import deque

# 左括号入栈, 拿右括号去碰, 要求栈顶能匹配上, 碰不上直接返回False
# 遍历完之后, 看栈里还有没有没匹配上的左括号
# 一次遍历, 时间复杂度O(n)
def is_matched(s):

    sl = '{[('
    sr = '}])'

    stack = deque()

    for e in s:

        # 左括号直接压入
        if e in sl:
            stack.append(e)

        elif e in sr:
            # 栈为空, 遇到)]}, 则不匹配
            if len(stack) == 0:
                return False

            # 找栈顶元素在sl里的索引, 栈只压左括号, 所以这里不会报错
            if sl.index(stack[-1]) != sr.index(e):
                return False

            # 匹配上了, 栈顶左括号出栈
            stack.pop()

    # 全部匹配完, 看栈里还有没有左括号
    return len(stack) == 0

print(is_matched('[()]'))
print(is_matched(')('))
print(is_matched('[(5+x)-(y+z)]'))

