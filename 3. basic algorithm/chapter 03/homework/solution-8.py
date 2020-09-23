# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    根据渐进增长率对下面函数排序
    4nlog(n)+2n     O(n*log(n)) 4
    2^10            O(1)
    2^log(n)=n      O(n)        1
    3n+100log(n)    O(n)        3
    4n              O(n)        4
    2n              O(n)        2
    n^2+10n         O(n^2)      1
    n^3             O(n^3)      1
    nlog(n)         O(n*log(n)) 1

    同数量级内的看系数
"""