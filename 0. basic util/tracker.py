# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    函数调用跟踪装饰器
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