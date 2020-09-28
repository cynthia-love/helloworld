# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    绘制标尺
    有点绕, 其实是这么回事, 每两个大刻度之间有多少刻度取决于
    大刻度的长度,比如:
    -- 0
    -
    -- 1, 大刻度长度是2, 那么中间减一下就变成了1, 中间只有一个

    --- 0
    -
    --
    -
    --- 1, 大刻度3, 中间减一下变成2, 2的话显然还能减, 所以上下各多了一道长度为1的
    -
    --
    -
    --- 2

    享用递归, 首要是去思考边界条件和递推式

"""

# 比如画一个5个刻度的, 即0-1-2-3-4, 然后大刻度高度为3
def draw_line(length, label=''):
    s = '-'*length+' '+label
    print(s)

def draw_interval(length):
    if length == 0: return
    draw_interval(length-1)
    draw_line(length)
    draw_interval(length-1)

num_inches, max_length = 5, 4
for i in range(num_inches-1):
    draw_line(max_length, str(i))
    draw_interval(max_length-1)

draw_line(max_length, str(num_inches-1))
