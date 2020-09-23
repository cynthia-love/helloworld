# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明: 若d(n)为O(f(n)), e(n) 为O(g(n)), 则d(n)*e(n)为O(f(n)g(n))

    证明的几种方式: 公式证明, 举特例, 逆否命题, 反证法, 归纳法

    证明:
    d(n)为O(f(n)), 则存在k1, 当n>=k1时, d(n) <= c1*f(n), c1 > 0
    e(n)为O(g(n)), 则存在k2, 当n>=k2时, e(n) <= c2*g(n), c2 > 0

    那么, 取k为max(k1, k2), 当 n>=k时, d(n) <= c1*f(n)和e(n) <= c2*g(n)同时成立
    则: d(n)*e(n) <= c1*c2*f(n)*g(n), c1, c2为正实数常量, 则c1*c2也为正实数常量
    所以: d(n)*e(n)为O(f(n)*g(n))
"""