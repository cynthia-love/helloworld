# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    评估pop(k)的效率
"""
"""
    pop(), 始终pop最后一个, 不涉及元素移动, O(1), 有时候数组会缩小, 摊销后还是O(1)
    
    pop(n//2), pop中间的, 后一半元素要往前移动, O(n), 考虑数组缩小还是O(n)
    
    pop(0), pop开头的, 后面的元素都要往前移动, O(n), 考虑数组缩小还是O(n)
"""
import time

def f1(n):
    l = [i for i in range(n)]

    t1 = time.time()

    l.pop(0)

    t2 = time.time()
    print((t2-t1)*1000000)

def f2(n):
    l = [i for i in range(n)]

    t1 = time.time()

    l.pop(n//2)

    t2 = time.time()
    print((t2 - t1)*1000000)

def f3(n):
    l = [i for i in range(n)]

    t1 = time.time()

    l.pop()

    t2 = time.time()
    print((t2 - t1)*1000000)

f1(100)
f1(1000)
f1(10000)
f1(100000)
f1(1000000)
print('===')
f2(100)
f2(1000)
f2(10000)
f2(100000)
f2(1000000)
print('===')
f3(100)
f3(1000)
f3(10000)
f3(100000)
f3(1000000)
