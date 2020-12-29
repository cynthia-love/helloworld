# -*- coding: utf-8 -*-
# Author: Cythia

"""
    实现一个完整的collection.deque
"""

class EmptyError(Exception):
    pass

class Deque:
    CAPACITY = 5

    def __init__(self, c=None):

        self._data = [None]*c if c else [None]*Deque.CAPACITY

        self._fixed = True if c else False

        self._head = 0

        self._count = 0

    def __len__(self):
        return self._count

    def empty(self):
        return self._count == 0

    def resize(self, c):
        data2 = [None]*c
        head2 = 0

        for i in range(self._count):

            data2[(head2+1+i) % c] = self._data[(self._head+1+i) % len(self._data)]

        self._data = data2
        self._head = head2

    # 如果限制大小, 且满了, 右边挤出去一个
    def append_left(self, e):

        if not self._fixed:

            if self._count == len(self._data):
                self.resize(2*len(self._data))

            self._data[self._head] = e
            self._head = (self._head-1) % len(self._data)
            self._count += 1

        else:
            # 固定大小的情况, 满与不满都是给head位置赋值
            # 无非是满的时候把尾部覆盖, 其实就相当于挤出去了
            self._data[self._head] = e
            self._head = (self._head-1) % len(self._data)

            # 如果限制大小, 没满时插入元素数量才+1
            if self._count != len(self._data):
                self._count += 1

    def pop_left(self):
        if self.empty():
            raise EmptyError

        res = self._data[(self._head+1) % len(self._data)]
        self._data[(self._head+1) % len(self._data)] = None

        self._head = (self._head+1) % len(self._data)

        self._count -= 1

        return res

    # 如果限制大小了, 且满了, 左边挤出去一个
    def append_right(self, e):
        if not self._fixed:

            if self._count == len(self._data):
                self.resize(2*len(self._data))

            self._data[(self._head+1+self._count) % len(self._data)] = e

            self._count += 1

        else:
            # 注意, 左边挤出去不同于右边挤出去, 头指针位置会变
            if self._count != len(self._data):
                self._data[(self._head + 1 + self._count) % len(self._data)] = e
                self._count += 1
            else:
                # 满了, 可以这么算, 也可以直接赋值头指针的+1位置
                self._data[(self._head + 1 + self._count) % len(self._data)] = e
                self._head = (self._head+1) % len(self._data)

    def pop_right(self):
        if self.empty():
            raise EmptyError

        res = self._data[(self._head+self._count) % len(self._data)]
        self._data[(self._head + self._count) % len(self._data)] = None

        self._count -= 1

        return res

    def __getitem__(self, pos):
        if self.empty():
            raise EmptyError

        # 先校验索引及转换负索引
        # 如果有x个元素, 则合理范围: 0~x-1和-1~-x
        pos = pos if pos >= 0 else self._count+pos
        if not 0 <= pos <= self._count-1:
            raise IndexError

        return self._data[(self._head+1+pos) % len(self._data)]

    # 注意, setitem不是按总空间大小算的, 是按队列元素个数算的
    def __setitem__(self, pos, value):

        if self.empty():
            raise EmptyError
        pos = pos if pos >= 0 else self._count+pos

        if not 0 <= pos <= self._count-1:
            raise IndexError

        self._data[(self._head+1+pos) % len(self._data)] = value

    def clear(self):
        for i in range(self._count):
            self._data[(self._head+1+i) % len(self._data)] = None

        self._count = 0

    # 循环右移k步
    def rotate(self, k):
        if self.empty():
            raise EmptyError

        # 关键是, 把头指针右移k位, 出队的元素赋给队尾
        # 要考虑一种特殊情况, 队列满
        for i in range(k):
            l = (self._head+1+i) % len(self._data)  # 头部待移出元素
            r = (self._head+1+self._count+i) % len(self._data)  # 尾部待拼接元素

            if l == r: break  # 相等其实就是队列满的情况, 首尾相连了
            else:
                self._data[r] = self._data[l]
                self._data[l] = None

        self._head = (self._head+k) % len(self._data)

    # 移除第一个匹配的e
    def remove(self, e):

        for i in range(self._count):
            if self._data[(self._head+1+i) % len(self._data)] == e:
                for j in range(i, self._count-1):
                    self._data[(self._head + 1 + j) % len(self._data)] = \
                        self._data[(self._head + 1 + j+1) % len(self._data)]
                else:
                    # 移动完毕, 最后一个位置赋值None, 并元素数量-1
                    self._data[(self._head + self._count) % len(self._data)] = None

                    self._count -= 1

                    # 只删除一个, 别忘了外层循环退出
                    break

    def count(self, e):
        res = 0
        for i in range(self._count):
            if self._data[(self._head+1+i) % len(self._data)] == e:
                res += 1

        return res

    def show(self):
        print(self._data, self._head, self._count)

d1 = Deque()
d2 = Deque(5)
d1.show(); d2.show()
d1.append_left(1); d2.append_left(1)
d1.show(); d2.show()
d1.append_right(2); d2.append_right(2)
d1.show(); d2.show()
d1.append_left(1); d2.append_left(1)
d1.append_left(1); d2.append_left(1)
d1.append_left(1); d2.append_left(1)
d1.show(); d2.show()
print(d1.pop_left()); print(d2.pop_left())
d1.show(); d2.show()
print(d1.pop_right()); print(d2.pop_right())
d1.show(); d2.show()
d1.append_right(3); d2.append_right(3)
d1.show(); d2.show()
d1.append_right(3); d2.append_right(3)
d1.show(); d2.show()
d1.append_left(1); d2.append_left(1)
d1.show(); d2.show()
print(len(d1), len(d2))
print(d1[0], d2[0])
print(d1[-1], d2[-1])
print(d1[4], d2[4])
d1[4] = 8; d2[4] = 8
d1.show(); d2.show()

# d1.clear(); d1.show()
d1.rotate(1); d1.show()
d2.rotate(1); d2.show()

print(d1.count(1), d2.count(1))
d1.pop_right(); d2.pop_right()
d1.show(); d2.show()
d1.remove(1); d1.show()
d2.remove(1); d2.show()




