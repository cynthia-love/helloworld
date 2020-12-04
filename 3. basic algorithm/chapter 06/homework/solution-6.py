# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个分组符号匹配的精确完整定义, 可递归

    只考虑()[]{}, 不考虑<>, '', ""什么的

    非递归思路, 左入栈, 右和栈顶碰

    递归思路:
    一种取巧的办法是把栈作为参数传递, 递归仅起到循环的作用...

    下面思考如何彻底递归-基本思路比较清晰, 回溯

    (([]){})()

    遇到左括号往下递归, 右括号往上回溯, 就是细节怎么实现想不透

"""
from collections import deque, defaultdict
from helloutils.tracker import Track
# 先回顾非递归思路
def f1(s):
    d = deque()
    r2l = {')': '(', ']': '[', '}': '{'}
    for e in s:
        if e in r2l.values():
            d.append(e)

        else:

            if len(d) == 0:
                return False
            if d[-1] != r2l[e]:
                return False
            d.pop()
    else:
        return len(d) == 0

print(f1('(([]){})()'))

# 补充一种非递归思路, 数数
def f1(s):
    r2l = {')': '(', ']': '[', '}': '{'}
    d = defaultdict(int)

    for e in s:
        # 左括号, 计数加1
        if e in r2l.values():
            d[e] += 1
        # 右括号, 计数减1, 负值直接返回False
        else:
            d[r2l[e]] -= 1
            if d[r2l[e]] < 0:
                return False
    return sum(d.values()) == 0

print(f1('(([]){})()'))


"""
    先尝试一下一种取巧的递归, 传参, 实际上就是栈
    递归只是起到循环作用
    
"""

r2l = {')': '(', ']': '[', '}': '{'}
def f2(stack, s):
    if not s: return len(stack) == 0

    if s[0] in r2l.values():
        stack.append(s[0])
        return f2(stack, s[1:])
    else:
        if len(stack) == 0:
            return False
        if r2l[s[0]] != stack[-1]:
            return False

        stack.pop()

        return f2(stack, s[1:])

print(f2([], '(([]){})()'))

"""
    下面尝试真正的递归
    
    
"""
@Track
def f3(s):
    if len(s) == 0:
        return True

    if len(s) == 1:
        return s if s in r2l else False

    if s[0] in r2l:
        return s
    else:
        r = f3(s[1:])

        pass


f3('[]')