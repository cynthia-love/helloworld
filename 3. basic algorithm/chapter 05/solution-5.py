# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    自己实现动态数组
    一般每次扩展为原大小的两倍

    这里要再次强调一下list和array的区别
    注意, array模块里的array, 应该理解成array类, 而不是数组结构, 其也对底层紧凑数组做了封装
    也就是说, 代码里的list和array都是对紧凑数组的封装, 都支持了动态性

    无非list类比array类多做了一步, 存值的时候转地址和取值的时候地址转对象

    另外, n*ctypes.py_object 语法得到的是<class '__main__.py_object_Array_n'> 类
    这种类其实是一种list, 限定了数组元素为py_object指针, 存值取值的时候会自动进行地址-对象转换
"""
import copy
import ctypes
from array import array
"""
    演示1, 动态紧凑数组, 即存值取值不转换; 要求数组元素类型一致
"""
class MArray:
    def __init__(self):
        self.cur_size = 0
        self.max_size = 1

        # 这里用L-long和Q-long long都能获得8字节元素, 保险点用Q吧
        self.base_array = array('Q')  # array没法初始化空间大小

    def append(self, o):
        if self.cur_size == self.max_size:
            self.resize()
        # 真正的动态数组这里有空地, 是直接赋值的, 而不是append
        self.base_array.append(o)
        self.cur_size += 1

    def resize(self):
        self.max_size = self.max_size*2
        # 按真正模拟的话, 这里应该是去分配一个新的两倍大小的数组
        # 然后把原数组复制到新数组的前半部分去
        self.base_array = copy.copy(self.base_array)

    def __len__(self):
        return self.cur_size

    def __getitem__(self, item):

        return self.base_array[item]

m = MArray()

for i in range(100):
    print("元素个数{}, 总空间{}".format(m.cur_size, m.max_size))
    m.append(i)

print(m[10])
print("=====")

"""
    演示2, 动态引用数组, 和引用数组的区别无非是存值取值的时候有地址-对象转换
    由于存储的是地址, 不限制对象类型
"""
class MArray2:
    def __init__(self):
        self.cur_size = 0
        self.max_size = 1

        self.base_array = array('Q')

    def __len__(self):
        return self.cur_size

    def append(self, o):
        if self.cur_size == self.max_size:
            self.resize()
        self.base_array.append(id(o))
        self.cur_size += 1

    def __getitem__(self, key):
        # 从地址中读取python对象要借助ctypes, 记住这句话!!!
        po = ctypes.cast(self.base_array[key], ctypes.py_object)
        return po.value

    def resize(self):
        self.max_size *= 2
        self.base_array = copy.copy(self.base_array)

m2 = MArray2()
for i in range(100):
    print("元素个数{}, 总空间{}".format(m2.cur_size, m2.max_size))
    m2.append("hello")

print(m2[0])
print("======")

"""
    演示3, 更贴合真正的写法
    演示1, 2里用的array类不是最底层的array数据结构, 其本身也是动态的, 无法自定义空间分配
    
    这里用<class '__main__.py_object_Array_n'>
    虽然也是有一层封装, 但好歹可以自定义分配底层占用的数组的大小
"""
# 第二种办法, 绕过已经动态化的数组array
# n*ctypes.py_object, 会得到一个元素为python对象的n长数组类, 可以实例化
class DArray:
    def __init__(self):
        self.max_size = 1  # 初始给个1吧, 总要往里存东西的
        self.cur_size = 0

        # self.max_size*ctypes.py_object得到<class '__main__.py_object_Array_n'>
        self.array = (self.max_size*ctypes.py_object)()

    def __len__(self):
        return self.cur_size

    def __getitem__(self, k):
        if not 0 <= k < self.cur_size:
            raise IndexError
        return self.array[k]

    def append(self, obj):
        if self.cur_size == self.max_size:
            self.resize()
        # 这里的写法才是真正的动态数组写法, 即对已分配空间直接赋值
        # 另外注意, 这里直接赋值obj, 而不是id(obj), 而又支持多数据类型
        # 说明<class '__main__.py_object_Array_n'>这一级给把地址-对象转换做了
        self.array[self.cur_size] = obj
        self.cur_size += 1

    def resize(self):
        self.max_size *= 2
        array_new = (self.max_size*ctypes.py_object)()
        for i in range(self.cur_size):
            array_new[i] = self.array[i]
        self.array = array_new

d = DArray()
for i in range(100):
    print("元素个数{}, 总空间{}".format(d.cur_size, d.max_size))
    d.append("hello")

print(d[0])

