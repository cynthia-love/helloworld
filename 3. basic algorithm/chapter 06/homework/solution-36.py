# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    计算股票总收益

    输入为一系列单只股票的连续操作:

    0, 20.00, 35  以20.00的价格买入35股
    0, 25.00, 40
    1, 31.00, 10  以31.00的价格卖出10股

    假设不存在卖空

    计算连续操作结束后的最终收益

    收益计算先买先卖而非平均成本, 比如此例卖出的10股, 单价为20的足够, 所以收益

    (31-20)*10

"""

"""
    基本思路:
    双端队列, 买入队, 卖出队
    
    比如: (20.00, 35), (25.00, 40)
    卖10, 从第一个开始出队, 直到够卖的
    
"""
from collections import deque

trade = [(0, 21.00, 35), (0, 24.00, 20), (1, 26.00, 10), (0, 21.00, 10), (1, 20.00, 30)]

profit = 0

position = deque()

for tag, price, amount in trade:

    if tag == 0:
        position.append((price, amount))
    else:

        ta = amount

        while ta > 0:

            lp, la = position.popleft()

            # 如果刚好覆盖, 则计算完利润退出即可
            if la == ta:

                profit += (price-lp)*ta
                break

            # 如果买入量大于卖出, 剩下的还得回到队首
            if la > ta:
                profit += (price-lp)*ta
                position.appendleft((lp, (la-ta)))
                break

            # 如果买入量小于卖出, 继续读取下一个买入
            profit += (price-lp)*la
            ta -= la

print(profit)
