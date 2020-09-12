# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    作用域和命名空间
    命名空间以字典形式管理当前作用域内定义的所有标识符
"""

def f(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    c = a+b
    print(dir())  # ['a', 'b', 'c'], 函数的命名空间包括形参标识符和局部变量标识符
    return c

x = 8  # 标识符赋值时都有相应的作用范围, 即作用域; 右边可用来赋值的value称为第一类对象, 比如int, 函数, 类
y = f(x, 10)  # 确定与标识符相关联的值的过程称为名称解析, 解析时先查找本地命名空间, 没有再往外找
print(dir())  # 返回当前命名空间的所有标识符, 即命名空间的.keys()
# [..., ..., ..., 'f', 'x', 'y']
print(vars())  # 返回当前命名空间的完整字典形式{k: v}

"""
    进一步分析这个文件(先理解好什么叫第一类对象, 什么叫标识符)
    第一类对象有8, 10, 18, 相加函数, 这些是作为value值实际占用空间的
    全局的标识符x指向8, 标识符y指向18, 标识符f指向相加函数, 10没有标识符指定
    函数f里的标识符a指向8, b指向10, c指向18
"""
f2 = f  # 这里f是标识符而不是第一类对象, 所以这句话只是给相加函数多了个标识符, 而没有创建新的函数
# 对于函数来说, def f(), 才是创建了新的函数, 并将标识符f指向该函数