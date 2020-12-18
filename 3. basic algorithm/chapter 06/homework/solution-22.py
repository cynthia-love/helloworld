# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    后缀表示法转换, 只涉及单个数字及+-*/()

    比如: ((5+2)*(8-3))/4
    的后缀表示法为: 52+83-*4/

    本题练习:
    1. 表达式转成后缀表达式
    2. 根据后缀表达式生成树
    3. 将树前中后序遍历
    4. 将树还原成原表达式(可以多加括号), 比如
    ((5+2)*(8-3))/4 变成 (((5+2)*(8-3))/4)

"""
"""
    思路, 一句话介绍的话, 用栈暂存左边界和操作符
    
    a op b -> a b op
    具有明显的递归思路, 但是这种递归需要先生成树...
    
    '((5+2)*(8-3))/4'
    
    (
    ((
    遇到5, 直接加到res里去
    遇到+, 因为是后缀, 需要把b部分加完res才能加+, 所以入栈
    遇到2, 加到res里去
    遇到), 说明局部表达式到头了, 把栈中的元素出到(或者空, 此时式子其实变成(*(8-3))/4
    遇到*, 同样, 要入栈
    遇到(, 入栈
    遇到8, 加到res里去
    遇到-, 入栈
    遇到3, 加到res里去
    遇到), 完成局部处理
    再遇到), 式子其实变成(*)/4, 出*加到res里, 出(
    遇到/, 入栈
    遇到4, 加到res里去
    最后, 把栈里剩的/加到res里去
    
    换一个角度, 表达式的变化情况
    ((5+2)*(8-3))/4             空
    ((+2)*(8-3))/4              5
    ((+)*(8-3))/4               52
    (*(8-3))/4                  52+
    (*(-3))/4                   52+8
    (*(-))/4                    52+83
    (*)/4                       52+83-
    /4                          52+83*
    /                           52+83*4
    空                          52+83*4/
        
        
    再比如'2*3+3*4'
    2*3+3*4         空           空
    *3+3*4          空           2
    3+3*4           *            2
    +3*4            *            23
    3*4             +            23*
    *4              +            23*3
    4               +*           23*3
    空              +*           23*34
    空              空           23*34*+
    
"""
from collections import deque

s = '((5+2)*(8-3))/4'

# s = '2*3+3*4'
def f1():
    stack = deque()
    res = deque()
    prior = {'+': 0, '-': 0, '*': 1, '/': 1}

    for e in s:
        # 如果是数字, 直接入队
        if e.isdigit():
            res.append(e)
        # 如果是左括号, 直接入队
        elif e == '(':
            stack.append(e)
        # 如果是右括号, 把栈里元素出栈入队直到遇到(
        elif e == ')':
            while stack:
                top = stack.pop()
                if top == '(':
                    break
                res.append(top)
        else:
            # 否则, 是运算符, 把优先级高的出栈入队然后把当前运算符入栈
            while stack:
                top = stack[-1]
                if top in ['+', '-', '*', '/'] and prior[top] >= prior[e]:
                    res.append(stack.pop())
                else:
                    break
            stack.append(e)
        print(stack, res)

    # 把栈里剩余元素出栈入队
    while stack:
        res.append(stack.pop())
        print(stack, res)
f1()

"""
    将后缀表示法转化成二叉树, 并进行前中后遍历以及还原表达式
    52+83-*4/
    
    生成树思路:
    
    因为是后缀,所以前面的俩分别是其左右子树
    5
    52
    遇到+, 出俩, 分别作为+节点的右和左节点, 然后+入栈
    +
    +8
    +83
    遇到-, 出俩, 分别作为-节点的右和左节点, 然后-入栈
    +-
    遇到*, 出俩, 分别作为*的右和左节点, 然后*入栈
    *
    *4
    遇到/, 4是右子节点, *是左子节点
    
"""
print("===================")
def f2():

    s_back = '52+83-*4/'
    class BinTree:

        class Node:
            def __init__(self, e=None):
                self.e = e
                self.l = None
                self.r = None

        def __init__(self, s):

            self.head = None
            self.build(s)

        def build(self, s):

            stack = deque()
            for e in s:
                node = BinTree.Node(e)
                if e.isdigit():
                    stack.append(node)
                else:
                    r = stack.pop()
                    l = stack.pop()
                    node.l = l
                    node.r = r
                    stack.append(node)
            self.head = stack.pop()

        def search_first(self):

            def rf(node):
                print(node.e)
                if node.l:
                    rf(node.l)
                if node.r:
                    rf(node.r)

            rf(self.head)

        def search_middle(self):

            def rf(node):
                if node.l:
                    rf(node.l)
                print(node.e)
                if node.r:
                    rf(node.r)

            rf(self.head)

        def search_back(self):

            def rf(node):
                if node.l:
                    rf(node.l)
                if node.r:
                    rf(node.r)
                print(node.e)

            rf(self.head)

        # 中序回去, 但要加上括号
        # 最后会变成(((5+2)*(8-3))/4)
        def reverse(self):

            def rf(node):
                # 这里l, r一定是同时存在的

                if node.l:
                    return '('+rf(node.l)+node.e+rf(node.r)+')'
                else:
                    return node.e

            print(rf(self.head))

    bt = BinTree(s_back)

    bt.search_first()
    print("===================")
    bt.search_middle()
    print("===================")
    bt.search_back()
    print("===================")
    bt.reverse()

f2()




