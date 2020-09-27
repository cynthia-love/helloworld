# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明: log1+log2+..+logn 的运行时间是Ω(n*logn)

    t(n) = t(log1)+t(log2)+..+t(logn)+n-1

    ???这么好像证不出来...

    log(n!) 这么证呢
    不行

    感觉和51一样, 题目出的有问题
    f(n) = 1+2+3...+n, 不能直接说求1-n和的公式运行时间是O(n^2)

    f(n)只是数学公式, 又不是运行时间随输入量级的公式

    直接用n*(n+1)/2, 一步就求出来了, O(1)

    所以抛开具体实现算法本身, 去说某一个公式的运行时间是xx, 是有问题的

    这题应该这么描述
    for i in range(n):
        xxx

    循环内的耗时不是固定的, 而是随i变化, i=1时是log1, i=2时是log2, i=n时是logn

    总时间复杂度: t(n) = log1+log2+...+log(n)

    证明t(n) 是 Ω(n*log(n))的

    这么表述就没那么难理解了

    题目变为: 证明存在k, 当n>=k时, 有正实数c, log1+log2+...+log(n) >= c*n*log(n)成立

    1. 另c=1/2, n=1时成立
    2. 假设n=k时成立, log(1*2*..*k) >= 1/2*k*log(k)
    那么当n=k+1时, log(1*2*..*k*(k+1)) 和 1/2*(k+1)*log(k+1)比较
    左边增加 log(k+1), 右边增加0.5*k*log(k+1)+0.5*log(k+1)-0.5*k*log(k)
    左边增加-右边增加 = 0.5*log(k+1)-0.5*k*log(k+1)+0.5*k*log(k)
    = 0.5*(1-k)*log(k+1)+0.5*k*log(k)
    去掉0.5=log((k+1)^(1-k))+log(k^k) = log(k^k/(k+1)^(k-1))...不会证了, 不过这里确实是大于0的

    要么就直接证: log(n!) 是Ω(n*log(n))的
    log(n!) >= c*n*log(n)
    n! >= n^cn 不可能啊....
"""