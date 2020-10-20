# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计一个递归, 不能使用任何循环, 查找一个序列中的最小值和最大值
"""
from helloutils.tracker import Track
s = [1, 2, 3, -1, 800, 2000, -8]

# 逻辑上最好理解的
@Track
def f(s, k):
    if k == len(s)-1:
        return s[k], s[k]

    return max(s[k], f(s, k+1)[0]), min(s[k], f(s, k+1)[1])

# print(f(s, 0))

# 第一步优化, 二路递归转线性递归
@Track
def f2(s, k):
    if k == len(s)-1:
        return s[k], s[k]
    res = f2(s, k+1)
    return max(s[k], res[0]), min(s[k], res[1])
# print(f2(s, 0))

# 进一步优化, 尾递归, 把必要的参数传给子递归
@Track
def f3(s, k, vmax, vmin):
    if k > len(s)-1:  # 比较这里和f2的这里, f2要找到最后一个元素, 而这里要输出, 所以要越界之后输出
        # 当然, 用=也行, 得先求max和min, 再判断相等则return vmax, vmin
        return vmax, vmin
    return f3(s, k+1, max(vmax, s[k]), min(vmin, s[k]))
print(f3(s, 0, s[0], s[0]))

