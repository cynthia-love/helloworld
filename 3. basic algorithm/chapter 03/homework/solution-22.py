# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    证明, 若f(n)为正, 非递减, 且恒大于1, 则f(n)的上界为O(f(n))

    f(n) <= 上界(f(n)) <= f(n)+1 <= f(n)+f(n) <=2*f(n)

    所以上界f(n)是O(f(n))的
"""