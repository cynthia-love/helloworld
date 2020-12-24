# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计队列
    构造函数可以接受maxlen
    如果不指定, 则队列满之后自动扩展
    如果指定, 则队列满之后抛异常
"""
class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Queue:
    MAXLEN = 5

    def __init__(self, maxlen=None):

        if maxlen:
            self._data = [None]*maxlen
            self._fix = True
        else:
            self._data = [None]*Queue.MAXLEN
            self._fix = False

        self._head = 0
        self._count = 0

    def __len__(self):
        return self._count

    def empty(self):
        return len(self) == 0

    def enqueue(self, e):
        if self._count == len(self._data):
            if self._fix:
                raise FullError
            else:
                self.resize(2*len(self._data))

        self._data[(self._head+1+self._count) % len(self._data)] = e
        self._count += 1

    def dequeue(self):
        if self.empty():
            raise EmptyError

        res = self._data[(self._head+1) % len(self._data)]
        self._data[(self._head+1) % len(self._data)] = None

        self._head = (self._head+1) % len(self._data)

        self._count -= 1

        if self._count <= len(self._data) / 4:
            self.resize(len(self._data) // 2)

        return res

    def head(self):
        if self.empty():
            raise EmptyError

        return self._data[(self._head+1) % len(self._data)]

    def resize(self, c):
        data2 = [None]*c
        head2 = 0

        for i in range(self._count):

            data2[(head2+1+i) % c] = self._data[(self._head+1+i) % len(self._data)]

        self._data = data2
        self._head = head2

    def show(self):
        print(self._data)

q = Queue(); q.show()
q.enqueue(1); q.enqueue(2)
q.enqueue(3); q.enqueue(4)
q.enqueue(5); q.show()
q.enqueue(6); q.show()

q = Queue(5); q.show()
q.enqueue(1); q.enqueue(2)
q.enqueue(3); q.enqueue(4)
q.enqueue(5); q.show()
# q.enqueue(6); q.show()
q.dequeue(); q.show()
q.dequeue(); q.show()