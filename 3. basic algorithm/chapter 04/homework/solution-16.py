# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个递归, 输出字符串的逆序
    比如: abc, 输出cba
"""

"""
    分析: 输出abc = 输出ab, 然后输出c
"""

def rf(s):
    if len(s) == 0:
        print(s)
        return

    rf(s[1:])
    print(s[0])

rf("abcde")

"""
    如果是要得到完整串呢
    f(abcde) = f(bcde)+'a'
"""
from helloutils.tracker import Track
@Track
def rf2(s):
    if len(s) == 0: return s
    return rf2(s[1:])+s[0]
rf2("abcde")