# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    循环链表

    在循环数组中, 只是循环存储, 队列元素本身无循环
    而循环链表中, 队列元素本身尾首相接, 尾指针右移即可实现队首元素出队入队尾

    典型应用场景: 轮转调度

    有A B C D E 几个任务

    当前资源分配给A, 然后A入队尾, 处理B, 直到处理完E, 下一个又是A了

    C D E A B, 假如正处理C时, 来了个新任务, 直接跟到当前队列后面, 即 C D E A B F
"""

class EmptyError(Exception):
    pass

class CircularQueue:

    class _Node:

        __slots__ = ['e', 'next']

        def __init__(self, e=None):
            self.e = e
            self.next = None

    def __init__(self):

        self._tail = None

        self._c = 0

    def empty(self):
        return self._c == 0

    def enqueue(self, e):
        node = self._Node(e)

        # 如果为空, node自循环, tail指向node
        if self.empty():

            node.next = node
            self._tail = node

        # 如果不为空, 把node接入尾部, tail后移
        else:
            node.next = self._tail.next
            self._tail.next = node
            self._tail = node

        self._c += 1

    def dequeue(self):
        if self.empty():
            raise EmptyError

        # 长度为1时要特殊处理
        if self._c == 1:
            r = self._tail
            self._tail = None
            self._c = 0

            return r.e

        r = self._tail.next
        self._tail.next = r.next
        self._c -= 1

        return r.e

    def first(self):
        if self.empty():
            raise EmptyError

        return self._tail.next.e

    def rotate(self, k):
        if self.empty():
            raise EmptyError

        for _ in range(k):
            self._tail = self._tail.next

    def show(self):

        p = self._tail

        for _ in range(self._c):
            p = p.next
            print(p.e, end=' ')
        print('')

q = CircularQueue(); q.show()
q.enqueue(1); q.enqueue(2); print(q.first())
q.enqueue(3); q.enqueue(4); print(q.dequeue())
q.show()

q.rotate(1); q.show()
q.rotate(1); q.show()
q.enqueue(5); q.show()



