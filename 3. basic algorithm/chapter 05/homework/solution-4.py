# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    修改自定义动态引用数组的__getitem__方法, 使其支持负索引
"""

import ctypes

class DynamicQuoteArray:

    def __init__(self):

        self.size = 1
        self.len = 0

        self.array = self.make_array(self.size)