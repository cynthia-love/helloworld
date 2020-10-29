# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    自己实现一个walk函数
    知识点: yield from
"""

import os

for root, dirs, files in os.walk("../.."):
    print(root)

"""
    分析, 以root作为基准深度优先遍历
    每次输出当前目录下的子目录和文件, 但不作为递归基准
"""
print("===")
def f1(path):

    c = os.listdir(path)
    d = [e for e in c if os.path.isdir(os.path.join(path, e))]
    f = [e for e in c if os.path.isfile(os.path.join(path, e))]
    yield (path, d, f)

    for e in d:
        # 这里用到一个语法, yield from
        # 这里不能直接f1(os.path.join(path, e))
        # 而要显示地把子函数的yield拼接到父级的yield里, 有点像extend
        yield from f1(os.path.join(path, e))

for root, dirs, files in f1("../.."):
    print(root)

# 探究yield from
"""

    yield 返回一个值
    yield from, 从可迭代对象里返回
"""

# 例子1, 基本演示
def f11():
    yield 1
    yield from [2, 3, 4]

    # yield from 相当于这个for循环
    for e in [5, 6, 7]:
        yield e

print(list(f11()))  # 1, 2, 3, 4

# 例子2, 递归里的yield from
def f22(k):
    if k == 0: yield 0

    yield f22(k-1)

for e in f22(3): print(e)
# <generator object f22 at 0x109d5c6d0>
# 而不是我们想象中的3, 2, 1, 0
"""
    这里的知识点在于, 只要函数里有yield, 那么解释器就把其作为一个generator
    所以yield f22(k-1)返回的是个generator, 相当于多了一级
    本来函数底下yield 1, yield 2, 整个函数作为一级generator
    现在yield generator1, yield generator 2, yield出来的元素还是个generator, 就乱了
    
    这里要用yield from, 表示父函数的yield值依赖于子generator
    相当于:
    for e in f22(k-1):
        yield e
"""

def f23(k):
    yield k
    if k > 0:
        for e in f23(k-1):
            yield e

print(list(f23(3)))

# 用yield from时, f24和f25两种写法都行
def f24(k):
    yield k
    if k > 0:
        yield from f24(k-1)
print(list(f24(3)))

def f25(k):
    if k == 0: yield 0
    else:
        yield k
        yield from f25(k-1)
print(list(f25(3)))

# yield from有什么妙用呢???
# 在递归里拿到所有返回值而不用额外设置数组存
# 比如输出k-0的几种写法

# 方法1, 非递归
def f41(k):
    while k >= 0:
        yield k
        k -= 1
for each in f41(3): print(each, end="")

# 方法2, 递归, 额外存数组
def f42(res, k):
    if k < 0: return res
    else:
        res.append(k)
        return f42(res, k-1)
for each in f42([], 3): print(each, end="")

# 方法3, 递归, 不作为参数, 而是在返回值上做文章
def f43(k):
    if k < 0: return []
    else:
        return [k]+f43(k-1)
for each in f43(3): print(each, end="")

# 方法4, 全局变量存
res = []
def f44(k):
    if k < 0: return
    else:
        res.append(k)
        f44(k-1)
f44(3)
for each in res: print(each, end="")

# 方法5, yield from, 最为推荐
def f45(k):
    yield k
    if k > 0:
        yield from f45(k-1)
for each in f45(3): print(each, end="")