# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    假设O(n*log(n))可以完成对n个数字的排序, 证明在O(n*log(n))时间内能判断三集不相交问题

    把三个列表拼起来排序, 然后一次遍历看有没有连续三个相等的(三集问题了, 每个集合内部不重复)
"""

def f():
    # 当然, 最简单的是直接三集取交集, 这里暂不采用这种方法

    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 6, 7, 8, 9]
    l3 = [5, 7, 10, 11]

    l = l1+l2+l3
    l.sort()   # O(n*log(n))

    for i in range(len(l)-2):
        if l[i] == l[i+1] == l[i+2]:  # n*3
            return True

    return False

print(f())

