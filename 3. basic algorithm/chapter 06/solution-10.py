# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    双端队列, double-ended queue, 简写deque

    并不是栈+队列
    栈: 尾进尾出, 队列: 尾进头出
    而双端队列是两边都能进都能出

"""
"""
    双端队列的ADT
    add_left(e)
    pop_left()
    left()
    add_right(e)
    pop_right()
    right()
    
    empty()
    len(d)
"""
"""
    实现方案:
    类似队列实现改进方法3-可扩展/缩小的循环数组
    
    注意, 头部, 尾部, 元素个数三个存其二即可算出来剩下那个
    
    建议存头部, 元素个数, 逻辑上更好理解
"""

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Deque:
    pass

