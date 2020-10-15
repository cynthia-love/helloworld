# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    消除尾递归
    (这里的消除并不是说尾递归不好, 而是编译器会对尾递归自动优化, 减少额外的递归函数活动记录开销)
    (尾递归是线性递归的一种, 所以也一定可以转化成非递归形式)
"""

"""
    递归相对于非递归的
    优势:
    递归使我们能够简洁地利用重复结构简化问题, 从而可以避开复杂的案例分析和嵌套循环
    劣势:
    解释器必须保持跟踪每个嵌套调用的函数的状态的活动记录, 从而带来额外的空间开销
    
    为了减少递归调用带来的劣势, 有两种选择:
    1. 将递归转化为非递归形式, 以通过只存储最小限度的必要信息来减少内存使用
    2. 尽可能将递归处理成尾递归的形式, 对于这种形式的递归, 一般解释器会自动对代码进行优化,
    转换成常数级的空间占用
    
    尾递归, 一种特殊的线性递归
    当递归调用是整个函数体中最后执行的语句, 且它的返回值不属于表达式的一部分时, 就是尾递归,
    这个形式使得解释器可以不去保存当前递归函数的状态, 举个例子:
    
    def f(n):
        if n == 1: return 1
        return n*f(n-1)
    
    这里f(n)在调用f(n-1)的时候, 由于得到f(n-1)的时候, 还得进行乘积运算, 所以需要把相关信息存起来,
    比如f(5)的活动记录会是:
    [5*f(4)]
    [5*[4*f(3)]]
    [5*[4*[3*f(2)]]]
    [5*[4*[3*[2*f(1)]]]
    [5*[4*[3*[2*1]]]
    [5*[4*[3*2]]
    [5*[4*6]
    ...


    即得暂存f(5), f(4), f(3), f(2)的活动记录, 然后是f(1)有返回值后再逐级返回
    
    尾递归要实现什么, 下一级递归函数的返回值即是当前递归函数的返回值
    def f(n):
        if n == 1: return 1
        return f(n-1)
    然后调用f(5)的时候, 发现返回f(4), 没有任何其他上下文信息需要存储, 就不存f(5)的活动记录了
    然后调f(4)的时候发现返回f(3), f(4)的也不存了, 直到最后, 发现返回f(1), 直接返, 不用一级级
    返回
    
    或者换一种说法, 比如管理的两种形式:
    1. 别人找到项目组长问一个问题->项目组长找到开发->开发返回给项目组长->项目组长告诉别人
    转换成尾递归的方式就是把必要信息传给下一级, 自己不用老惦记这事了
    1. 别人找项目组长问一个问题->项目组长找到开发, 并把对方联系方式告诉开发->开发找到问题答案,直接
    回复给别人
    
    基于上述思路, 把前面的递归转换成尾递归, 即把必要的信息传给下一级递归函数
    def f(n):
        if n == 1: return 1
        return n*f(n-1)
        
    def f(last, n):
        if n == 1: return last*1
        return f(last*n, n-1)
        
    虽然多传了个函数参数, 但相比较存储整个函数的活动记录, 这种开销还是很小的
    
"""

"""
先以前n项和为例, 演示一下非递归, 线性递归, 线性尾递归
"""
s = [1, 2, 3, 4, 5]

# 非递归(这里的n表示索引)
def h1(n):
    res = 0
    for i in range(n):
        res += s[i]
    return res

# 线性递归
def h2(n):
    if n == 0: return s[n]
    return s[n]+h2(n-1)

# 线性尾递归
def h3(sum, n):
    if n < 0: return sum
    return h3(sum+s[n], n-1)
print(h3(0, 4))

"""
再以前面的斐波那契数列为例, 看一下其二路递归, 非递归, 线性递归, 尾递归几种实现方式
"""
# 二路递归, 最直观最好理解但开销最大
def f1(n):
    if n == 1: return 1
    if n == 2: return 2
    return f1(n-1)+f1(n-2)

# 非递归
def f2(n):
    if n == 1: return 1
    if n == 2: return 2
    a, b = 1, 2
    for i in range(n-2):
        a, b = b, a+b

    return b

# 利用增加返回值将二路递归转化成线性递归
# 不过这种形式的线性递归没法转成尾递归
def f3(n):
    if n == 1: return 1, 0
    if n == 2: return 2, 1

    a, b = f3(n-1)
    return a+b, a

# 线性尾递归
# 这里的n本质上是起到计数作用, 本质上还是从1, 2, 3, 5, 8这么开始数的而不是利用递推式往回找
def f4(a, b, n):
    if n == 1: return a
    return f4(b, a+b, n-1)
print(f4(1, 2, 5))

"""二分查找"""
# 递归
def f5(s, target, left, right):
    if left > right:
        return False

    mid = (left+right)//2
    if s[mid] == target:
        return True
    elif s[mid] > target:
        return f5(s, target, left, mid-1)
    else:
        return f5(s, target, mid+1, right)

# 非递归
def f6(s, target):
    left, right = 0, len(s)-1
    while left <= right:
        mid = (left+right)//2
        if s[mid] == target:
            return True
        elif s[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return False

"""序列逆置"""
# 递归形式
def f7(s, left, right):
    if left >= right: return
    s[left], s[right] = s[right], s[left]
    f7(s, left+1, right-1)

# 非递归形式
def f8(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

