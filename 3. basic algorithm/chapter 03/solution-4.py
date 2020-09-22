# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    算法分析示例
"""

def f():
    l = [1, 2, 3, 4, 5]
    print(len(l))
    print(l[0])

"""
    len(list)是单独存储的, 无需遍历, 所以时间复杂度是O(1)
    list[index], 元素是连续存储的, 可以直接根据索引计算位置, 无需遍历, 所以时间复杂度也是O(1)
"""

