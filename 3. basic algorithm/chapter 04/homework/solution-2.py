# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    绘制普通power函数的power(2,5)追踪
"""

"""
    思路: 利用装饰器
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
    if n == 0: return 1
    return x*power(x, n-1)

power(2, 5)