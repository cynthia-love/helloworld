# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    给出一个正函数f(n)的例子, 既不是O(n), 也不是Ω(n)

    连续函数是不可能的满足要求的
    f(n) = log(n), n为奇数
    f(n) = n^2, n为偶数

    log(n) <= n <= n^2

    所以既不是O(n)也不是Ω(n)

"""