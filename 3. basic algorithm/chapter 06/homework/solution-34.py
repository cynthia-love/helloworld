# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    后缀表达式1. 生成树 2. 计算值
"""
from collections import deque
s1 = '12*24*+'
s2 = '12+24+*'

# 方法1, 直接算
def f1(exp):

    s = deque()

    for e in exp:

        if e in '+-*/':
            # 是操作符, 说明上两个入栈的字符分别为左右操作数
            r = s.pop()
            l = s.pop()

            # 如果觉得eval不合适可以自己写函数, 判断操作符, 分别做不同计算
            s.append(str(eval(l+e+r)))

        else:
            # 数字直接入栈
            s.append(e)

    return float(s.pop())

print(f1(s1))
print(f1(s2))

# 方法2, 先生成树再处理
class BiTree:

    class Node:
        def __init__(self, e=None):
            self.e = e
            self.l = None
            self.r = None

    def __init__(self):
        self._root = None

    def build(self, s):
        stack = deque()
        # 构建过程同方法1中的直接算
        for e in s:

            if e in '+-*/':
                node = BiTree.Node(e)
                node.r = stack.pop()
                node.l = stack.pop()

                stack.append(node)

            else:
                stack.append(BiTree.Node(e))

        self._root = stack.pop()

    def calculate(self):

        def rf(node):

            if node.e.isnumeric():

                # 数字直接返, 注意这里是字符
                # 为了兼容单节点的情况, 也做一步转换
                return eval(node.e)

            else:
                l = rf(node.l)
                r = rf(node.r)

                # 多用format, 可以规避参数是数字还是字符的判断
                return eval("{}{}{}".format(l, node.e, r))

        return rf(self._root)

bt = BiTree()
bt.build(s1)
print(bt.calculate())
bt.build(s2)
print(bt.calculate())
