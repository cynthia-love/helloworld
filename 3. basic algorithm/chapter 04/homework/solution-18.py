# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个递归, 确定字符串中是否元音比辅音多
"""

"""
    ???直接统计不就行了...
"""
s = 'ababbaf'

c1, c2 = 0, 0

for each in s:
    if each in 'aeiou': c1 += 1
    else: c2 += 1

print(c1 > c2)

"""
    递归也不是不行, 循环一定可以转成递归的
"""
def f(c1, c2, pos):
    if pos > len(s)-1:
        return c1 > c2

    if s[pos] in 'aeiou':
        return f(c1+1, c2, pos+1)
    else:
        return f(c1, c2+1, pos+1)
print(f(0, 0, 0))

"""
    如果不依据循环思路, 就想设计一个性能一般但好理解的递归呢
    abc 的元音,辅音个数 = bc的元音个数+1, bc的辅音个数
"""
def f2(pos):
    if pos > len(s)-1:
        return 0, 0

    next = f2(pos+1)

    if s[pos] in 'aeiou': return next[0]+1, next[1]
    else: return next[0], next[1]+1

r = f2(0)
print(r[0] > r[1])

"""
    还有没有其他递归思路了?
    abcde 元音个数大于辅音个数, c(元音) - c(辅音) >= 1
    a是元音, 所以需要bcde的 c(元音) - c(辅音) >= 0
    b是辅音, 所以需要cde的 c(元音) - c(辅音) >= 1
    c是辅音, 需要de c1-c2 >= 2
    d是辅音, 需要e c1-c2 >= 3
    e是元音, 需要""的c1-c2 >= 2
    而""的c1和c2都是0, 那么右边这个值小于等于0才能返回True

"""
from helloutils.tracker import Track
@Track
def f3(s, k):
    if not s:
        return True if k <= 0 else False

    if s[0] in 'aeiou':
        return f3(s[1:], k-1)
    else:
        return f3(s[1:], k+1)

f3(s, 1)