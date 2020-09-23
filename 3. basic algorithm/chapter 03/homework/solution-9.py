# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明: d(n)为O(f(n)), 则对于任意常数a>0, ad(n)为O(f(n))
"""

"""
    分析: d(n) <= c*f(n)
    证明的几种方式: 公式证明, 举特例, 逆否命题, 反证法, 归纳法
    
    这里直接公式证明就好
    d(n) <= c*f(n), n>=k
    a*d(n) <= a*c*f(n), a*c > 0, n>=k
    所以a*d(n) 为O(f(n))
    
    
"""