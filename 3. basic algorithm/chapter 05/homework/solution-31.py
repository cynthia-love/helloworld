# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    二维数组, nxn, 每个数+1
"""
k = 30
ll = [[0 for _ in range(k)] for _ in range(k)]

# 非递归
for e1 in ll:
    for i in range(len(e1)):
        e1[i] += 1

print(ll)

# 递归, 由下往上, 由右往左
def f(ll, n1, n2):

    if n1 < 0: return

    # 二维到最左边, 则一维上移一行
    if n2 < 0: f(ll, n1-1, len(ll[0])-1)

    # 否则, 二维左移一位
    else:
        ll[n1][n2] += 1
        f(ll, n1, n2-1)


f(ll, len(ll)-1, len(ll[0])-1)
print(ll)

# 递归, 由上往下, 由左往右
def f(ll, n1, n2):

    if n1 >= len(ll): return

    if n2 >= len(ll[0]): f(ll, n1+1, 0)

    else:
        ll[n1][n2] += 1
        f(ll, n1, n2+1)
f(ll, 0, 0)
print(ll)