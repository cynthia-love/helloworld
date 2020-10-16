# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    函数调用跟踪装饰器
"""

class Track:
    """
        函数调用跟踪装饰器
    """
    def __init__(self, func):
        """
        初始化函数
        :param func: 待装饰的函数
        """
        self._func = func
        self._mark = 0

    def __call__(self, *args, **kwargs):
        """
        相当于wrapper函数, 接受的参数原封不动地传给原函数
        调用前打印一次信息, 调用后打印一次信息, args, kwargs都拆开后打印
        :param args:
        :param kwargs:
        :return:
        """
        print("{}↓{}({})".format("\t"*self._mark, self._func.__name__,
                                ",".join([str(e) for e in list(args)+list(kwargs.values())])))
        self._mark += 1
        res = self._func(*args, **kwargs)
        self._mark -= 1
        print("{}↑{}({})".format("\t"*self._mark, self._func.__name__,
                                ",".join([str(e) for e in list(args)+list(kwargs.values())])))
        return res

    # 下面这个方法是为了保证加了装饰器的函数取__name__等属性时还能取到原函数的属性, 而不是Track实例的
    def __getattribute__(self, item):
        # 这个要单摘出来, 因为就这个属性装饰器优先于原函数
        # 其他的属性优先返回原函数本身的, 找不到才去找instance自己的
        # 注意装饰器类中不要用太多和原函数同名的属性, 不然会取到原函数的
        # 要么就像_func一样去特殊处理

        if item == '_func':
            return super().__getattribute__(item)

        # 多加一个参数用于表示层级
        if item == '_mark':
            return super().__getattribute__(item)

        try:
            return self._func.__getattribute__(item)
        except AttributeError:
            try:
                return super().__getattribute__(item)
            except AttributeError:
                raise AttributeError
