# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    进一步分析之前的三种prefix函数, 用实验法画三个对比图, 横纵坐标双对数
"""
import math
import timeit
import random
from matplotlib import pyplot as pt

def main():

    # 思路1
    def f1(n):
        l = [random.random() for _ in range(n)]
        res = [0]*len(l)  # n
        for i in range(len(res)):
            total = 0  # n
            for j in range(i+1):
                total += l[j]  # 1+2+3+..+n
            res[i] = total/(i+1)  # n
        return res  # 1
    """
        分析: n+n+(1+2+..+n)+n + 1
        = 3n+1+n*(n+1)/2 = O(n^2)
    """

    # 思路2
    def f2(n):
        l = [random.random() for _ in range(n)]
        res = [0]*len(l)  # n
        for i in range(len(res)):
            res[i] = sum(l[:i+1])/(i+1)  # sum本质上也是一个函数
        return res  # 1
    """
        分析: n+(1+2+..+n)+1 = O(n^2), 只是少了一个n, 时间复杂度量级还是n方
    """

    # 思路3
    def f3(n):
        l = [random.random() for _ in range(n)]
        res = [0]*len(l)  # n
        total = 0  # 1
        for i in range(len(res)):
            total += l[i]  # n
            res[i] = total/(i+1)  # n
    """
        分析: n+1+n+n = O(n)
    """

    xs = [_+1 for _ in range(100)]  # n取1-100

    y1 = [timeit.timeit(lambda : f1(x), number=1) for x in xs]
    y2 = [timeit.timeit(lambda : f2(x), number=1) for x in xs]
    y3 = [timeit.timeit(lambda : f3(x), number=1) for x in xs]

    pt.figure(1)
    pt.plot(xs, y1, label='y1')
    pt.plot(xs, y2, label='y2')
    pt.plot(xs, y3, label='y3')
    pt.legend()
    pt.show()

    xss = [math.log(x, 2) for x in xs]
    y11 = [math.log(x, 2) for x in y1]
    y22 = [math.log(x, 2) for x in y2]
    y33 = [math.log(x, 2) for x in y3]

    pt.figure(2)
    pt.plot(xss, y11, label='y11')
    pt.plot(xss, y22, label='y22')
    pt.plot(xss, y33, label='y33')

    pt.legend()
    pt.show()

if __name__ == '__main__':
    main()