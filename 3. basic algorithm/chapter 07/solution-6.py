# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    位置链表

    类似于数组数字索引, 希望链表也可以有位置的概念

    为了达到这个目的, 在链表外层再封装一次, 要求:
    1. 排除头, 尾结点的干扰
    2. 可以校验传入的位置的有效性
    3. 支持在位置p之前、之后返回/插入新的元素
    4. ...
"""


class DoubleLinkedList:
    class _Node:

        __slots__ = '_e', '_prev', '_next'

        def __init__(self, e=None):
            """注意这里变量加了_, 因为不想在外部能访问到"""
            """不过在类_Node的兄弟函数里有时也要直接访问这几个保护对象, 不过也只能这么写了"""
            self._e = e
            self._prev = None
            self._next = None

    def __init__(self):

        self._head = self._Node()
        self._tail = self._Node()

        self._head._next = self._tail
        self._tail._prev = self._head

        # 为了防止乱拼接, 基链表也可以存一个结点哈希表用于校验
        # 这么看来, 好像也不是非要外层再包一个Position
        # 和PositionLinkedList里的校验逻辑比较一下
        # 一个是父母记住哪些是自己孩子, 一个是孩子记住自己父母是谁

        self._nodelist = {self._head, self._tail}

    # 注意这里的校验函数名, 如果子类里给覆盖了
    # 父类用self._validate校验的时候也会调到子类的函数
    # 所以俩校验函数不能重名
    def _validate_n(self, node):
        if node in self._nodelist:
            return True
        return False

    def __len__(self):
        return len(self._nodelist) - 2

    def empty(self):
        return len(self) == 0

    def _insert_between(self, left, right, e):

        if not self._validate_n(left):
            raise TypeError

        if not self._validate_n(right):
            raise TypeError

        # 校验两个结点是否相邻
        if left._next is not right:
            raise TypeError

        if right._prev is not left:
            raise TypeError

        node = self._Node(e)

        node._prev, node._next = left, right

        left._next, right._prev = node, node

        self._nodelist.add(node)

        return node

    def _delete_node(self, node):

        if not self._validate_n(node):
            raise TypeError

        node._prev._next = node._next
        node._next._prev = node._prev

        r = node._e

        node._prev = node._next = node._e = None

        self._nodelist.remove(node)

        return r


class PositionLinkedList(DoubleLinkedList):
    """A sequential container of elements allowing position access"""
    """由于是'元素'的位置概念, 所以不包含头尾结点"""

    class _Position:
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """container记录节点归属的链表对象"""
            self._container = container
            self._node = node

        @property
        def element(self):
            """Return the element stored at this position"""
            return self._node._e

        def __eq__(self, other):
            """Return True if other is a position representing the same location"""
            """位置相等不要求是同一个对象"""
            if type(other) is not type(self): return False

            if other._container is not self._container: return False

            if other._node is not self._node: return False

            return True

    def _validate_p(self, p):
        """first, last等函数会对外暴露p, 插入函数外部传入p, 要校验"""

        if not isinstance(p, self._Position):
            return False

        # 注意删除结点的时候把Container置为None
        if p._container is not self:
            return False

        return True

    def _n2p(self, node):
        # 排除头尾结点
        if node in [self._head, self._tail]:
            return None

        return self._Position(self, node)

    def _insert_between(self, left, right, e):
        """override inherited version to return position, rather than node"""
        """这里override的唯一目的是处理返回类型, 校验什么的原函数都做了"""

        node = super()._insert_between(left, right, e)
        return self._n2p(node)

    # -------------------------------accessor----------------------------

    def first(self):
        # 除了删除直接返回值, 其余的都返回位置对象而非结点
        # 另外, 由于n2p函数里处理了头尾结点, 这里无需单独判断empty
        return self._n2p(self._head._next)

    def last(self):
        return self._n2p(self._tail._prev)

    def before(self, p):
        """Return the position just before position p; 外部传入的位置实例都要校验"""
        """注意, 元素结点才有before, 且首结点的before是None"""
        if not self._validate_p(p):
            raise TypeError

        return self._n2p(p._node._prev)

    def after(self, p):

        if not self._validate_p(p):
            raise TypeError

        return self._n2p(p._node._next)

    def __iter__(self):
        """Generate a forward iteration of the element of the list"""
        cursor = self.first()  # 如果空, 返回的是None

        while cursor:
            yield cursor.element
            cursor = self.after(cursor)

    # -------------------------------mutator----------------------------
    def add_first(self, e):
        """Insert element e at the front of the list and return new position"""

        return self._insert_between(self._head, self._head._next, e)

    def add_last(self, e):
        return self._insert_between(self._tail._prev, self._tail, e)

    def add_before(self, p, e):
        """Insert element e into list before position p and return new position"""
        if not self._validate_p(p):
            raise TypeError

        return self._insert_between(p._node._prev, p._node, e)

    def add_after(self, p, e):
        if not self._validate_p(p):
            raise TypeError

        return self._insert_between(p._node, p._node._next, e)

    def delete(self, p):

        """Remove and return the element at position p"""
        if not self._validate_p(p):
            raise TypeError

        r_e = self._delete_node(p._node)  # 这里直接返回的就是旧值

        p._container = p._node = None  # 别忘了这里去掉关联关系

        return r_e

    def replace(self, p, e):
        """Replace the element value at position p
        return the former value"""

        if not self._validate_p(p):
            raise TypeError

        r_e_old = p._node._e

        p._node._e = e

        return r_e_old

pll = PositionLinkedList()
for e in pll: print(e)
print(pll.empty())
print(pll.first(), pll.last())
p1 = pll.add_first(1)
p2 = pll.add_last(2)
for e in pll: print(e)
print(pll.first().element, pll.last().element)
pll.add_before(p1, 0)
pll.add_after(p1, 1.5)
print(list(pll))
print(pll.before(p2).element)
print(pll.after(pll.after(p1)).element)
pll.delete(pll.after(p1))
print(list(pll))
pll.replace(p1, 8)
print(list(pll))
print(len(pll))


