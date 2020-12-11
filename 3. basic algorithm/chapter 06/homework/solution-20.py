# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    非递归(栈)实现{1, 2, 3, ...n}的所有排列数

    比较常用的算法有递归法和字典顺序法(1 2 3 4->1 2 4 3->1 3 2 4)

    非递归栈思路还真没思考过...

    不过既然递归可行, 一般都能转成栈的形式

    基本思路, 以{1, 2, 3}为例, 直接把结果数组压入栈
    初始:
    [1], [2], [3]
    第一步, 出[3], 去numbers里找[3]里不存在的{1, 2}和[3]拼一起入栈, 变成:
    [1], [2], [3, 1], [3, 2]
    第二步同理, 知道出的栈元素长度同待排列长度, 计入结果集

"""
from collections import deque

numbers = {1, 2, 3}

stack = deque()

for e in numbers:
    stack.append([e])  # 注意压的是[1][2][3], 而非1, 2, 3

res = []
while stack:

    t = stack.pop()

    if len(t) == len(numbers):
        res.append(t)  # [1, 2, 3]
    else:
        for e in numbers:
            if e in t: continue
            stack.append(t+[e])  # 比如出[3], 那么压入[3, 1], [3, 2]

print(res)

