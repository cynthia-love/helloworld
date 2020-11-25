# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    栈, 队列和双端队列

    注意, 这几个概念是较数组更高一级的概念, 是逻辑上的关系而非存储上的

    其底层既可以用数组(顺序表)实现, 也可以用链表实现

    另外, 还有引用数组, 直接数组, 是数组存地址还是存值的概念

    动态数组, 静态数组, 是数组是否可变上的概念

    上述分类方法的不同引出的不同概念不要混淆了
"""

"""
    栈, LIFO, 后进先出, 或者说FILO先进后出的数据结构, 栈顶压入栈顶取出
    
    典型的应用比如浏览器的后退, 用户从A->B, 则将A及对应信息入栈, 从B->C则B入栈,
    当用户在C页面点后退的时候, 从栈顶取最近一次访问的B, 退过去, 同时B出栈, 再点退回A
    
    再比如文本编辑器的撤销操作, 编辑器会记住用户最近几次的操作, 每点一次撤销, 就取
    最近一次的操作回滚, 同时该操作出栈, 再点, 再取一次
    
    再比如git, 实际上存的也是一次次的操作记录
    
    当然, 实际设计的时候并不一定是要出栈, 因为还有前进操作, 猜测是有一个指针指向当前页面???
    
"""

"""
    栈的抽象数据类型, Abstract Data Type, 数据类型的抽象表示
    包括数据对象、数据对象之间的关系和数据对象的基本操作(注意操作也包含在内)
    
    栈支持的操作:
    
    push(e), 将一个元素压入栈顶
    pop(), 栈顶的一个元素出栈并返回, 如果为空, 报错
    top(), 栈顶的一个元素不出栈返回, 如果为空, 报错
    empty(), 为空返回True, 否则返回False
    len(栈), 返回栈中元素的数量
"""

"""
    利用适配器模式+动态引用数组类型list实现自定义栈
    
    这种把一个类的方法利用适配器类包装一下, 变成另一个方法的设计模式称为适配器模式
    
    比如狗的bark和猫的meow, 可以用一个适配器封装, 提供统一make_sound方法
    
    根据传入的类是狗还是猫, make_sound调用不同的方法
    
    本例中, 不存在这种动态适配, list直接写在Adaptor里就行
"""

# 特别地, 要自定义一个空错误类型, 代替list为空时的IndexError

class EmptyError(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class Stack:
    """FILO Stack implementation using a Python list as underlying storage
    一共有__init__, push, pop, top, empty, __len__ 六个方法
    """

    def __init__(self):
        """Create an empty stack"""
        self._data = list()

    def __len__(self):  # O(1)
        """Return the number of elements in the stack"""
        return len(self._data)

    def empty(self):  # O(1)
        """Return True if the stack is empty"""
        # 这里len(self), len(self._data)都行
        # 既然定义了__len__, 直接用len(self)吧
        return len(self) == 0

    def push(self, e):
        """Add an element e to the top of the stack"""

        self._data.append(e)  # O(1)

    def pop(self):
        """Remove and return the element from the top of the stack
        Raise EmptyError if the stack is empty
        """
        if self.empty():
            raise EmptyError('Stack is empty')

        return self._data.pop()  # O(1)

    def top(self):
        """Return but not remove the element at the top of the stack
        Raise EmptyError if the stack is empty"""
        if self.empty():
            raise EmptyError('Stack is empty')

        return self._data[-1]  # O(1)

    def __str__(self):
        return ', '.join(str(e) for e in self._data)

s = Stack()

s.push(5)
print(s)
s.push(3)
print(s)
print(len(s))
s.pop()
print(s)
print(s.empty())
s.pop()
print(s.empty())
# s.pop()
s.push(7)
s.push(9)
print(s.top())
print(s)
s.push(4)
print(s)
print(len(s))
print(s.pop())
print(s)
s.push(6)
s.push(8)
print(s)
s.pop()
print(s)
"""
5
5, 3
2
5
False
True
9
7, 9
7, 9, 4
3
4
7, 9
7, 9, 6, 8
7, 9, 6
"""


