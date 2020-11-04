# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    紧凑数组, array
    与引用数组list相对的称为紧凑数组, 即内存上直接存值
    而不是像引用数组那样, 每个位置存储64位地址, 然后这个地址再指向实际的值
    注意, 由于内存上直接存值, 后面元素的地址是算出来的, 所以要求每个元素类型、大小相同

    其实, list也可以理解为另外一种意义上的紧凑数组, 即关于内存地址的紧凑数组
    即其存储地址是用的array, 无非是地址指向的地方随机分布...
"""

"""
    比较array和list存储100个数的内存占用大小的区别
    
    如果一个数组元素类型固定, 即每个元素占用大小固定, 用array会有更优的存储空间和计算性能
"""
import sys
from array import array

vl = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sys.getsizeof(vl), sys.getsizeof(88))
# 208, 10个地址, 一个8字节, 10个80, 剩下128个字节应该是存储公共信息的
# 注意这里统计出的208, 不包括各个元素指针指向的实际对象的大小, 这里一个野生整形占28字节
# 总大小应该是: 128+8*10+28*10 = 488
va = array('l', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sys.getsizeof(va))
# 144, 10个数字, 每个占8字节, 一共80, 剩下64个字节应该是存储公共信息, 与元素个数无关
# !!!注意这里, 紧凑数组可以做到每个long int占8字节, 而像野生数字比如上面的88那样则一个占28字节
# 也就是说, 内存占用: 10个整形list > 10个独立整形变量 > 10个整形array

"""
    array模块
    array模块的第一个参数取值有:
    b   signed char
    B   unsigned char
    u   Unicode char
    h-i-l   signed short/normal/long int, 对应大写是unsigned的
    q-Q, 更长的整数, 比如64位系统那这个就保证是8字节
    f   单精度float
    d   双精度float
"""
va = array('b', [121, 122, 123, 124, 125])
# 公共信息64字节, 一个char占1字节, 所以总占用69字节
# 另外, char给的元素也是数字, 而不是单字符
print(sys.getsizeof(va))  # 69

"""
    演示ctypes
    ctypes可以理解成c和python之间的翻译器, 比如中文-英语-印度语
    所以ctypes可以用于c和python的混合编程
    一般步骤是: 
    写C->编译成动态链接库->在python里调用
    
    比如c函数要求参数类型char*, 则对应ctypes的c_char_p, 对应python的string
    再比如int, 对应ctypes的c_int, 对应python的int
"""
from ctypes import *
from platform import *

cdll_names = {
            'Darwin' : 'libc.dylib',
            'Linux'  : 'libc.so.6',
            'Windows': 'msvcrt.dll'
        }

clib = cdll.LoadLibrary(cdll_names[system()])

s1 = c_char_p('hello'.encode('utf-8'))
s2 = c_char_p('world'.encode('utf-8'))
print(s1.value)
clib.strcat.restype = c_char_p
# 上面那句话指定返回类型, 下面才能获取到python类型的返回值
# 注意, 直接返回python类型, 不用再用.value获取
s3 = clib.strcat(s1, s2)
print(s3.decode('utf-8'))

# 上面那几行可以简写
clib.strcat.restype = c_char_p
res = clib.strcat(c_char_p('hello'.encode('utf-8')), c_char_p('world'.encode('utf-8')))
print(res.decode('utf-8'))