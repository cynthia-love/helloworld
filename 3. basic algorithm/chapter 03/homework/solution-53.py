# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    n瓶酒, 其中一瓶有毒, 毒药很致命, 稀释成10亿:1滴也会死人
    但毒药有延时, 中毒后一个月才会死. 设计一个方案, 用一个月的时间, 通过O(n*log(n))个测试者
    确定哪个酒瓶被下毒(题目出错了吧, 是log(n)吧, 不然一人喝一瓶不就行了)

    注意这题, 无法实时知道结果
    实时的思路很简单, 第一个人喝一半, 死了第二个人喝这一半的再一半, 没死第二个人喝另一半的再一半

    非实时就不能这么干了
"""

"""
    这题思路是真的不好想, 二分减治不现实, 一个比较取巧的方法是二进制位, 比如9瓶, 4个人就够
    0000   第一位喝第一位为1的, 第二位喝第二位为1的, 第三位喝第三位为1的, 第四位喝第四位为1的
    0001
    0010
    0011
    0100
    0101
    0110
    0111
    1000
"""
import math
from collections import defaultdict

def f():
    n = 9
    p = int(math.log(n, 2))+1
    d = defaultdict(set)

    # n*log(n)
    for i in range(n):
        for j in range(0, p):
            b = (1 << j) & i  # 编号为i的酒的二进制第j位, 结果为0是0, 结果不为0是1
            if b: d[j].add(i)

    print(d)

    die_state = [True, False, False, False]
    res = {_ for _ in range(n)}

    # 结果集先取全部, 然后死了的且关系, 没死的减去关系(而非或)
    for i in range(p):
        if die_state[i]:
            res &= d[i]
        else:
            res -= d[i]
        print(res)

    print(res)

f()
