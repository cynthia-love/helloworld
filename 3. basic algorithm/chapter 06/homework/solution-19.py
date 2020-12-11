# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改HTML标签匹配代码
    使得标签支持带属性
    <table border="3" cellpadding="5"> </table>
"""

"""
    对思路1的修改, 找到<>中的字符串之后用空格做split, 取第一个
    对思路2的修改, 正则模式串改成 '<(.*?)( .*?)?>'
    
    理解这种写法, 尤其后半部分作为一个整体加?
    
"""
import re
from collections import deque
from helloutils.tracker import Track

def is_matched1(s):
    stack = deque()
    pos = 0

    while True:
        l = s.find('<', pos)
        if l == -1: break  # 注意, 找不到返回-1, 这里不能用not判断

        r = s.find('>', l+1)
        if r == -1: break

        tag = s[l+1: r].split(" ")[0]

        # 外层的是获取标签逻辑, 这里是匹配逻辑
        if tag.startswith('/'):
            # 处理右标签
            if not stack: return False
            if stack[-1] != tag[1:]: return False
            stack.pop()
        else:
            # 左标签直接入栈
            stack.append(tag)

        # 匹配逻辑结束

        pos = r+1

    # 如果没有提前返回, 判断栈是否为空
    return len(stack) == 0


def is_matched2(s):
    tags = re.findall(r"<(.*?)( .*?)?>", s)
    tags = [e[0] for e in tags]
    print(tags)

    stack = deque()

    for e in tags:

        if not e.startswith('/'):
            stack.append(e)

        else:
            # 这里可以不提前返回
            # 不提前返回性能差, 但逻辑更容易转写成递归
            if stack and stack[-1] == e[1:]:
                stack.pop()

    return not stack

def is_matched3(s):

    tags = re.findall(r"<(.*?)( .*?)?>", s)
    tags = [e[0] for e in tags]
    print(tags)

    def rf(k):

        if k >= len(tags): return []
        next = rf(k + 1)

        # next最左和当前能匹配上, 返回next[1:]
        # 匹配不上, 拼一起返回
        if not tags[k].startswith('/') and next and next[0][1:] == tags[k]:
            return next[1:]
        else:
            return [tags[k]]+next

    return not rf(0)


print(is_matched1('<div border="3" cellpadding="5"><p>xxx</p></div>'))
print(is_matched2('<div border="3" cellpadding="5"><p>xxx</p></div>'))
print(is_matched3('<div border="3" cellpadding="5"><p>xxx</p></div>'))
