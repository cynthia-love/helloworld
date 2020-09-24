# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明: 若b>1, logb(f(n) 为 θ(log(fn))
"""

"""
    证明: logb(f(n)) <= c*log(f(n))
    
    logb(f(n)) = log(f(n))/log(b), log(b)为常数, 取任意c > 1/log(b)
    则log(f(n))/log(b) <= c*log(f(n))
    即logb(f(n)) 是O(log(f(n))的
"""