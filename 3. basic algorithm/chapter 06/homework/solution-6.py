# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个分组符号匹配的精确完整定义, 可递归

    只考虑()[]{}, 不考虑<>, '', ""什么的

    非递归思路1, 左入栈, 右和栈顶碰
    非递归思路2, 计数

    递归思路:
    一种取巧的办法是把栈或计数器作为参数传递, 递归仅起到循环的作用...

    彻底的递归思路的话, 嗯, 把非递归栈方法里的提前return逻辑去掉, 都最后判断
    你就能想出来递归思路了, 见下面的f(4)

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

"""
    灵机一动, 突然有递归思路了
    (([]){})()
    观察之前的栈方法, 发现最终目的是得到一个栈, 包括中间的提前return其实都是可以不提前的
    (([]){})(), 最终期望返回是""
    ((), 最终期望返回是"("
    (((, 最终期望返回是"((("
    ))), 最终期望返回是")))"
    即把所有匹配项都去掉, 看还能剩下什么
    
    对于f(s)来说:
    1. 情况1, s为空, return ""
    2. 情况2, s不为空, 求f(s[1:]), 设为res
            (1)s[0] 为左括号且res不为空且res[0]能匹配上, return res[1:]
            (2)否则, 返回s[0]+res
    
    ??? 有这么简单吗, 三四行代码想了一天, 再捋一捋
    
    定义f(s)返回字符串s由内往外去掉所有成对括号剩下的字符, 内部去不掉就不去了
    (())->""
    ((()->((
    )))->)))
    ([)->([)
    
    那么f('(([]){})()') =
                        先令 f(s[1:]) = res
                        
                        根据定义, res是去掉所有成对括号后剩下的字符
                        
                        如果res[0]能喝s[0]匹配上, return res[1:]
                        
                        否则return s[0]+res

    好像没错, 看来关键的是定义递推函数
"""

def f4(s):
    if not s: return ""

    res = f4(s[1:])


    if res and r2l.get(res[0]) == s[0]:

        # 理解这里为什么能直接return res[1:]
        # 因为res[1:] == f4(s[1:])
        return res[1:]

    else:

        # 下面这个呢, 为什么能这么写
        # x-abcde, abcde消不掉, x-a消不掉, x和bcde哪怕匹配了, 还是消不干净, 所以这么写是可以的

        return s[0]+res


print(f4('(([]){})()') == "")
print(f4('(([]]))'))

