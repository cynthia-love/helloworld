# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个递归, 重新排列一个整数值序列, 使所有偶数出现在所有奇数的前面

    比如: [1, 2, 3, 4, 5] 可以变成 [2, 4, 1, 3, 5]
    奇偶内部顺序不做要求
"""

"""
    思路1, 循环
    
    左边找到第一个奇数, 右边找到第一个偶数, 互换
"""


def f1():
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 22, 44]
    left, right = 0, len(s)-1

    while left < right:
        while s[left] % 2 == 0: left += 1
        while s[right] % 2 == 1: right -= 1

        if left < right:
            s[left], s[right] = s[right], s[left]

    print(s)
f1()

"""
    思路2, 递归
    [1, 2, 3, 4, 5]的递推关系怎么找?
    好像还是得用循环的思路, 只不过写成了递归形式...
"""

def f2():
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 22, 44]

    def rf(left, right):
        if left >= right: return

        if s[left] % 2 == 0:
            if s[right] % 2 == 0:
                rf(left+1, right)
            else:
                rf(left+1, right-1)
        else:
            if s[right] % 2 == 0:
                s[left], s[right] = s[right], s[left]
                rf(left+1, right-1)
            else:
                rf(left, right-1)
    rf(0, len(s)-1)
    print(s)
f2()

"""
    除了上述借助双指针思路的递归, 还有其它思路吗?
    [1, 2, 3, 4, 5] = [1, 2, 3, 4] 5
    而[1, 2, 3, 4] = 4 [1, 2, 3]
    而[1, 2, 3] = [1, 2], 3
    
    先不管空间复杂度
"""
def f3():
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 22, 44]

    def rf(var_s):
        if len(var_s) == 0: return []

        if var_s[-1] % 2 == 0:
            return [var_s[-1]]+rf(var_s[:-1])
        else:
            return rf(var_s[:-1])+[var_s[-1]]

    print(rf(s))

f3()


