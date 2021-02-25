# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    跳表SkipList
    作为一种平衡数据结构, 跳表的效率和红黑树和AVL树不相上下, 原理却简单很多
    虽然是链表, 但可以做到插入和删除都是O(logN), 广泛应用于各种缓存实现中

    简单来讲, 维护多层指针

    head---------->4---->None
    head---->2---->4---->None
    head->1->2->3->4->5->None
    (设置None可以统一逻辑, forward长度始终等于当前节点层级)

    理想情况下, 最下层1级跳, 再往上2级跳, 再往上4级跳
    但这么插入的时候会很复杂, 所以作为权衡, 是否往上扩展采用随机0.5概率的方式

    刚好1级概率: 0.5
    刚好2级概率: 0.5*(1-0.5) = 0.5^2
    刚好3级概率: 0.5*0.5*(1-0.5) = 0.5^3

    有1级概率: 1            n个元素1级个数期望: n
    有2级概率: 1*0.5        n个元素2级个数期望: n*0.5
    有3级概率: 1*0.5*0.5    n个元素3级个数期望: n*0.25

    另外, 注意跳表要求key值有序

    此外, 有上必有下, 比如节点A第3层有指针, 那么第2层也有

"""
from random import random

class SkipList:

    class Node:

        # 注意level默认为1而非0
        def __init__(self, key, value=None, level=1):

            self.key = key

            self.value = value

            # 每层尾结点指向None, 这么设计可以使得forward长度
            # 始终等于当前节点层级
            self.forward = [None]*level

        @property
        def level(self):
            return len(self.forward)

    def __init__(self, p:float = 0.5, max_level: int = 16):

        self.head = self.Node('H')
        self.p = p
        self.max_level = max_level

    @property
    def level(self):
        return self.head.level

    def __iter__(self):
        cursor = self.head

        while cursor.forward[0]:

            cursor = cursor.forward[0]
            yield cursor.key, cursor.value, cursor.level

    def __str__(self):

        keys = ['H']+[e[0] for e in list(self)]+['N']

        res = [['-' for _ in range(len(keys))] for _ in range(self.level)]

        for i in range(self.level):

            res[i][0], res[i][-1] = 'H', 'N'

            cursor = self.head

            while cursor.forward[i]:

                cursor = cursor.forward[i]

                res[i][keys.index(cursor.key)] = str(cursor.key)

        return '\n'.join(['-'.join(e) for e in res])

    def random_level(self) -> int:

        level = 1

        while random() < self.p and level < self.max_level:
            level += 1

        return level

    def _locate_node(self, key):

        pre_nodes = []

        cursor = self.head

        # 从上往下找, 有上必有下
        for i in reversed(range(self.level)):

            while cursor.forward[i] and cursor.forward[i].key < key:

                cursor = cursor.forward[i]

            pre_nodes.append(cursor)

        pre_nodes.reverse()

        # cursor最终找到第一层
        if cursor.forward[0] and cursor.forward[0].key == key:

            return cursor.forward[0], pre_nodes

        else:
            return None, pre_nodes

    def insert(self, key, value):

        node, pre_nodes = self._locate_node(key)

        if node:
            node.value = value

        else:

            level = self.random_level()

            # 节点高度大于当前跳表高度, 需要补充头结点
            # 最终头结点高度达到max_level后不再变化
            if level > self.level:

                # 注意这里两行不能倒, 因为后一句会影响self.level
                # 要么把self.level单独赋个临时变量
                pre_nodes += [self.head]*(level-self.level)
                self.head.forward += [None]*(level-self.level)

            # 否则, 可能小于, 那么需要截断忽略超出的部分
            else:

                pre_nodes = pre_nodes[:level]

            # 这里实例化节点的时候别忘了把level传进去
            new_node = self.Node(key, value, level)

            for i, pre_node in enumerate(pre_nodes):

                new_node.forward[i] = pre_node.forward[i]

                pre_node.forward[i] = new_node

    def delete(self, key):

        node, pre_nodes = self._locate_node(key)

        if not node: raise KeyError

        # 前置节点是所有层的, 需要截断到与当前节点层数相同
        pre_nodes = pre_nodes[:node.level]

        for i, pre_node in enumerate(pre_nodes):
            pre_node.forward[i] = node.forward[i]

    def find(self, key):
        node, pre_nodes = self._locate_node(key)
        if not node: return False
        return node.key, node.value

sl = SkipList()

for i in range(5):
    sl.insert(i, 'value')
    print('=====')
    print(list(sl))
    print(sl)

sl.delete(3)
print('=====')
print(list(sl))
print(sl)

print(sl.find(2))
print(sl.find(3))



