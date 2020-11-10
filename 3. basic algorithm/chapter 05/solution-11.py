# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    使用list存储排行榜
"""

# 自定义排行榜单项的数据类型
class Element:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __ge__(self, other):
        return self._score >= other.get_score()

    def __lt__(self, other):
        return self._score < other.get_score()

    def __str__(self):
        return "({}, {})".format(self._name, self._score)

class ScoreBoard:

    def __init__(self, capacity):
        self._board = [None]*capacity
        self._n = 0

    def __getitem__(self, index):
        return self._board[index]

    def __setitem__(self, key, e):
        self._board[key] = e

    def __len__(self):
        return len(self._board)

    def __str__(self):
        # 这里注意, 要拼接有效元素, 而不是列表里的所有元素
        return '\n'.join(str(self._board[i]) for i in range(self._n))

    def add(self, e: Element):

        # 为了统一插入逻辑, 先把要插入的元素放在列表结尾
        # 特别地, 如果满了, 看最后一个元素是不是比它小, 小了替换, 大了什么都不做
        if self._n == len(self):
            if self[-1] < e:
                self[-1] = e
        else:
            # 没满, 放到结尾, 同时元素个数+1
            self[self._n] = e
            self._n += 1

        # 4, 3, 2, 1, 2.5, 待调整位置元素已经到末尾了, 接下来, 往前冒泡:
        # 4, 3, 2, 2.5, 1
        # 4, 3, 2.5, 2, 1, 冒不动了, 直接break
        for i in range(self._n-1, 0, -1):
            if self[i] > self[i-1]:
                self[i], self[i-1] = self[i-1], self[i]
            else:
                break

    def add2(self, e: Element):
        # 第二种插入逻辑, 给待插入元素空出位置再插
        # 特殊情况特殊处理, 满了, 且最后一个元素大于待插入元素
        if self._n == len(self) and self[-1] >= e: return

        # 否则, 1. 满了, 最后一个小于待插入; 2. 没满, n+1
        self._n = self._n if self._n == len(self) else self._n+1

        # 理解这里pos为什么这么取, 情况1, 已经确定最后一个小于, 没必要判断, 直接判断倒数第二个
        # 情况2, 虽然是原倒数第一个元素, 但右边多了个空位
        pos = self._n-1-1

        while pos >= 0:
            if self[pos] < e:
                self[pos + 1] = self[pos]
                pos -= 1
            else:
                break
        # 因为有-1情况的存在, 这里赋值不能放在循环里面
        self[pos + 1] = e

sb = ScoreBoard(5)
sb.add2(Element('aa', 100))
sb.add2(Element('bb', 200))
sb.add2(Element('cc', 88))
sb.add2(Element('dd', 300))
sb.add2(Element('ee', 33))
sb.add2(Element('ff', 1))
sb.add2(Element('gg', 3000))
print(sb)