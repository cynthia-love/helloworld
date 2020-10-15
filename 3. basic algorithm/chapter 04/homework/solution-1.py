# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    对于一个含有n个元素的序列S, 设计一个递归查找最大值, 并评估时间复杂度和空间复杂度
"""

s = [1, 2, 8, 100, -8, 2000, 3]

# 非递归
res = s[0]
for i in range(1, len(s)):
    if s[i] > res:
        res = s[i]
print(res)

# 递归
"""
    时间复杂度: f(n-1)到f(0), 即O(n)
    空间复杂度: 递归深度O(n), 单次递归空间复杂度O(1), 总的空间复杂度O(n)
"""
def f(k):
    if k == 0: return s[0]
    return max(s[k], f(k-1))

print(f(len(s)-1))

# 尾递归
"""
    时间复杂度: f(n-1)到f(-1), 即O(n)
    空间复杂度: 编译器如果没对尾递归优化, 则O(n), 如果优化了, O(1)
"""
def f(res, k):
    if k < 0: return res
    return f(max(res, s[k]), k-1)
print(f(s[0], len(s)-1))
