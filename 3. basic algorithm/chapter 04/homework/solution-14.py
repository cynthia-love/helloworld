# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    汉诺塔
    n表示盘子数量, 初始n个盘子从下往上由大到小摆在A柱上, 要移动到C柱上

    拆解问题:
    n个盘子由A->C: n-1个盘子由A到B, n号盘子由A到C, n-1个盘子由B到C
"""
from helloutils.tracker import Track
def f(n):
    @Track
    def rf(k, f, b, t):
        """
        :param f: 从哪个柱子
        :param t: 移到哪个柱子
        :param b: 借助哪个柱子
        :return:
        """
        if k == 1:
            print('{}->{}'.format(f, t))
        else:
            rf(k-1, f, t, b)
            print('{}->{}'.format(f, t))
            rf(k-1, b, f, t)

    rf(n, 'A', 'B', 'C')

f(3)