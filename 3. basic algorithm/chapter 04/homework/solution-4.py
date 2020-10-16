# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    绘制线性递归逆置序列元素的递归跟踪
"""
from helloutils.tracker import Track

@Track
def reverse(s, left, right):
    if left >= right: return
    s[left], s[right] = s[right], s[left]
    reverse(s, left+1, right-1)

s = [4, 3, 6, 2, 6]
reverse(s, 0, len(s)-1)
