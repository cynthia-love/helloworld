# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    python自带的双端队列deque

    与solution-10中自己设计的最大的功能上的区别是
    deque允许通过索引访问/修改队列中的元素

    另外, deque允许指定队列大小, 指定大小后, 如果队列
    满了, 不自动扩展, 而是把另一端的元素挤出去
"""

from collections import deque

d = deque()

d.appendleft(1)
d.append(8)
print(d)
print(len(d))
print(d[0])
print(d[-1])
d.popleft()
print(d)
d.pop()
print(d)

d.append(10)
d.append(11)
d.append(12)
print(d[1])
d[2] = 100
print(d)
d.rotate(1)  # 1, 2, 3 -> 3, 1, 2, 记住这个方法
print(d)

print(d.count(10))
d.remove(11)
print(d)

d.clear()
print(d)

# 如果指定deque大小呢
dd = deque(maxlen=3)
dd.append(1)
dd.append(2)
dd.append(3)
print(dd)
dd.append(4)  # 1, 2, 3 -> 2, 3, 4
print(dd)

# 此外, deque还支持传入sequence初始化
ddd = deque(i for i in range(3))
print(ddd)  # deque([0, 1, 2])