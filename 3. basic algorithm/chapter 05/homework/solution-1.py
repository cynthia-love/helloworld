# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    不停地往list里插入元素
    观察空间占用情况
"""
import sys
l = list()

for i in range(100):
    print("{}个元素, 占用空间{}".format(i, sys.getsizeof(l)))
    l.append(i)

"""
    0个元素, 占用空间72
    1个元素, 占用空间104
    2个元素, 占用空间104
    3个元素, 占用空间104
    4个元素, 占用空间104
    5个元素, 占用空间136
    
    显然, 每个元素占用空间32/4 = 8
    
    第一次扩展32字节
    
    第二次扩展32
    
    第三次扩展64
    
    第四次72
    
    第五次80
    
    好像没什么规律性
"""