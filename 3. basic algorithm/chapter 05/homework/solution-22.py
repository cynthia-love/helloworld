# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    做实验比较extend和append在等量任务时效率的不同
"""
import time

l1, l2 = [], []

l3 = [i for i in range(10000000)]

t1 = time.time()
l1.extend(l3)
t2 = time.time()
print(t2-t1)

t1 = time.time()
for i in range(10000000):
    l2.append(i)
t2 = time.time()
print(t2-t1)

# append达到了extend的10倍左右