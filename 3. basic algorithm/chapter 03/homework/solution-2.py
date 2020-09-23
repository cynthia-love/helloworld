# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    算法A和B的时间复杂度分别为:
    8*n*log(n)和2*n*n
    确定k, 当n>=k时, A优于B

    8*n*log(n) <= 2*n*n
    4*log(n) <= n

    当n=16时, 左边=右边=16
    证明, n>=16时, 8*n*log(n) <= 2*n*n, 即 4*log(n) <= n


    1. n=16时满足
    2. 假设n=k时满足 4*log(k) <= k
    则n=k+1时, 左边增加4*log(k+1)-4*log(k), 右边增加1
    4*log(k+1)-4*log(k) = 4*log(1+1/k) <= 4* log(1+1/16) = 0.35
    即左边增加不如右边大, 所以满足4*log(k+1) <= k+1
    3. 根据上述推导可以得出, 当n>=16时, 8*n*log(n) <= 2*n*n

"""