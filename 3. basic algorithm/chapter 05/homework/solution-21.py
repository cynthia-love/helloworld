# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    评估以下几种字符串拼接方法的效率
"""
import sys
import timeit
def f1():
    s = 'hello world'
    r = ''
    for e in s:
        r += e
    return r

print(timeit.timeit(f1, number=1000000))  # 0.89

def f2():
    s = 'hello world'
    r = []
    for e in s:
        r.append(e)
    return ''.join(r)
print(timeit.timeit(f2, number=1000000))  # 1.20

def f3():
    s = 'hello world'
    return ''.join([e for e in s])

print(timeit.timeit(f3, number=1000000))  # 0.80

def f4():
    s = 'hello world'
    return ''.join(e for e in s)
print(timeit.timeit(f4, number=1000000))  # 1.11

"""
    ???可能和预期的不太一样
    最优的是: 数组表达式生成数组, 然后对该数组做join, 两步都能提前知道大小
    
    次优的是: 直接一次遍历+=拼接, 提前不知道大小
    
    接着是: 得到生成器, 然后对该生成器做join, 提前不知道大小
    
    最后是: append生成数组, 然后join拼接, 第一步不提前知道大小
    
    假设提前知道大小, 那么时间可以忽略
    
    方法1, 0
    方法2, 仅考虑+=拼接时间, 提前不知道大小
    方法3, 仅考虑join拼接时间, 提前不知道大小
    方法4, 仅考虑append生成数组时间, 提前不知道大小
    
    即在不提前知道大小的情况下, += 优于 join 优于 append
    怀疑 += 解释器有做什么优化
    
    综上, 优先数组表达式, 优化了的+=
    生成器虽然时间上慢了点, 但空间性能好, 也可以考虑
    
    append少用
"""