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
    
    怎么记是下界还是上界, 用特例法
    比如4和5, 4第一次完事后最多是2, 5第一次完事后始终是2
    即4和5第一轮完了之后最坏时间复杂度是一样的, 说明是取下界
    即log(5), log(6), log(7)都取log(4)的
"""

# 再分析计算磁盘空间使用情况
import os
def ff(url):
    size = os.path.getsize(url)

    if os.path.isdir(url):
        for each in os.listdir(url):
            size += ff(os.path.join(url, each))

    print('{:<7}'.format(size), url)
    return size

"""
    这里的分析方法和二分不太一样, 二分是单行线, 递归函数调用次数比较容易估计
    而这里, 递归函数里有for循环
    
    换个思路, getsize终归只计算一次, 所以递归函数调用次数肯定是n-1, 所以是O(n)
    
    当然, 这里有个点比较绕, 即递归函数次数为O(n), 但单个递归函数是不是O(1)的?
    猛一看, 里面有for循环, 好像不是O(1)的, 但注意, 这里有一个分期偿还的概念
    计算递归函数的总调用次数已经分期偿还了这部分时间复杂度, 即如果计算了for循环,
    那么就不能直接加总递归函数调用次数, 如果直接加总了, 那么已经偿还了for循环的部分
    那么, 在分析单个递归函数的时候, for循环逻辑就不能计入时间复杂度计算, 即单个
    递归函数的时间复杂度仅为getsize()的时间复杂度, 即O(1)
"""