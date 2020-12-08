# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    可扩展/缩小的循环队列, resize时为什么不能直接复制???
"""

"""
    分析: 新老head不一致, capacity不一致
    假设head指向第一个而不是前一个, 便于分析:
    
                  ↓
    4 5 x x x x x 1 2 3     1 2 3 4 5
    ↓
    4 5 x x x x x 1 2 3 x x x x x x x x x x     4 5 x x x
    
    当然, 按len复制更不行了
    data2[k] = self._data[k]
    
    4 5 x x x
    
    不光输出不了1, 2, 3, 直接存都不存了
    
    
"""