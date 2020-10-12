# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    递归例子-线性递归

    先明确几个概念:
    线性递归: 一个递归函数最多调用其他一个递归函数(减治?, 注意二分查找是线性递归)
    二路递归: 一个递归函数最多调用其他两个递归函数
    多重递归: 一个递归函数可以调用多个其他递归函数
"""

# 例子1, 计算list前n个值的和
"""
    能不能用递归, 看能不能找到递推式和边界条件
    当然递推式不一定是数学形式, 也可能是逻辑上的, 比如二分查找, 归并排序等
    
    这里:
    res(n) = s[n]+res(n-1), 递推式
    res(0) = s[0], 边界条件
"""
s = [1, 2, 3, 8, 100, -199]

def f1(k):
    if k == 0: return s[0]
    else: return s[k]+f1(k-1)
print(f1(2))

# 例子2, 将序列逆序
"""
    逆序, 最直观的想法是循环到中间位置, 对称交换
    另外, 设定一个k值还需要在函数体里再计算对称位置, 还不如设定俩
    
    递归函数调用次数, n为奇数时, n//2+1, n为偶数时, n/2+1 = n//2+1
    而每次递归函数是O(1)的, 所以总的时间复杂度是O(n)的
"""
s2 = [1, 2, 3, 8, 100, -199]

def f2(left, right):
    if left >= right: return
    s2[left], s2[right] = s2[right], s2[left]
    f2(left+1, right-1)

f2(0, len(s2)-1)
print(s2)

# 例子3, 计算x的n次幂, x取2吧
"""
    思路1:
    f(n) = f(n-1)*x
    f(0) = 1
    显然, 是O(n)的
    
    思路2:
    f(n) = f(n//2)*f(n-n//2)
    f(0) = 1
    
    2-3
    3-5
    4-7
    100-199, 看这意思, 还是O(n)的???
    怎么由递归的递推式得到递归次数的递推式???
    t(n) = t(n//2)+t(n-n//2)+1
    简化: = 2*t(n/2)+1, t(1) = 1
    t(2) = 3
    t(4) = 7
    t(8) = 15
    t(16) = 31, 差不多是2n+1, 即O(n)
    
"""

def f3(n):
    if n == 0: return 1
    return 2*f3(n-1)
print(f3(8))

count = 0
def f4(n):
    global count
    count += 1
    if n == 0: return 1
    if n == 1: return 2
    return f4(n//2)*f4(n-n//2)
print(f4(128))
print(count)

"""
    思考一下算法4为什么用了二路递归, 但是还是O(n)
    xxxxxx...xxxxxx, 因为该乘的一点没少f(4)*f(5)重复部分并没有优化, 本质上还是每个x乘了一次
    优化思路是f(4)*f(4)*1这样, 就变成线性递归了
    t(n) = t(n/2)+1
    1+1+1...+1, 加了log(n)个1
    即时间复杂度变成了O(log(n))
    (或者这么考虑, f(8)一共经历了: f(8), f(4), f(2), f(1)
    f(16)一共经历了: f(16), f(8), f(4), f(2), f(1)...)
"""
count5 = 0
def f5(n):
    global count5
    count5 += 1
    if n == 0: return 1
    if n == 1: return 2
    if n % 2 == 0: return f5(n/2)**2
    else: return 2*f5(n//2)**2

print(f5(128))
print(count5)

"""
    f5的优化方式最好, 当然, 还有一种优化方法, 存储中间值, 看看效果怎样
    如果不算 if n in d: return d[n]的开销的话, 其实也基本能算是O(log(n))

"""
count6 = 0
d = {}
def f6(n):
    if n in d: return d[n]
    if n == 0: res = 1
    elif n == 1: res = 2
    else:
        global count6
        count6 += 1
        res = f6(n//2)*f6(n-n//2)
    d[n] = res
    return res

print(f6(1000))
print(count6)

