# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计算法做自然连接

    数组A(x,y)有n个元素, 数组B(y,z)有m个
    每个是一对数, 比如:
       A         B
    (1, 2)     (2, 8)
    (2, 3)     (3, 9)
    (3, 3)     (2, 11)

    则最终结果:
    (1, 2, 8)
    (1, 2, 11)  # 注意B里的y有两个2, 拼完出来两条
    (2, 3, 9)
    (3, 3, 9)

    即对A的每个元素遍历B, 找到y列相等的项拼接到一起

    ???处理暴力遍历O(n*m), 还有其它思路???
"""

a = [(1, 2), (2, 3), (3, 3)]
b = [(2, 8), (3, 9), (2, 11)]

# 先看一下zip函数的结果
print(list(zip(a, b)))  # [((1, 2), (2, 8)), ((2, 3), (3, 9)), ((3, 3), (2, 11))]

res = []
for e1 in a:
    for e2 in b:
        if e1[1] == e2[0]:
            res.append((e1[0], e1[1], e2[1]))
print(res)

"""
    思路2
       A         B
    (1, 2)     (2, 8)
    (2, 3)     (3, 9)
    (3, 3)     (2, 11)

    则最终结果:
    (1, 2, 8)
    (1, 2, 11)  # 注意B里的y有两个2, 拼完出来两条
    (2, 3, 9)
    (3, 3, 9)
    
    处理A第二对元素的时候, B又从头扫描
    而实际上, 处理A的第一对元素的时候, B已经扫描过一遍了, 可以记下来
"""
from collections import defaultdict

a = [(1, 2), (2, 3), (3, 3)]
b = [(2, 8), (3, 9), (2, 11)]

dd = defaultdict(list)

for e in b:
    dd[e[0]].append(e)  # O(m)

res = []

"""
    外层遍历n次
    但内层每次不一样, n次加一起是m
    
    x1, x2, x3...xn, 其中x1+x2+..+xn = m, 平均到每次是m/n
    
    n*m/n = m???时间复杂度是O(m)???
"""
for e1 in a:

    for e2 in dd[e1[1]]:
        res.append((e1[0], e1[1], e2[1]))

print(res)