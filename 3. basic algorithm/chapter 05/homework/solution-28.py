# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    二进制字符串转十进制整数

    110->6
"""

s = '110'

res = 0

for each in s:

    res = res*2+(1 if each == '1' else 0)

print(res)