# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个函数示例, 其在标准坐标轴和双对数坐标轴中图形一样

    n -> f(n)

    log(n) -> log(f(n))

    x = log(n), 则n = 2^x

    y = log(f(n)) = log(f(2^x))

    log(f(2^x)) 与 f(n) 图形一样, 另f(n) = 2^n

    则log(f(2^x)) = log(2^(2^x)) = 2^x

    所以f(n) = 2^n满足要求
"""