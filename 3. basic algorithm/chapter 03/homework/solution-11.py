# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明: 若d(n)为O(f(n)), e(n)为O(g(n)), 则d(n)+e(n)为O(f(n)+g(n))

    d(n)为O(f(n)), 即存在k1, 当n>=k1时, 有正实数c1, 使得: d(n) <= c1*f(n)
    e(n)为O(g(n)), 即存在k2, 当n>=k2时, 有正实数c2, 使得: e(n) <= c2*g(n)

    那么, 取k为max(k1, k2), 当n>=k时:
    d(n)+e(n) <= c1*f(n)+c2*g(n), 取c=max(c1, c2)
    d(n)+e(n) <= c*f(n)+c*g(n) <= c*(f(n)+g(n))
    从而证明: d(n)+e(n)为O(f(n)+g(n))
"""