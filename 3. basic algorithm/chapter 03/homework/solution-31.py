# -*- coding: utf-8- -*-
# Author: Cynthia

"""
    给出一个包含n个整数的序列S, 算法C对S中的每个偶数执行O(n)的计算时间, 每个奇数O(log(n))
    则算法C的最好和最坏运行时间是什么??
"""

"""
    f(n) = n1*O(n) + n2*O(log(n))
    
    最好, 全是奇数: O(n*log(n))
    最差, 全是偶数: O(n*n)
"""