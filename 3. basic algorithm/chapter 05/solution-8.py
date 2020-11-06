# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    python序列类型的效率-list和tuple
    tuple不用单独考虑, 其可以理解为不支持修改的list
    当然, 由于不支持修改, 其不用创建多余空间, 从而内存利用率更高
"""

l1 = [1, 2, 3, 4, 5]

"""
    不修改列表的操作
"""

print(len(l1))  # O(1), 注意底层数组空间是大于实际元素个数的, 所以list单独存储了当前元素个数, 直接取
print(l1[3])  # O(1), l1指向第一个元素, 通过第一个元素的地址值直接计算第4个元素的地址值, 再去对应地址取值

print(l1.count(3))  # 得全部遍历一遍才能数出来有几个目标值, 全遍历, 所以O(n)
print(l1.index(5))  # 最差情况要遍历到最后一个位置, 所以也是O(n)
print(5 in l1)  # 同样, 最差情况要遍历到最后一个位置, 所以也是O(n)

print([1, 2, 3, 4, 5] < [3])  # 注意数组比较是按字典顺序比较; 如果可比较部分都一样, 才比较长度, 显然, 时间复杂度依赖短的那个O(n短)

print(l1[1:3])  # 创建新的实例, 依赖于要赋多少值, 即要创建的新实例的长度O(n新)

print(l1+l1)  # 创建新的实例, 同样依赖要赋多少值, 即要创建的新实例的长度O(n1+n2)

print(l1*3)  # 创建新的实例, 同样依赖要赋多少值, 即要创建的新实例的长度O(c*n)


l2 = [1, 2, 3, 4, 5]

"""
    修改列表的操作
"""

l2[1] = 8  # 赋值, 直接将第2个元素位置的地址指针值改了, O(1)
l2.append(88)  # 大小扩展操作耗时向后摊销, 得到平均append O(1)


# insert, 头部插入, 中间插入, 尾部插入不一样
# 头部O(n), 中间O(n/2), 尾部O(1), 可以写成O(n-k+1), 或者直接按概率求平均
# 比如数组 1, 2, 3, 4, ...n, 可插入位置n+1, 每个位置概率1/(n+1)
# 平均耗时: (1+2+...+n+1)/(n+1) = O(n)
import time
t1 = time.time()
for i in range(10000):
    l2.append(i)
t2 = time.time()
print("append平均耗时{}".format(t2-t1))

t1 = time.time()
for i in range(10000):
    l2.insert(0, i)
t2 = time.time()
print("insert-开始 平均耗时{}".format(t2-t1))

t1 = time.time()
for i in range(10000):
    l2.insert(len(l2)//2, i)
t2 = time.time()
print("insert-middle 平均耗时{}".format(t2-t1))

t1 = time.time()
for i in range(10000):
    l2.insert(len(l2), i)
    # 注意插入到末尾不要用-1, 插入的意思是往指定索引位置查, 其他值后移
    # -1的意思是插入最后一个位置, 最后一个位置往后移, 而不是插入到最后
t2 = time.time()
print("insert-末尾 平均耗时{}".format(t2-t1))

l3 = [1, 2, 3, 4, 5, 6, 7, 8]
l3.pop()  # 无参数, pop最后一个, 不用移动元素, 理论上是O(1), 不过有时候会触发数组自动缩小, 暂不考虑
l3.pop(0)  # pop第一个, 所有元素都要左移, O(n)
l3.pop(3)  # pop中间的, 比如第k个, 那右边的左移, O(n-k)
del l3[3]  # 等价于l3.pop(3), O(n-k)

l3.remove(2)  # 从左遍历找到对应值, 然后右边的左移, 比较和移动加起来, 使得总时间复杂度恒O(n)

for i in range(3):
    l3.append(i)
l3.extend([0, 1, 2])
# extend等价于多次append, 即时间复杂度为O(n2)
# 但注意, 其还是比多次append优的, 一是执行一个函数肯定是比执行多个优的, 二是extend可以提前知道n2
# 而append一个一个往里插入可能会导致多次空间动态扩展

l4 = l3+[1, 2, 3]  # 创建一个新数组, 大小为n1+n2, 然后复制所有, O(n1+n2)

l3.reverse()  # 双指针, O(n)

l3.sort()  # 依赖于所用的算法, 最优O(n*log(n))

"""
    构造新列表的几种方法
"""
t1 = time.time()
l = []
for i in range(100000):
    l.append(1)
t2 = time.time()
print("append, {}".format(t2-t1))  # 一个个元素插入, 最慢, 不停地扩展空间, 30t左右

t1 = time.time()
ll = [0]*100000
t2 = time.time()
print("*, {}".format(t2-t1))  # list*c语法, 最快, 因为可以先行确定总空间大小, 设为t

t1 = time.time()
lll = [0 for _ in range(100000)]
t2 = time.time()
print("列表推导式, {}".format(t2-t1))  # 列表推导式, 中间, 10t左右

# 列表推导式比循环append快哪了呢, 函数的载入
# 列表推导式有对应的底层汇编命令LIST_APPEND
# 而append没有, 每次都需要加载append方法
import dis
def f():
    l = [i for _ in range(10)]

dis.dis(f)

"""
    在自定义动态数组的基础上, 增加insert和remove的实现
"""
import ctypes

class DArray:
    def __init__(self):
        self.cur_size = 0
        self.max_size = 1
        self.array = self.make_array(self.max_size)

    def make_array(self, n):
        return (n*ctypes.py_object)()

    def __len__(self):
        return self.cur_size

    def __getitem__(self, index):
        if not 0 <= index <= self.cur_size-1:
            raise IndexError
        return self.array[index]

    def append(self, obj):
        if self.cur_size == self.max_size:
            self.resize()
        self.array[self.cur_size] = obj
        self.cur_size += 1

    def resize(self):
        t = self.make_array(self.max_size*2)

        for i in range(self.cur_size):
            t[i] = self.array[i]

        self.array = t
        self.max_size *= 2

    def insert(self, index, obj):

        if not 0 <= index <= self.cur_size:
            raise IndexError

        if self.cur_size == self.max_size:
            self.resize()
        for i in range(self.cur_size, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = obj
        self.cur_size += 1

    def remove(self, obj):

        for i in range(self.cur_size):
            if self.array[i] == obj:
                for j in range(i, self.cur_size-1):
                    self.array[j] = self.array[j+1]
                self.cur_size -= 1
                break

da = DArray()

for i in range(10):
    print(da.cur_size, da.max_size)
    da.append(i)

for i in range(da.cur_size):
    print(da[i], end=" ")
print()

da.insert(da.cur_size, 88)
for i in range(da.cur_size):
    print(da[i], end=" ")
print()

da.insert(3, 888)
for i in range(da.cur_size):
    print(da[i], end=" ")
print()

da.remove(1000)
for i in range(da.cur_size):
    print(da[i], end=" ")
print()

da.remove(3)
for i in range(da.cur_size):
    print(da[i], end=" ")
print()