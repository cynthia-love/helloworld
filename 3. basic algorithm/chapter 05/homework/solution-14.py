# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    使用random.shuffle对list重新排序, 使得每种可能顺序出现的概率相等
    然后借助random.randrange, 自己实现一个random.shuffle
"""

import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(l)
print(l)

# 补充一个利用shuffle从n个里随机选m个的用法
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(l)
print(l[:5])  # 从10个里随机选5个

"""
    自定义实现思路1
    枚举所有排列, 然后用randrange从里面随机选一个
    0, 1, 2, 3
    0, 1, 3, 2
"""

def f1():
    l = ['A', 'B', 'C', 'D']

    r = []

    def rf(base, res):
        if not base:
            # 注意这里插进去的要是个副本
            # 不然后面的递归函数里res会被改变
            r.append(res.copy())

        for e in base.copy():

            base.remove(e)
            res.append(e)

            rf(base, res)

            res.remove(e)
            base.append(e)

    rf(l, [])

    return r[random.randrange(len(r))]

print(f1())

"""
    自定义实现思路2
    基本同思路1, 只不过算排列的方法可以优化
    
    0, 1, 2, 3
    0, 1, 3, 2
    0, 2, 1, 3
    0, 2, 3, 1
    0, 3, 1, 2
    
    本质上是一个从小到大排列的n进制数序列
    
    算法机制: 
    初始0~n-1, 升序, 从右往左, 只要是升序一直遍历
    
"""

def f2():
    i2s = ['A', 'B', 'C', 'D']
    seed = list(range(len(i2s)))
    res = [seed]

    # 计算下一个

    while True:

        p = len(seed)-1

        # 从右往左找到升序的最后一个元素
        while p >= 1:
            if seed[p-1] > seed[p]:
                p -= 1
            else:
                # 内层break中断的是内层while
                break
        else:
            # 外层break, 如果内层循环完, 则中断外层while
            # 表示已经是倒叙了3, 2, 1, 0, 已得到所有排列
            break

        # 将右侧升序的刚好大于最左大值左边的元素的元素与其互换
        # 比如0, 1, 3, 2是1和2互换; 而0, 2, 3, 1是2和3互换

        t = len(seed)-1
        while t >= p and seed[t] < seed[p-1]:
            t -= 1
        seed[t], seed[p-1] = seed[p-1], seed[t]

        # 然后将原右侧升序部分倒转, p到最后一个元素的部分
        l, r = p, len(seed)-1
        while l < r:
            seed[l], seed[r] = seed[r], seed[l]
            l, r = l+1, r-1

        res.append(seed.copy())

    return [i2s[i] for i in res[random.randrange(len(res))]]

print(f2())

