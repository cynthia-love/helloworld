# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    重写自定义动态引用数组的insert的方法, 使得大小调整的时候元素就插入完毕而不是复制+移动两遍O(n)
"""