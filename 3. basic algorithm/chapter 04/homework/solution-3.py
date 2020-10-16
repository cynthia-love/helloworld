# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    绘制重复平方法power函数的power(2, 18)追踪
"""

class Track:

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print("->{}({})".format(self._func.__name__,
                                ",".join([str(e) for e in list(args)+list(kwargs.values())])))
        res = self._func(*args, **kwargs)
        print("<-{}({})".format(self._func.__name__,
                                ",".join([str(e) for e in list(args)+list(kwargs.values())])))
        return res

@Track
def power(x, n):
    if n == 0:
        return 1

    r = power(x, n // 2)

    if n % 2 == 0:
        return r*r
    else:
        return x*r*r

power(2, 18)