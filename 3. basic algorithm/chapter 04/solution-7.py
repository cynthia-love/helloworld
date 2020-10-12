# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    最大递归深度

    python一般规定最大递归深度为1000, 防止资源耗尽

    当然, 可以手动去改
"""
import sys

def f():
    f()

# f()

print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())
