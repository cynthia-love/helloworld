# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    序列S包含n-1个唯一的整数, 整数范围[0-n-1], 里面有一个不属于S
    设计一个算法找出此数, 时间复杂度O(n), 额外空间复杂度(不算S存储) O(1)

    O(n)说明只能单层遍历, O(1)说明只能额外声明几个变量
"""

# 方法1, 有点取巧了...
def f1():
    s = [1, 0, 7, 6, 2, 3, 5]

    for i in range(len(s)):
        try:
            s.remove(i)
        except ValueError:
            return i

print(f1())

# 方法2, 少了一个数, 应该加总值很好求, 当前加总值也很好求, 一减那个少的不就出来了
# 比如出门100块, 回来还剩90, 丢了的钱肯定是100-90
# 当然, 这里如果少的是两个, 就不能这么干了, 因为1+4 = 2+3
def f2():
    s = [1, 0, 7, 6, 2, 3, 5]  # 7个数, 整数范围[0-7]
    sum_s = len(s)*(len(s)+1)/2
    for each in s:
        sum_s -= each

    return int(sum_s)

print(f2())





