# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    利用PositionList实现收藏夹
    每次访问后按访问次数由低到高排序

    支持access, remove和top-k

    access需要定位元素, 有计数+1并且前移, 没有计数1放到末尾
    remove需要定位元素, 删除

"""

class DoubleLinkedList:

    class _Node:

        __slots__ = '_e', '_prev', '_next'

        def __init__(self, e=None):
            self._e = e
            self._prev = None

            self._next = None

    def __init__(self):
        self._head = self._Node()
        self._tail = self._Node()

        self._head._next = self._tail
        self._tail._prev = self._head

        self._c = 0

    def __len__(self):
        return self._c

    def empty(self):
        return self._c == 0

    def _insert_between(self, left, right, e):

        node = self._Node(e)

        node._prev, node._next = left, right
        left._next, right._prev = node, node

        self._c += 1

        return node

    def _delete_node(self, node):
        node._prev._next = node._next

        node._next._prev = node._prev

        node._prev = node._next = None

        self._c -= 1

        return node._e

class PositionLinkedList(DoubleLinkedList):

    # 对外不暴露node, 而是附加一张身份证给出去
    # 回来的时候看身份证, 过了才认为是原结点
    class _Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        @property
        def element(self):
            return self._node._e

        @element.setter
        def element(self, e):
            self._node._e = e

        def __eq__(self, other):
            if type(other) is not type(self):
                return False
            if other._container is not self._container:
                return False
            if other._node is not self._node:
                return False

            return True

    def _validate(self, p):
        if not isinstance(p, self._Position):
            return False

        if p._container is not self:
            return False

        return True

    def _n2p(self, node):

        if node in [self._head, self._tail]:
            return None

        return self._Position(self, node)

    # ------------------accessor---------------------

    def first(self):
        return self._n2p(self._head._next)

    def last(self):
        return self._n2p(self._tail._prev)

    def before(self, p):
        if not self._validate(p):
            raise TypeError

        return self._n2p(p._node._prev)

    def after(self, p):
        if not self._validate(p):
            raise TypeError

        return self._n2p(p._node._next)

    def __iter__(self):
        cursor = self.first()

        while cursor:

            yield cursor.element

            cursor = self.after(cursor)

    # --------------------mutator---------------------

    def add_first(self, e):

        return self._n2p(self._insert_between(self._head, self._head._next, e))

    def add_last(self, e):

        return self._n2p(self._insert_between(self._tail._prev, self._tail, e))

    def add_before(self, p, e):
        if not self._validate(p):
            raise TypeError

        return self._n2p(self._insert_between(p._node._prev, p._node, e))

    def add_after(self, p, e):

        if not self._validate(p):
            raise TypeError

        return self._n2p(self._insert_between(p._node, p._node._next, e))

    def delete(self, p):

        if not self._validate(p):
            raise TypeError

        r = self._delete_node(p._node)

        p._container = p._node = None

        return r

class FavoritesList:

    # FavoritesList并不是子类, 而是使用PositionLinkedList
    # 无非是原结点里的e变成一个自定义复杂元素类型Item
    class _Item:

        __slots__ = '_value', '_count'

        def __init__(self, value):
            self._value = value

            self._count = 1

        @property
        def value(self):
            return self._value

        @property
        def count(self):
            return self._count

    def __init__(self):

        self._data = PositionLinkedList()

    def __len__(self):
        return len(self._data)

    def empty(self):
        return self._data.empty()

    def __iter__(self):
        # PositionLinkedList的iter返回的事每个结点的e
        # 而e是自定义数据类型, 这里进一步把e拆成网址和访问次数

        for each in self._data:
            yield (each._value, each._count)

    def _find(self, value):

        # 找到目标元素所在的position
        cursor = self._data.first()

        while cursor:

            if cursor.element._value == value:
                return cursor

            cursor = self._data.after(cursor)

        return None

    def _move(self, p):

        q = self._data.before(p)

        while q and q.element._count <= p.element._count:

            q = self._data.before(q)

        # 退出条件有俩, 一是q为空
        if not q:
            self._data.add_first(self._data.delete(p))

        # 另一个是q位置值访问次数大于p
        else:
            self._data.add_after(q, self._data.delete(p))

    def access(self, v):
        p = self._find(v)

        if p:
            p.element._count += 1

        else:

            p = self._data.add_last(self._Item(v))

        self._move(p)

    def remove(self, v):
        p = self._find(v)

        if p:
            self._data.delete(p)

    def top(self, k):

        if not 1 <= k <= len(self):
            raise IndexError

        cursor = self._data.first()

        for i in range(k):

            yield cursor.element._value

            cursor = self._data.after(cursor)

pl = PositionLinkedList()
p1 = pl.add_first(1)
p2 = pl.add_first(-1)
p3 = pl.add_last(100)
p4 = pl.add_last(1000)
p5 = pl.add_after(p3, 800)
pl.add_after(p5, 900)
print(list(pl))

fl = FavoritesList()
fl.access('a')
fl.access('a')
fl.access('b')
fl.access('b')
fl.access('a')
fl.access('c')
fl.access('d')
fl.access('d')
fl.access('d')
print(list(fl))
print(list(fl.top(3)))

"""
    启发式权衡
    
    设想以下场景, 共n个元素
    元素1访问n次
    元素2访问n次
    ...
    元素n访问n次
    
    元素1的访问时间复杂度: 1*n = n
    元素2的访问时间复杂度: 2*n = 2n   (定位时从头找, 在第n次访问前其次数始终小于元素1)
    元素3的访问时间复杂度: 3n
    ...
    
    总: n+2n+3n+...+nn = O(n^3)
    
    所谓启发式方法, Move-to-Front, 认为如果一个元素被访问, 那么大概率在不久将来再次被访问
    即每次访问移动到最头部
    
    元素1访问n次: n
    元素2访问n次: n
    ...
    总: n+n+n... = O(n^2)
    
    访问是快了, 但是返回top-k就慢了
    
    原方法是O(k)
    
    启发式方法, 找最大的n, 次大的n, 总时间复杂度O(kn)
    
    如果先排序, O(nlogn+k)
    
    怎么样都不如O(k)的
    
"""

class FavoritestListMTF(FavoritesList):

    def _move(self, p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):

        if not 1 <= k <= len(self):
            raise IndexError

        t = PositionLinkedList()

        for item in self._data:
            t.add_last(item)

        # 找k次, 每次找到最大的, yield后删除
        for i in range(k):

            cursor = highest = t.first()

            while cursor:

                if cursor.element._count > highest.element._count:

                    highest = cursor

                cursor = t.after(cursor)

            yield highest.element._value

            t.delete(highest)


fl = FavoritestListMTF()
fl.access('a')
fl.access('a')
fl.access('b')
fl.access('b')
fl.access('a')
fl.access('c')
fl.access('d')
fl.access('d')
fl.access('d')
fl.access('c')
print(list(fl))
print(list(fl.top(3)))