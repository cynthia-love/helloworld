# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    Python的字符串类入门

    从单字节-双字节看存储结构

    从下面的例子可以看出, 字符串应该是非动态非引用数组

    不然每个元素占用大小应该就是固定的了(地址)
"""
import sys
print(sys.getsizeof(''))  # 49
print(sys.getsizeof('1'))  # 50
print(sys.getsizeof('我'))  # 76
print(sys.getsizeof('我1'))  # 78

"""
    如果只有ascii字符, 则一个字符占1字节
    如果有unicode字符, 则自动变为一个字符占2字节, 哪怕里面存的是ascii字符
    
    另, unicode字符比ascii也会占用更多的额外信息存储空间
"""