# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明, 当且仅当g(n)为Ω(f(n))时, f(n)为O(g(n)) (即充要条件)

    证明的几种方式: 公式证明, 举特例, 逆否命题, 反证法, 归纳法


    先证明A->B:
    g(n)为Ω(f(n))
    即存在k1, 当n>=k1时, g(n) >= c1*f(n), 即f(n) <= 1/c1*g(n)
    c1为正实数, 1/c1也是, 所以f(n)是O(g(n))

    再证B->A:
    f(n)为O(g(n))
    即存在k2, 当n>=k2时, f(n) <= c2*g(n), 即g(n) >= 1/c2*f(n)
    c2位正实数, 1/c2也是, 所以g(n)是Ω(f(n))的

    综上, 证明: 当且仅当g(n)为Ω(f(n))时, f(n)为O(g(n))

"""