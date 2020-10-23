# -*- coding; utf-8 -*-
# Author: Cynthia

"""
    证明draw_interval(c)函数打印的行数是2^c-1
    打印的短线数量是2^(c+1)-c-2
"""

"""
    归纳法证明第一个:
    1. 当c=0时, 2^0-1 = 0
       当c=1时, 2^1-1 = 1, 符合要求
    2. 假设当c=k时, 打印行数2^k-1
       则当c=k+1时, 打印行数2^k-1+1+2^k-1 = 2^(k+1)-1
    3. 综上, draw_interval(c)函数打印的行数是2^c-1
    
    再证明第二个结论:
    以c=3为例
    3, 2*2, 4*1
    
    2^(c+1)-c-2
    
    当c=0时, 0
    当c=1时, 就一道, 1
    假设当c=k时成立
    那么当c=k+1时, 划线数量为: 2^(k+1)-k-2 + (k+1) + 2^(k+1)-k-2
    = 2^(k+1+1)-(k+1)-2
    综上, 结论成立

"""
from helloutils.tracker import Track

def draw_line(length, label=''):
    s = '-'*length+' '+label
    # print(s)

@Track
def draw_interval(length):
    if length == 0: return
    draw_interval(length-1)
    draw_line(length)
    draw_interval(length-1)

draw_interval(3)