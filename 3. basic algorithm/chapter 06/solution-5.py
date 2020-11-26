# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    标签匹配
    <div><p>xxx</p></div>

    基本思路, 提取: div, p, /p, /div
    提取到这一级而不带<>是为了好配对

    注意一对<>才构成一个标签, <单个的不算
"""
import re
from collections import deque

# 第一种思路, 用find找<, 再在接下来的子串中找>
def is_matched(s:str):

    stack = deque()

    # 找到第一个<xxx>或者</xxx>

    l = s.find('<')

    while l != -1:

        r = s.find('>', l+1)

        if r != -1:

            tag = s[l+1:r]

            # 接下来的匹配过程就和括号一样了
            # 上面的步骤实际上是在找括号符号

            if tag[0] != '/':

                stack.append(tag)

            else:

                if len(stack) == 0:
                    return False

                if stack.pop() != tag[1:]:
                    return False

            l = s.find('<', r+1)

    return len(stack) == 0

print(is_matched('<div><p>xxx</p></div>'))

# 思路2, 把所有<>标签提取出来, 再去做匹配, 这么更简单清晰

def is_matched(s):

    tags = re.findall(r'<(.*?)>', s)  # ['div', 'p', '/p', '/div']

    stack = deque()

    for e in tags:

        if not e.startswith('/'):
            stack.append(e)
        else:
            if len(stack) == 0:
                return False

            # pop出来, 不配对, 返回False, 配对, 继续处理下一个标签
            if e[1:] != stack.pop():
                return False

    return len(stack) == 0

print(is_matched('<div><p>xxx</p></div>'))
