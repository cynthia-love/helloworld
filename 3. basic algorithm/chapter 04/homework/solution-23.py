# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现一个文件夹遍历递归函数
"""

"""
    思路1, 库函数
"""

import os

for root, dirs, files in os.walk("../..", True):
    print(root)

    for each in files:
        print(os.path.join(root, each))

"""
    思路2, 自己实现递归
    
"""
print("========================================")
def find(path, filename):

    p = os.path.join(path, filename)
    print(p)

    if os.path.isdir(p):
        for each in os.listdir(p):
            find(p, each)

find("..", "..")

# 为什么题目要求俩参数呢, 一个不更简洁
print("========================================")
def find2(path):
    print(path)
    if os.path.isfile(path):
        return

    for each in os.listdir(path):
        find2(os.path.join(path, each))

find2("../..")