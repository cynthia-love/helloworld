# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    假设爱丽丝选择了三个不同整数, 随机放置在栈S中
    设计程序, 不包含循环和递归, 只包含一次比较和一个变量x
    使得爱丽丝的三个整数中最大的以2/3的概率存储在变量x中

"""

"""
    分析:
    
    比如1 3 2
    
    x先赋值2, 然后3出栈, 做一次比较, x取较大的
    
    证明, 这么设计x取到最大的概率为2/3
    
    三个整数, 每个整数最大的概率都是1/3
    
    如果剩下那个不是最大, 那么x取到的值是前两个的最大, 即整体最大, 概率是1-1/3 = 2/3
    
    如果剩下那个最大, 那么x取到的值是错的, 概率是1/3
    
    综上, 该算法能以2/3的概率取到最大值
    
"""

s = [1, 3, 2]

x = s.pop()

x = max(x, s.pop())

print(x)