# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    分析递归算法
"""
def f1(n):
    if n == 0: return 1
    return n*f1(n-1)

"""
    如果能直接根据数学形式推出来递归函数调用次数,再乘以每次调用的原子操作次数, 即得到递归总调用次数
    比如这里, n调一次,n-1, n-2, 直到0, 可以知道函数调n+1次, 每次操作次数1, 所以总时间复杂度O(n)
    
    除了这个, 还有一个办法, 单独搞一个函数去统计次数, 找规律
"""
class Count:
    def __init__(self, func):
        self.c = 0
        self.f = func

    def __call__(self, *args, **kwargs):
        self.c += 1
        res = self.f(*args, **kwargs)
        return res

    def get_count(self):
        return self.c

    def reset_count(self):
        self.c = 0
@Count
def f2(n):
    if n == 0: return 1
    return n*f2(n-1)

# f2变成Count(f2)
f2.reset_count()
f2(100)
print(f2.get_count())

f2.reset_count()
f2(10)
print(f2.get_count())

f2.reset_count()
f2(88)
print(f2.get_count())


# 分析完阶乘, 再分析标尺绘制
# 其实就是统计draw_line的调用次数
@Count
def draw_line(length, label=''):
    s = '-'*length+' '+label
    print(s)

def draw_interval(length):
    if length == 0: return
    draw_interval(length-1)
    draw_line(length)
    draw_interval(length-1)

num_inches, max_length = 1, 9  # 英尺数是常量乘以, 所以分析时间复杂度把这个值设置为1就好
for i in range(num_inches):
    draw_line(max_length, str(i))
    draw_interval(max_length-1)

draw_line(max_length, str(num_inches))

print(draw_line.get_count())
"""
    4   9
    5   17
    6   33
    7   65
    8   129
    9   257
    看着像是指数. 递归主体是draw_interval, 分析它就行
    假设draw_interval(c)调2^c-1次draw_line
    1. c=0成立
    2. 假设c=k时成立, 那么当c=k+1时, 次数等于:
    2^k-1+1+2^k-1 = 2^(k+1)-1, 所以成立
    即draw_interval(c) = draw_interval(c-1)+1+draw_interval(c-1)
                       = 2^k-1 = O(2^n)
"""

# 再分析二分查找
def f():
    s = [1, 2, 3, 4, 5, 8, 10, 11, 20, 80, 100, 110, 120]

    def rf(l, r):
        if l > r: return -1
        m = (l+r)//2
        if s[m] == 20:
            return m
        elif s[m] > 20:
            return rf(l, m-1)
        else:
            return rf(m+1, r)

    return rf(0, len(s)-1)

"""
    初始n
    进行一次调用后至多 n/2
    进行两次    至多 n/4
    k次  n/2^k < 1
         k > log(n)
         k = log(n)的下界+1
         所以二分查找时间复杂度: O(log(n))
         
    补充: 比如10, 初始长度10, 最后一次列表长度<1
    
    2       2
    4       3
    6       3
    8       4
    9       4
    10      4
    log(n)取下界+1
    
    
"""