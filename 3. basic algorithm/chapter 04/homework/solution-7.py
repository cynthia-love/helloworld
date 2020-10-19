# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个递归, 可以把一串数字转换成对应的整数
    比如'13531'转13531
"""

"""
    分析
    思路1, 不管递归, 直接int转
    思路2, 非递归, 从右往左遍历, 第一位*10^0, 第二位...
    思路3, 非递归, 从左往右遍历, 可以直接根据索引和字符串长度算出10的指数
    思路4, 递归
    f('13531') = f('1353')*10+1
    = (f('135')*10+3)*10+1
    即f(k) = 10*f(k-1)+s[k], f(0) = s[0]
    
    思路5, 另外一种递归
    f('13531') = 1*10^len(s)-1+f('3531')
"""
from helloutils.tracker import Track

def f1(s):
    return int(s)
print(f1('13531'))

def f2(s):
    res = 0
    base = 1

    for i in range(len(s)-1, -1, -1):
        res += int(s[i])*base
        base *= 10
    return res

print(f2('13531'))

# 除了倒叙, 还可以正序
def f3(s):
    res = 0
    for i in range(len(s)):
        res += int(s[i])*10**(len(s)-1-i)
    return res
print(f3('13531'))

@Track
def f4(s):
    if len(s) == 1: return int(s)
    else:
        return 10*f4(s[:-1])+int(s[-1])

print(f4('13531'))

# f4还有另外一种写法, 传索引而不是截断s
@Track
def f5(s, k):
    if k == 0: return int(s[k])
    else:
        return 10*f5(s, k-1)+int(s[k])
print(f5('13531', len('13531')-1))

# 反过来递归
@Track
def f6(s):
    if len(s) == 1: return int(s)
    return int(s[0])*10**(len(s)-1)+f6(s[1:])
print(f6('13531'))

