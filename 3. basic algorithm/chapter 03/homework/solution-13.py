# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明: d(n)为O(f(n)), f(n)为O(g(n)), 则d(n) 为O(g(n))

    d(n)为O(f(n)), 存在k1, n>=k1时, d(n) <= c1*f(n), c1为正实数
    f(n)为O(g(n)), 存在k2, n>=k2时, f(n) <= c2*g(n), c2为正实数

    取k为max(k1, k2), 则当n>=k时
    d(n) <= c1*f(n) <= c1*c2*g(n), c1, c2为正实数, 则c1*c2为正实数
    所以d(n)是O(g(n))的

"""