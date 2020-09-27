# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明log1+log2+...+logn的运行时间是n*log(n)

    t(n) = t(log1)+t(log2)+..+t(logn)+n-1
    <= n*t(log(n))+n-1

    这里是把log(n)的时间认为是log(n)了吧, 而不是认为是原子操作1???

    t(n) <= n*log(n)+n-1 <= c*n*log(n)
"""