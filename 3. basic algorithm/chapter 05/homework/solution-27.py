# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    十进制整数转二进制字符串
    比如3: 11, 6: 110
"""

k = 6

sb = str(bin(k))[2:]
print(sb)

# 思路2, 不停地除以2
res = ''

while k >= 1:

    res = str(k % 2) + res

    # k = k // 2
    k = k >> 1

print(res)

# 思路2, 按位与
res = ''
k = 6
i = 1

while i <= k:
    # 比如10-110, 按位与, 10, 判断是否不是0
    res = ('1' if i & k else '0') + res
    i <<= 1

print(res)