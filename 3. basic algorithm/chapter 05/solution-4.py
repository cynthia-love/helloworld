# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    动态数组和摊销

    原理: list在关联底层array的时候, 并不是完全按元素数量来的
    而是先给一定的余量, 占满后, 再整个搬家, 新家再占满后, 再搬到一个更大的房子里, 原房子被系统回收
"""

import sys

# 演示动态扩展
vl = []
for i in range(100):
    print("{}元素, 总占用空间{}字节".format(i, sys.getsizeof(vl)))
    # 注意这里sys.getsizeof()得出的结果仅包括该列表主要结构的大小, 不包括列表元素指向的对象的大小
    vl.append(None)

"""
    0-72, 初始72字节, 存储了当前元素个数, 总支持个数, 底层array首地址(初始None)等信息
    1-104, 增加了32字节, 可以容纳4个8字节64位数
    4-104, 说明这32个里有24个是预留空间, 由接下来的3个元素摊销
    5-136, 又多了32
    8-136
    9-200, 注意这里直接多了64, 即8个地址空间, 说明扩展并不是线性的
    当系统发现你一直在变大, 后面每次扩展的量会越来越大
"""
