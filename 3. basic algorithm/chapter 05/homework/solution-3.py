# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明列表删除元素时, 其底层数组大小偶尔也会收缩

    list长度53, 占用空间920
    list长度52, 占用空间584

"""
import sys

l = [e for e in range(100)]

while l:

    l.pop()

    print("list长度{}, 占用空间{}".format(len(l),sys.getsizeof(l)))


