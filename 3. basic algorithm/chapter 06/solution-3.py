# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    栈的应用-数据逆置
"""
from collections import deque

def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed"""

    s = deque()

    with open(filename, 'r') as f:

        for line in f:
            s.append(line.rstrip('\n'))  # 去掉行尾的换行符; 注意strip可以指定字符

    with open(filename, 'w') as f:

        while s:
            f.write(s.pop()+'\n')

reverse_file('data/data1.txt')