# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    基于数组的序列和基于链表的序列对比
"""

"""
    数组优点:
    1. 根据索引k访问元素, O(1), 而链表O(k), 双向链表O(n-k)
    2. 忽略大小调整, enqueue基于数组操作很简单, 而基于链表涉及节点实例化、拼接等CPU操作更多
    3. 使用存储空间更小, 虽然有备用内存, 长度为n时可能占用2n, 但链表远不止2n
    
    链表优点:
    1. 有最坏情况的时间界限, 考虑有些场景, 要求每个操作都得快, 而不是整体平均快, 那么数组有时候
    触发动态扩展就是不可接受的, 这时候要用链表
    2. 可以提供时间复杂度为O(1)的插入和删除(借助PositionList描述位置), 比如编辑器光标位置插入,
    而数组如果不是末尾, 就要O(n-k)
    
"""