# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    算法运行时间为f(n) = log(n), 单位微秒
    那么1秒能跑完, n最大多少?

    log(n) <= 1000000
    n <= 2^1000000

    f(n) = n呢? 1000000

    f(n) = n*log(n)呢, n*log(n) <= 1000000

    f(n) = n*n, n <= 1000

    f(n) = 2^n <= 1000000, n <= log(1000000)
"""