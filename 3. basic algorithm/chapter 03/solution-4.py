# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    算法分析示例
"""
def f1():
    """
        len(list)是单独存储的, 无需遍历, 所以时间复杂度是O(1)
        list[index], 元素是连续存储的, 可以直接根据索引计算位置, 无需遍历, 所以时间复杂度也是O(1)
    """
    l = [1, 2, 3, 4, 5]
    print(len(l))
    print(l[0])

def f2():
    """
        a*n+b
    """
    l = [1, 2, 3, 4, 5]
    for each in l:
        if each == 8:
            return each
    return False

def f3():
    """
        整个算法的时间复杂度O(n)没悬念
        那如果只看 vmax = each 这个原子操作呢
        最差更新n次, 即O(n)
        平均呢?
        第i个数是前i个数最大的概率是1/i
        所以第一个更新概率: 1/1
        第二个: 1/2
        第三个: 1/3
        第n个: 1/n
        所以更新次数的期望为: 1/1+1/2+1/3...+1/n, 为θ(log(n))  (其实更精确的是ln(n), 但时间复杂度分析
        对数级的一般都直接用log(n)代表, 而不是用ln(n))

    """
    l = [1, 2, 3, 4, 5]
    vmax = 0
    for each in l:
        if each >= vmax:
            vmax = each

    return vmax

def f4():
    l = [1, 2, 3, 4, 5]
    # 计算l的前缀平均值, 即前1个的平均值, 前2个的平均值, 前3个的平均值
    # 即[1, 3/2, 6/3, 10/4, 15/5]

    # 思路1
    def f41():
        res = [0]*len(l)  # n
        for i in range(len(res)):
            total = 0  # n
            for j in range(i+1):
                total += l[j]  # 1+2+3+..+n
            res[i] = total/(i+1)  # n
        return res  # 1
    """
        分析: n+n+(1+2+..+n)+n + 1
        = 3n+1+n*(n+1)/2 = O(n^2)
    """

    # 思路2
    def f42():
        res = [0]*len(l)  # n
        for i in range(len(res)):
            res[i] = sum(l[:i+1])/(i+1)  # sum本质上也是一个函数
        return res  # 1
    """
        分析: n+(1+2+..+n)+1 = O(n^2), 只是少了一个n, 时间复杂度量级还是n方
    """

    # 思路3
    def f43():
        res = [0]*len(l)  # n
        total = 0  # 1
        for i in range(len(res)):
            total += l[i]  # n
            res[i] = total/(i+1)  # n
    """
        分析: n+1+n+n = O(n)
    """


def f5():
    # 三个集合不相交
    s1 = {1, 2, 3}
    s2 = {4, 5, 3}
    s3 = {5, 8, 0}

    # 思路1, 暴力枚举, O(n^3)
    def f51():
        for e1 in s1:
            for e2 in s2:
                for e3 in s3:
                    if e1 == e2 == e3:  # 2*n^3
                        return True
        return False

    # 思路2, 暴力枚举改进 !!!, 这个的时间复杂度分析要注意, 很容易错
    def f52():
        for e1 in s1:
            for e2 in s2:
                if e1 == e2:  # n*n
                    for e3 in s3:
                        if e2 == e3:
                            return True
                else: continue  # 加上个else好理解些
        return False

    """
        有点绕, 首先s1, s2, s3都是set, 所以内部不存在相同的值
        假设长度分别为n1, n2, (n1小)
        那么最多进到if n1次, 进到else n1*n2-n1次
        时间复杂度为: (n1*n2-n1)*1 + n1*n3 = O(n^2)
    """

def f6():
    # 判断元素唯一性
    l = [1, 2, 3, 4, 3]

    # 思路1, 暴力枚举, O(n^2)
    def f61():
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i] == l[j]:  # n-1, n-2, ...1 = (n-1)*n/2
                    return False
        return True

    # 思路2, 排序后一次遍历, 按最高效的排序算法 n*log(n)+n = O(n*log(n))
    def f62():
        l.sort()
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                return False
        return True

    # 思路3, O(n)
    def f63():

        s = set(l)
        return len(s) == len(l)

