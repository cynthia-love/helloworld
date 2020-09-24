# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    描述一种有效算法, 在大小为n的序列中找到前十个最大元素

"""

def f():

    l = [1, 2, 3, 4, 5, 8, 10, 11, 20, 11, -1, -2, 300]

    # 思路1, 排序后直接取, O(n*log(n))

    # 思路2, 冒泡10次, 10*n, O(n)
    for i in range(10):
        for j in range(len(l)-1-i):
            if l[j] >= l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
            print(l)

    return l[-10:]

print(f())