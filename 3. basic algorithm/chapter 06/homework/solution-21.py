# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    使用栈和队列非递归地生成一个含n个元素的集合的所有可能的子集集合
"""

"""
    分析, 子集集合首选二进制位, 从0到2^n-1去遍历
    
    但是这题有明显的要求, 栈和队列, 非递归
    
    {A, B, C, D, E}
    
    大致思路, 从{}开始, 先生成长度为1的, 再2的, 再3的
    
    {}
    {A}, {B}, {C}, {D}, {E}
    
    {B}, {C}, {D}, {E}, {AB}, {AC}, {AD}, {AE}
    
    {C}, {D}, {E}, {AB}, {AC}, {AD}, {AE}, {BC}, {BD}, {BE}
    
    {AB}, {AC}, {AD}, {AE}, {BC}, {BD}, {BE}, {CD}, {CE}, {DE}
    
    {AC}, {AD}, {AE}, {BC}, {BD}, {BE}, {CD}, {CE}, {DE}, {ABC}, {ABD}, {ABE}
    
    好像用不到栈

"""
from collections import deque

l = ['A', 'B', 'C', 'D', 'E']

def f1():
    queue = deque()
    queue.append([])
    # 这里队列元素用了个[]而非{}是为了找到倒数第一个元素
    # 比如[A, C], 生成长度为3的子集的时候, 从D开始遍历
    # 如此可以保证不重复, 从而省去去重步骤

    res = []

    while True:

        head = queue.popleft()
        res.append(head)

        if len(head) == len(l):
            break
        # 拼接后长度等于元素个数, 说明处理完了

        pos = 0 if not head else l.index(head[-1]) + 1

        for i in range(pos, len(l)):
            queue.append(head + [l[i]])

    return res


r1 = f1()

"""
    方法2, 栈, 其实无非就是广度优先和深度优先
    暂未想到方法怎么能同时用到队列和栈
    
    {}
    {A}, {B}, {C}, {D}, {E}
    
    {A}, {B}, {C}, {D}
    
    {A}, {B}, {C}, {DE}
    
    {A}, {B}, {C}
    
    {A}, {B}, {CD}, {CE}

"""

def f2():

    stack = deque()
    stack.append([])

    res = []

    while stack:

        top = stack.pop()
        res.append(top)

        pos = 0 if not top else l.index(top[-1])+1

        for i in range(pos, len(l)):
            # 如果还有可拼接元素, 拼接后入栈
            stack.append(top+[l[i]])

    return res

r2 = f2()

r1.sort()
r2.sort()
print(r1)
print(r2)

