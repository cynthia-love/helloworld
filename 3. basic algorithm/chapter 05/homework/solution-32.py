# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    编写函数, 可以加总两个三维数值型数据集

    [
        [
            [ 1, 2, 3],
            [4, 5, 6]
        ]
    ]

"""

n1, n2, n3 = 2, 3, 4

l1 = [[[3 for _ in range(n3)] for _ in range(n2)] for _ in range(n1)]
l2 = [[[1 for _ in range(n3)] for _ in range(n2)] for _ in range(n1)]

def f(l1, l2):

    if len(l1) != len(l2) or len(l1[0]) != len(l2[0]) or len(l1[0][0]) != len(l2[0][0]):
        raise ValueError

    d1, d2, d3 = len(l1), len(l1[0]), len(l1[0][0])

    l3 = [[[l1[i][j][k]+l2[i][j][k] for k in range(d3)] for j in range(d2)] for i in range(d1)]

    print(l3)

f(l1, l2)