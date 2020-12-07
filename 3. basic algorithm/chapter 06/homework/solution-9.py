# -*- coding: utf-8 -*-
# Author: Cynthia

"""

    初始空的循环队列, 固定空间大小30

    执行了32次入队没有触发FullError, 10次取首元素, 15次出队其中5次触发EmptyError

    那么head指针最终指向哪?

    (假设初始指向0, 从元素从1号位开始进)
"""
"""
    分析:
    
    入队不影响head指针位置, EmptyError也不影响
    
    所以影响head指向的只有10次有效dequeue, 每一次head+1
    
    0+10 = 10 < 30, 未循环
    
    所以head指针最终指向index-10
    
"""