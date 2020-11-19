# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    比较列表推导式和重复append之间的相对效率
"""
import time
r = range(1000000)

t1 = time.time()
l1 = [e for e in r]
t2 = time.time()
print(t2-t1)

l2 = []
t1 = time.time()
for i in range(1000000):
    l2.append(i)
t2 = time.time()
print(t2-t1)

# 后者大概是前者的两倍

l3 = []
t1 = time.time()
l3.extend(r)
t2 = time.time()
print(t2-t1)

# extend又比列表推导式更优???

"""
    总结: extend优于列表推导式优于append
    extend优于列表推导式因为extend不用动态拓展, 列表推导式本质上也是不断LIST_APPEND
    列表推导式优于append因为虽然两者都是一个个append, 但列表推导式有内置命令, 而append
    每次调用都需要往内存加载append函数, 两者主要差在这了
"""