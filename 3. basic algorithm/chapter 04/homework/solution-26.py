# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    汉诺塔
"""

def f1(n):

    def rf(k, f, b, t):
        """

        :param k: 几个盘子
        :param f: 从哪
        :param b: 经过哪
        :param t: 移动到哪
        :return:
        """
        if k == 1:
            print("{}->{}".format(f, t))
        else:
            rf(k-1, f, t, b)
            print("{}->{}".format(f, t))
            rf(k-1, b, f, t)

    rf(n, 'A', 'B', 'C')

f1(3)

# 思考, 既然所有递归都能转成非递归, 这里行不行
"""
    核心思路, 用栈模拟递归函数调用栈
    栈存的无非是子递归参数代表递归函数, 和当前递归函数的操作输出
    [(3, 'A', 'B', 'C')]
    [(2, 'A', 'C', 'B'), 'A->C', (2, 'B', 'A', 'C')]
"""
print("======")
from collections import deque
def f2(n):
    d = deque()
    d.append((n, 'A', 'B', 'C'))

    while d:
        e = d.pop()

        if isinstance(e, str):
            print(e)
        else:
            if e[0] == 1:
                print("{}->{}".format(e[1], e[3]))
            else:
                # 这里append的顺序要注意下, 栈是后进先出
                # 那么要先执行的子递归要后插入
                # solution-26的例子不用考虑因为二路递归是对称的
                # 这里参数不一样, 所以得考虑这个
                # 实在不好理解, 先按正序写, 再调换一下
                d.append((e[0] - 1, e[2], e[1], e[3]))
                d.append("{}->{}".format(e[1], e[3]))
                d.append((e[0] - 1, e[1], e[3], e[2]))

f2(3)
