# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    二维数组排序, 可以指定key
"""
"""
    尝试写归并
    
    1, 2, 4, -1, 3, 2
    
    思路, 要整个有序, 则前半部分有序, 且后半部分有序, 然后合并
    
"""
l = [(1, 2), (3, 4), (-1, 3), (8, 8), (2, 1)]

def f(key):

    def rf(pl, pr):
        if pl >= pr: return

        mid = (pl+pr) // 2

        rf(pl, mid)
        rf(mid+1, pr)

        # merge
        l1, p1 = l[pl:mid+1], 0
        l2, p2 = l[mid+1:pr+1], 0

        # 好好理一下这块归并的思路, 比之前写的更优
        # 第一个子串超限, 外层还在循环, 说明第二个子串还没完, 内层直接继续遍历第二个
        # 两个都没超限, 才是去比较两个子串的当前元素大小, 小的赋值给外层数组然后指针指向下一个
        for i in range(pl, pr+1):
            if p1 > len(l1)-1:
                l[i] = l2[p2]
                p2 += 1
            elif p2 > len(l2)-1:
                l[i] = l1[p1]
                p1 += 1

            else:
                if key(l1[p1]) < key(l2[p2]):
                    l[i] = l1[p1]
                    p1 += 1
                else:
                    l[i] = l2[p2]
                    p2 += 1

    rf(0, len(l)-1)

    print(l)
f(key=lambda x: x[0])
f(key=lambda x: x[1])

# 思考, 归并时能否不借助中间数组, 比如[1, 2, 3, 4, 2, 2, 5, 8], 知道分割线位置
# 能, 不过时间复杂度不如借助中间数组
ll = [1, 2, 3, 4, 2, 2, 5, 8]
pp = 4
# 思路, 遍历2, 2, 5, 8, 对左边的有序数组部分做插入
# 同时, 由于右边也是有序的, 较普通插入可以记住上一次插入位置, 下一次遍历不超过该位置+1

def f():
    mark = 0  # mark用于标记可插入空间的左界(包含)
    for i in range(pp, len(ll)):
        t = ll[i]  # 这里注意元素右移会覆盖初始i位置的元素, 设置个临时变量存一下
        # 从t元素的左边一个位置遍历, 大于就将元素右移, 直到不大于, 那么右边那个空位就是待插入位置
        for j in range(i-1, mark-1, -1):

            if ll[j] > t:
                ll[j+1] = ll[j]
            else:
                ll[j+1] = t
                mark = j+1+1
                break
        # 如果中间没有break, 表示过了mark, 所有元素都大于, 则左界mark位置就是待插入位置
        # 注意这里是取不到j变量的
        else:
            ll[mark] = t
            mark += 1

    print(ll)

f()