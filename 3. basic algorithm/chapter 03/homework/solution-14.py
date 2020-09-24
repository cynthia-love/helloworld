# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明: O(max(f(n), g(n)) = O(f(n)+g(n))

    (这里其实有个隐含约定, 虽然说f(n)是O(g(n))这里的g(n)可能有很多个, 但一般认为就一个最准确的那个
    比如O(n+1), O(n) 都可以认为是f(n) = n的O, 但显然后者更准确)

    假设
    d(n)为O(f(n)), e(n)为O(g(n))
    当n>=k1, d(n) <= c1*f(n)
    当n>=k2, e(n) <= c2*g(n)
    当n>=max(k1, k2), d(n)+e(n) <= max(c1, c2)*(f(n)+g(n))
    所以: d(n)+e(n)是O(f(n)+g(n))

    同样有, 当n>=max(k1, k2)
    d(n)+e(n) <= max(c1, c2)*2*max(f(n), g(n))
    所以: d(n)+e(n)是O(max(f(n), e(n)))的

    从而证明O(max(f(n), g(n)) = O(f(n)+g(n))

"""