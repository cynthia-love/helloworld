# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    编写一个矩阵类, 支持加和和相乘

    2 1
    1 2    x  2     ->     4,2 x 2,1->4,1
    3 3       2
    1 1
"""
import copy

class Matrix:

    def __init__(self, d1=1, d2=1, ll = None):
        """
        可以给定一个二维数组, 也可以给定一维二维维数, 初始化为0
        :param ll:
        :param d1:
        :param d2:
        """
        if ll:
            self._matrix = copy.deepcopy(ll)
            self._d1 = len(self._matrix)
            self._d2 = len(self._matrix[0])

        else:
            self._d1 = d1
            self._d2 = d2
            self._matrix = [[0 for _ in range(d2)] for _ in range(d1)]

    # property的简洁写法
    @property
    def shape(self):
        return self._d1, self._d2
    # shape = property(get_shape)

    def __len__(self):
        return self._d1

    # 这里注意, 要实现self[i][j]这么写就行了, 因为self[i]返回的是个一维list
    # 另外, self[i][j] = xxx 也不用再写__setitem__了, 想想为什么
    def __getitem__(self, k):
        return self._matrix[k]

    def __str__(self):
        return '\n'.join(', '.join(str(x) for x in e) for e in self._matrix)

    def __add__(self, other):
        """
        other不要求是Matrix实例, 只要和self维度相同即可
        :param other:
        :return:
        """
        try:
            d1, d2 = len(other), len(other[0])
        except ValueError:
            print("illegal matrix")
        else:
            if d1 != self._d1 or d2 != self._d2:
                print("matrix dimensions not same")
            else:
                ll = [[self[i][j]+other[i][j] for j in range(self._d2)] for i in range(self._d1)]
                return Matrix(ll=ll)  # 这里返回Matrix实例, 便于用str等方法

    def __mul__(self, other):
        """
        要求左矩阵的第二维长度和右矩阵的第一维长度相同
        :param other:
        :return:
        """
        d1, d2 = len(other), len(other[0])

        if self._d2 != d1:
            raise ValueError

        # 这里注意, r不用能*法初始化, 因为二维, 里面的对象用*法初始化每一行就是同一个了
        r = [[0 for _ in range(d2)] for _ in range(self._d1)]
        # r[i][j] = 第一个矩阵的第i行和第二个矩阵的第j列每个元素的积数和
        for i in range(self._d1):
            for j in range(d2):

                r[i][j] = sum(self[i][k]*other[k][j] for k in range(d1))

        return Matrix(ll=r)


o1 = Matrix(ll=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
o2 = Matrix(ll=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
o3 = o1 + o2
print(o3)

o4 = Matrix(ll=[[1, 1],[1, 1],[1, 1]])
o5 = o2*o4
print(o5)