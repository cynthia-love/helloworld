# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    4头牛, 过桥耗时分别为2, 4, 10, 20
    过桥需要特定装置, 该装置最多两头同时过, 且按最慢的速度走, 装置只有一个

    问怎么34分钟过完?

    2, 4过桥, 耗时4
    2把装置带回去, 耗时2
    10, 20过桥, 耗时20
    4把装置回去, 耗时4
    2, 4过桥, 耗时4
    总耗时34

    分析, 这个思路能抽象化吗?
    首先, 目标改一下, 怎么最少时间过完

    {2, 4, 10, 20}  {}
    {10, 20}        {2, 4}  奇数步, 装置在左边, 右边没有, 走最小的两个
    {2, 10, 20}     {4}     偶数步, 装置在右边, 右边得回来, 显然, 优先回来最小的
    {2}             {4, 10, 20} 奇数步, 装置在左边, 右边有, 走最大的两个
    {2, 4}          {10, 20}    偶数步, 装置在右边, 右边得回来个最小的
    {}              {2, 4, 10, 20}  奇数步, 装置在左边, 直接过去

    原则总结:

    首先处理特殊情况, 就一只, 装置初始在左边, 直接过, 否则:

    划分为四种状态(这种思路会比设置多个字段去判断处理逻辑更清晰)
    初始状态0, 最小的两个移到右边, 装置带到右边, 状态1
    单2回到左边, 装置带回左边, 状态2
    左边最大俩移到右边, 装置带到右边, 状态3
    4回到左边, 装置带到左边, 回到状态0

"""
from collections import deque

left = deque([2, 4, 10, 20])  # 若无序, 先排序
right = deque([])

def f():

    # 如果就一头牛, 直接过去
    if len(left) == 1: return left[0]

    res = 0

    state = 0

    while left:

        if state == 0:
            # 保证左边最左侧是2, 4的顺序
            # 右边最左侧也是2, 4的顺序
            t1 = left.popleft()
            t2 = left.popleft()
            print(left, "->{},{}->".format(t1, t2), right)
            right.appendleft(t2)
            right.appendleft(t1)

            state = 1
            res += t2

        elif state == 1:
            t = right.popleft()
            print(left, "<-{}<-".format(t), right)
            left.appendleft(t)

            state = 2
            res += t

        elif state == 2:

            t2 = left.pop()
            t1 = left.pop()

            print(left, "->{},{}->".format(t1, t2), right)

            right.append(t1)
            right.append(t2)

            state = 3
            res += t2

        else:
            t = right.popleft()
            print(left, "<-{}<-".format(t), right)
            # 这里4回去, 保证左边是2, 4的顺序, 要先把2出出来
            l = left.popleft()
            left.appendleft(t)
            left.appendleft(l)
            state = 0
            res += t

    return res
print(f())







