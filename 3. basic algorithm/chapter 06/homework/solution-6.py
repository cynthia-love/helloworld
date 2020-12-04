# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个分组符号匹配的精确完整定义, 可递归

    只考虑()[]{}, 不考虑<>, '', ""什么的

    非递归思路1, 左入栈, 右和栈顶碰
    非递归思路2, 计数

    递归思路:
    一种取巧的办法是把栈或计数器作为参数传递, 递归仅起到循环的作用...

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

# 补充一种非递归思路, 计数
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
    先尝试一下第一种取巧的递归, 传栈
    递归只是起到循环作用
    
    f(stack, k) = 
        如果k > len(s)-1, len(stack) == 0
        如果s[k] 为左括号, f(stack.append(s[k]), k+1)
        如果s[k] 为右括号:
                如果len(stack) == 0, False
                如果stack栈顶不配对, False
                否则f(stack.pop(), k+1)
    
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
    下面尝试第二种取巧的递归, 传计数器
    
    f(count, k) = 
        如果 k > len(s)-1, sum(count.values()) == 0
        如果 s[k] 为左括号, f(count[s[0]]+=1, k+1)
        如果 s[k] 为右括号, count里对应左括号计数-1
                -1后小于0, False
                不小于0, f(count, k+1)
"""

def f2(count, s):
    if not s:
        return sum(count.values()) == 0

    if s[0] in r2l:
        count[r2l[s[0]]] -= 1
        if count[r2l[s[0]]] < 0:
            return False
    else:
        count[s[0]] += 1

    return f2(count, s[1:])


print(f2(defaultdict(int), '(([]){})()'))
