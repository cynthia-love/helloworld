# -*- coding: utf-8 -*-
# Author: Cynthia

"""

    对于任意正整数n, 0~2n范围内, 所有偶数的和是多少

    2+6+8+...+2n = n*(2n+2)/2 = n*(n+1) = n*n+n

    证明:
    当n=1时, 1*1+1 = 2 成立
    假设当n=k时, 2+6+8..+2k = k*k+k
    那么当n=k+1时, 2+6+8+2k+2(k+1) = k*k+k+2k+2 = (k+1)^2 + (k+1)
    所以对n=k+1也成立
    所以结论成立
"""

res = 0
k = 1
while k <= 10:
    res += 2*k

"""
    利用循环不变量证明上述循环算法最终可以求得2+4+6+..+20
    
    1. 选取循环不变量L(k) = 2+4+6+..+2*k
    2. 当循环开始时, L(开始) = 0, 成立
    3. 假设第i轮循环后成立, L(i) = 2+4+..+2*i
    则第i+1轮结束后, L(i+1) = L(i) + 2*(i+1) = 2+4+..+2*(i+1)
    循环不变量成立
    4. 循环退出k=10, L(10) = 2+4+..+2*10, 刚好是要求的的2+4+  +20的和
"""