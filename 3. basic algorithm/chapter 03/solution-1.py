# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    算法分析
    数据结构: 组织和访问数据的一种系统化方式
    算法: 在有限的时间内一步步执行某些任务的过程
"""

"""
    最简单的算法分析的方法是实验研究, 即实际去跑, 看运行时间
    实验研究的问题:
    1. 很难控制完全相同的硬件和软件环境变量, 导致无法精确比较两个算法性能的优劣 
    2. 为了得到实验结果需要给定确定的输入, 而这些输入不一定全面, 可能某些未计入在内的输入对整体
    性能评估影响很大
    3. 算法必须完全实现, 如果只是为了评估算法A好还是B好, 都实现一遍显然是不可取的
"""
import time

def f():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for each in l:
        if each == 8:
            return True
    return False

"""
方法1, 利用time.time()
用这个的问题是, 许多进程共享使用CPU, 所以算法执行过程花费的时间依赖于
作业执行时正运行在计算机上的其他进程
"""
t1 = time.time()
f()
t2 = time.time()
print(t2-t1)

"""
方法2, 利用time.perf_counter(), 会比time更精确些
还有一个time.process_time(), 说是perf_counter会计算sleep, process_time不会
"""
t1 = time.perf_counter()
f()
t2 = time.perf_counter()
print(t2-t1)

"""
方法3, timeit
"""
import timeit
res = timeit.timeit(stmt=f, number=1)  # 注意这里的返回是汇总时间, 比如执行10次, 得除以10才是每次时间
print(res)