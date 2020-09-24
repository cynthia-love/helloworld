# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明, 若p(n)为n的多项式, log(p(n))为O(log(n))

    p(n) = a0+a1*n^1+a2*n^2+...+ai*n^i

    log(p(n)) = log(a0+a1*n^1+a2*n^2+...+ai*n^i) <= log((a0+..+ai)*n^i)
    <= i*log(n) + log(a0+...+ai)

    log(p(n)) = O(i*log(n) + log(a0+...+ai)) = O(log(n))
"""