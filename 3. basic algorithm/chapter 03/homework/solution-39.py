# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明: 1/2^1 + 2/2^2 + 3/2^3 .. < 2
    1/2^1 + 2/2^2 + 3/2^3 + n/2^n
    = (1/2+1/2^2+..+1/2^n) + (1/2^2+..+1/2^n) + ..+ 1/2^n

    = 1/2*(1-1/2^n)/(1-1/2) + 1/2^2*(1-1/2^(n-1))/(1-1/2) + ...

    = 1-1/2^n + 1/2 - 1/2^n + ...+ 1/2^(n-1) - 1/2^n

    < 1+1/2+..+1/2^(n-1)
    = 1*(1-1/2^n)/(1-1/2)
    = 2-1/2^(n-1)
    < 2

"""