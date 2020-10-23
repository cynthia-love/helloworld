# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    设计递归, 输出一个含有n个元素的集合的所有子集

    分析: 比如{a, b, c}, 求组合, 从0到n都要有
    {}
    {a}, {b}, {c}
    {a, b}, {a, c}, {b, c}  (还有一种场景, ab和ba认为是俩)
    {a, b, c}

    以C(n, 2)为例, 为了实现组合而不是排列有两种办法

    1. 遍历的时候就控制好
    第一轮a或b或c, a的话下一轮从bc里选, b的话下一轮从c里选, c的话无
    2. 遍历的时候按排列算, 最后去重
    第一轮a, 第二轮从bc里选; b, 第二轮从ac里选; c, 第二轮从ab里选
    得到: ab, ac, ba, bc, ca, cb, 再去重
    3. 直接绕过这种思维定式, 其他更巧妙的算法

"""

"""
    方法1, 最基础的思路, 从C(n, 0)一直到C(n, n)
    然后求C(n, k)的时候先选一个, 然后从右边剩下的选第二个, 重复此过程, 直到选够k个
    这里从右边剩下的选下一个, 而不是从所有剩下的选下一个, 可以保证结果不重复, 省去最后去重过程
"""
from helloutils.tracker import Track
s = [1, 2, 3]  # s用list有序遍历, 可以避免出现重复结果

def f1(k, res, pos):

    # 如果待选元素不够了, 直接返回
    if len(s)-pos+1 < k:
        return

    # k==0, 表明已经选够了要选的元素
    if k == 0:
        print(res)
    else:
        # 否则从待选里再选一个
        for i in range(pos, len(s)):
            res.add(s[i])
            # 选完, 再从选的元素的右边选下一个
            # 而不是只是简单去掉选的元素
            # 123, 1->2, 1->3, 2->3, 最后就不用去重了
            f1(k-1, res, i+1)
            res.remove(s[i])

# for i in range(len(s)+1):
#     f1(i, set(), 0)


"""
    方法2, 对方法1的优化
    其实, 求C(n, k)的过程已经包含了C(n, k-1)的解
    进一步优化得出思路如下:
    1, 2, 3
    
    f({}, 0)
    f({1}, 1)
    f({1, 2}, 2)
    f({1, 2, 3}, 3)
    f({1, 3}, 3)
    f({2}, 2)
    f({2, 3}, 3)
    
    先输出{}
    然后遍历1, 2, 3, 加入res中, 打印{1}, {2}, {3}
    遍历1的时候, 子递归, res={1}, pos标记的待选{2, 3}, 然后遍历{2, 3}添加第二个元素
    比如是2, res={1, 2}, 待选{3}, 继续, res{1, 2, 3}, 待选{}
    比如是3, res={1, 3}, 待选{}, 下一轮子递归输出{1, 3}后, 直接递归, 不再进行其他操作
    
    思路上很巧妙, 也很简洁, 但是时间复杂度并不好    
"""
@Track
def f2(res, pos):
    print(res)
    if pos > len(s)-1: return

    for i in range(pos, len(s)):
        res.add(s[i])
        f2(res, i+1)
        res.remove(s[i])

# f2(set(), 0)

"""
    方法3, 二进制位, 比如[1, 2, 3]
    000->{}
    001->{3}  (实际上右边是低位, 这里应该是{1})
    010->{2}
    011->{2, 3}
    100->{1}
    101->{1, 3}
    110->{1, 2}
    111->{1, 2, 3}
    刚好和所有子集对应...
    由此引申, 不枚举, 只求特定C(n, k)也可以用这种办法...
"""

def f3():
    for i in range(2**len(s)):
        # res = set()
        # for j in range(len(s)):
        #     if 1 << j & i:
        #         res.add(s[j])
        # print(res)
        res = {s[k] for k in range(len(s)) if 1 << k & i}
        print(res)

# f3()

# 当然, f3可以强行写成递归形式
def f4(n):
    if n < 0: return
    print({s[k] for k in range(len(s)) if 1 << k & n})
    f4(n-1)

f4(2**len(s)-1)


