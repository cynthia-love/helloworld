# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    输出'c', 'a', 't', 'd', 'o', 'g' 所有可能组成的字符串, 不可重复
    注意, 经常遇到的问题有四种:
    1. 全排列-最优字典法
    2. 排列
    3. 组合
    4. 子集(即所有长度的组合)-最优二进制数法

    注意对应的库函数
    print(list(permutations(x)))  # 1全排列
    print(list(permutations(x, 2)))  # 2部分排列
    print(list(combinations(x, 2)))  # 3组合

    子集可以通过遍历所有长度的combinations(x, 2)得到

"""

"""
方法1: 内置函数permutations
方法2: 递归, 每一轮删掉一个备选值, 即n*(n-1)*(n-2)...
方法3: 回溯, 不删, 进到下一递归看当前字符是否已经用过
方法4: n进制自然进位, 012-210, 过滤掉有重复的排列
方法5: 插入, c->插a得到ac, ca->插t得到tac,atc,act和tca,cta,cat
方法6: 邻位对换, 123, 初始移动方向都向左, 不断寻找最大可移动数:移动方向的下一位小于自己
      移动完之后, 所有比它大的数反向; 123, 3->132, 3->312, 2->321, 3
      即3往12里插, 插不动了, 改一下12的顺序, 3就可以反向再插一波
方法7: 字典序法3 5421, 从右到左找到第一个非递增的数, 这里是3, 因为5421从右向左递增
      就4位看, 已经是最大了, 那么下一个排列一定是4打头, 即第一个比3大的数, 互换
      4 5321, 换完之后肯定还是倒叙, 因为打头的大了1, 那么右侧倒一下就行了4 1235

方法8: 递增中介, 35421, 原始中介数(右侧小于当前的个数)2321, 原始中介不好翻译, 调整顺序
      改为从n到1计算中介, 即3221, 转回去用数空格法, 然后计算下一个3221+1=3222
      从右向左进制分别为2345, 进位计算得到3300
      
方法9: 递减中介, 不按5432排, 而是按2345排, 即1223, 进制分别为2345, 这么相对于递增, 进位计算变少了

方法10: 递减中介的进阶思路, 不借助中介数直接变, 12345, 5的中介数增加的逻辑是5左移, 最终变成51234
      到头了, 再加1, 变0, 即5移到右边, 然后4左移一位12435
      考虑特殊情况54123, 5的中介数加1变0, 进1, 4的中介数也会变0, 再进1, 3左移
      注意5和4都是0, 到右边顺序是45而不是54, 所以下一个排列是13245
"""
from itertools import permutations
def f1():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    g = permutations(l, len(l))
    l_p = list(g)
    return ["".join(x) for x in l_p]

print(len(set(f1())))

# 其他方法, 自己实现
# 方法1, 递归最一般思路, 枚举, 在当前数组里面选一个, 剩下的继续递归, 直到数组长度为1, 全拼起来append到结果集里去

def f2():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    def rf(res, l):
        if len(l) == 1:
            r.append(res+l[0])
        else:
            for i in range(len(l)):
                rf(res+l[i], [l[j] for j in range(len(l)) if j!=i ])
                # 注意这里用的解析语法, 会生成一个新的[], 避免直接在原[]上改影响了下一次递归

    rf("", l)
    return r
print(len(set(f2())))

# 方法2, 回溯法
# 和f2的区别在于, f2是准入控制, 已经用到的字符就不传给下一级递归了
# 而回溯法则是可以到下一级递归, 发现不符合条件再回去
def f3():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []

    def rf(res, s):
        if s in res: return
        # 注意这里判断的一定是5, 而不是6
        if len(res) == 5:
            r.append(res+s)
            return
        for each in l:
            rf(res+s, each)

    for each in l:
        rf("", each)

    return r
print(len(set(f3())))

# 方法4, n进制元素自然进位法(不停地加1, 然后过滤掉不符合要求的项), 效率低
# 012->020->021->022->100->101->...
# 最后一次循环为1-000
def f4():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    n = len(l)
    k = list(range(n))  # 初始012345

    while sum(k) != 0:  # 555555->1-000000
        if len(set(k)) == n:
            r.append("".join([l[i] for i in k]))
        flag = 0
        for i in range(n-1, -1, -1):
            k[i] = k[i] + 1 if i == n-1 else k[i] + flag
            flag = 0
            if k[i] >= n:
                k[i] %= n
                flag = 1
            else:
                break
    return r

print(len(set(f4())))

# 方法5和6, 递归的另一种思路, 插入以及衍生的号称最蛋疼的全排列邻位对换法
def f5():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    # 插入思路, c->ac, ca->tac, atc, act, tca, cta, cat->...

    def rf(s, i):
        if len(s) == len(l):
            r.append(s)
            return
        # 枚举位置比s长度多一个
        for j in range(len(s)+1):
            rf(s[:j]+l[i]+s[j:], i+1)
    rf("", 0)
    return r
print(len(set(f5())))

"""
    邻位对换法思路, 不断地找最大可移动数
    (1)可移动概念, 一个数沿着它的方向的邻位比它小(需要引入方向概念)
    (2)如果一个可移动的数发生了移动, 那么所有比他大的数的方向都反过来
    有点绕, 基本思路其实很简单: 1234, 找到最大可移动的数4, 1243
    继续找最大可移动数4, 1423, 继续, 4123, 再找最大可移动数3
    4132, 因为3移动了, 把大于3的方向反向, 此时继续找最大可移动, 又变成了4
    
    1234->1243->1423->4123
    123->132
    4132->1432->1342->1324
    132->312
    3124->3142->3412->4312
    12->21
    4321->3421->3241->3214
    321->231
    2314->2341->2431->4231
    231->213
    4213->2413->2143->2134
    
"""
def f6():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    n = len(l)
    # k存储索引序列, 即我们要排序的对象
    # d存储各个索引的初始方向, 初始都向左, 即-1
    k = list(range(n))  # [0, 1, 2, 3, 4, 5]
    d = [-1 for _ in range(n)]  # [-1, -1, -1, -1, -1, -1]

    def findTop():
        top_i, top_v = -1, -1
        # 这里直接遍历k就好, 没必要非要从大到小找
        # 从大到小找倒是可以提前终止, 不过还得去反向定位其在k中的位置
        for i in range(n):
            # 符合条件的要求: 移动方向上的下一个位置的值小于当前值
            if k[i] > top_v and 0 <= i+d[k[i]] < n and k[i+d[k[i]]] < k[i]:
                top_i, top_v = i, k[i]
        return top_i, top_v

    r.append("".join([l[i] for i in k]))

    while True:
        t_i, t_v = findTop()
        if t_i == -1: break

        # 注意这里的改变方向要放在位置移动前面
        for i in range(t_v+1, n):
            d[i] = -d[i]

        # 待移动位置t, 邻位t+d[k[i]]
        k[t_i], k[t_i+d[t_v]] = k[t_i+d[t_v]], k[t_i]

        r.append("".join([l[i] for i in k]))

    return r
print(len(set(f6())))

# 方法7, 字典序法, 最推荐的算法
"""
    思路, n进制元素自然进位法会有很多冗余
    012-020-021-022-100....
    实际上, 这种冗余是可以避免的
    以3421为例, 下一个应该是4123, 怎么变换过去的?
    首先, 从右向左找到第一个非升序的数字(小于右近邻), 1-2-4, 3找到
    然后3-421, 将3和右侧124里第一个大于它的数字互换, 变成4-321
    互换之后, 将右侧翻转, 变成4-123, 即得到下一个数字
    
    原理依据是什么呢?
    xxTcba, cba是从大到小, 找下一个排线显然在其内部变化已经不可能, 要扩展到第4位T
    3-5421, cba部分已经最大, 那么3-5421的下一个的第一位数字肯定是刚刚大于3的一个数字
    刚刚大于3什么概念, 5-4-21, 大于3, 右侧降序, 那么5肯定也大于3, 因为是刚刚大于, 说明2肯定小于3不然就找2了
    4-5321, 那么替换之后的右侧序列一定还是降序的, 4替换3已经实现了进位, 那么相应的右侧要变成最小值, 即翻转
    4-1235, 即得到下一个序列
    
"""
def f7():
    ls = ['c', 'a', 't', 'd', 'o', 'g']
    res = []
    n = len(ls)
    k = list(range(n))

    # 找到第一个左侧小于右侧的在k中的索引
    # 找不到返回-1, -1, 找到了, 返回其索引和右侧刚好大于其值的索引
    def findLR():
        # 因为索引存在0, 这里不要用None, 不然外面判断会有问题
        l, r = -1, -1
        for i in range(n-2, -1, -1):
            if k[i] < k[i+1]:
                l = i
                break  # 找到第一个左小于右的, 就终止循环
        if l != -1:
            for i in range(l+1, n, 1):
                if k[i] > k[l]:
                    r = i
                else:
                    break
                    # l有值, 那么r一定有, 大于k[l]继续往右找, 可以找到刚好大于的
        return l, r

    def reverse(l):  # l为待翻转的最左索引
        l, r = l, n-1
        while l < r:
            k[l], k[r] = k[r], k[l]
            l += 1
            r -= 1

    res.append("".join([ls[i] for i in k]))
    l, r = findLR()
    while l != -1:
        k[l], k[r] = k[r], k[l]
        reverse(l+1)
        res.append("".join([ls[i] for i in k]))
        l, r = findLR()
    return res

print(len(set(f7())))

# 方法8, 中介数, 分为递增中介和递减中介
"""
    核心思路, 当A->B无法直接推导的时候, 将A->A2, A2->B2, B2->B, 借一个中介实现转换
    
    还是以35421为例(24210也可以, 不影响), 
    
    注意, 中介数不止一种, 分为原始中介数, 递增中介数, 递减中介数
    原始中介数是按原顺序排的, 比如35421右边比当前小的个数分别为2321, 这里的原始中介数是2321
    
    原始中介数也是能转回去的, 只不过比较绕, 比如第一位2, 一个5个数, 右边比它小的2个, 那么比它大的也2个, 所以是3
    去掉3之后, 第二位3, 剩下4个数里排行第4, 所以是5
    然后2, 第三位2, 剩下3个数里排行第3...这里最大问题是, 剩下的数这个概念与之前去掉的数有关系, 需要知道哪些
    已占用, 然后排序, 找第k个
    
    在原始中介数的基础上, 新增递增中介数的概念, 即算中介数的时候, 按从大到小算
    35421, 5的事3, 4的是2, 3的事2, 2的是1, 所以中介数3221
    
    转回排列时, _ _ _ _ _, 5右边有3个, _ 5 _ _ _, 4右边有2个, _ 5 4 _ _, 3右边2个
    3 5 4 _ _, 2右边1个, 3 5 4 2 1
    
    注意递增中介数和原始中介数, 算出来的序号不一样, 但两者序号范围是一样的, 都是0~n!-1
    且初始12345, 对应的递增中介和原始中介都是0 0 0 0
    结尾54321, 对应的递增中介和原始中介都是4 3 2 1
    
    然后是算中介数的下一个, 比如3221, 加1, 3222, 右边第一位进制为2
    
"""

import math
def f8():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    n = len(l)
    # 初始k, 后面中介数转k都用这个, 节约空间
    k = list(range(n))
    # 初始中介数
    m = [0 for _ in range(n-1)]

    def m2k():
        for i in range(n):
            k[i] = -1
        for i in range(n-1, -1, -1):
            if i == 0:
                for j in range(n):
                    if k[j] == -1:
                        k[j] = 0
            else:
                # i对应的中介数位置为n-1-i
                e = 0  # 空格计数
                for j in range(n-1, -1, -1):
                    if k[j] == -1:
                        e += 1
                    if e == m[n-1-i]+1:
                        k[j] = i
                        break
    def nextM():
        add = 0  # 进位
        m[-1] += 1
        for i in range(n-2, -1, -1):
            m[i] = m[i] + add
            add = 0  # 加完记得重置回0
            # 算第i位的进制
            base = n - i
            if m[i] >= base:
                m[i] = m[i] % base
                add = 1
            else: break

    for i in range(math.factorial(n)):
        m2k()
        r.append("".join([l[i] for i in k]))
        nextM()

    return r

print(len(set(f8())))


# 与递增中介数类似, 还可以用递减, 比如35421, 对应2321, 按2345排列: 1223, 进制分别为2345
# 除了加法和递增的不一样, 由中介数转换为排列时方法基本一样(无非是定位中介数索引时不一样)
import math
def f9():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    n = len(l)
    # 初始k, 后面中介数转k都用这个, 节约空间
    k = list(range(n))
    # 初始中介数
    m = [0 for _ in range(n-1)]

    def m2k():
        for i in range(n):
            k[i] = -1
        for i in range(n-1, -1, -1):
            if i == 0:
                for j in range(n):
                    if k[j] == -1:
                        k[j] = 0
            else:
                # i对应的中介数位置为n-1-i
                e = 0  # 空格计数
                for j in range(n-1, -1, -1):
                    if k[j] == -1:
                        e += 1
                    if e == m[i-1]+1:  # 与递增中介的第一个区别, 找值x的中介数索引
                        k[j] = i
                        break
    def nextM():
        add = 0  # 进位
        m[-1] += 1
        for i in range(n-2, -1, -1):
            m[i] = m[i] + add
            add = 0  # 加完记得重置回0
            # 算第i位的进制
            base = i + 2  # 与递增中介的第二个区别, 进制是从左往右由2开始增的, 而不是从右往左由2开始增的
            if m[i] >= base:
                m[i] = m[i] % base
                add = 1
            else: break

    for i in range(math.factorial(n)):
        m2k()
        r.append("".join([l[i] for i in k]))
        nextM()

    return r

print(len(set(f9())))

# 方法10, 递减中介数的优化算法, 不用算中介数
"""
    思路: 比如35421, 对应2321-0, 按2345排列: 0-1223, 进制分别为2345
    0-1223+1变成1224实际上是什么? 5右边比它小的数增加了1个, 4, 3, 2的没变
    即 5 3 4 2 1, 那么4321的相对位置就不能变, 仅仅3和5互换了位置
    1224再加1, 变成1225 -> 1230, 2的右边没变, 3的右边没变, 4的右边加1, 5的右边变0
    3 2 1相对位置没变, 5和4互换, 然后5移到最右边, 4 3 2 1 5
    上述两个例子其实覆盖了两种情况
    1. 中介数末尾小于等于n-2, 加1后小于等于n-1, 不用进位, 反应到排列上就是左边不是最大值
    那么将最大值左移一位即可
    2. 中介数末尾等于n-1, 加1后等于n, 需要进位, 末尾变0, 即原排列左边最大值移到最右边
    进位后下一位是否进位判断标准和最高位类似, 5 3 4 2 1-> 3 4 2 1 5, 不用进位, 变成4 3 2 1 5即可
    如果是5 4 3 2 1 -> 4 3 2 1 5, 4在最左边, 还要进位, 这里的还要进位注意了, 是变成 3 2 1 4 5
    而不是3 2 1 5 4, 因为5和4进位后都是0, 4放右边, 那5的中介就变成1了

    再捋一下
    12345->12354->12534...51234, 这个过程是保持1234不动不停地动5
    5到头了, 右边4个, 再加就超了, 会变0, 同时给4的中介+1, 1 2 3 4 5, 4不在最左边, 可以直接加
    1 2 4 3 5, 继续移动5, 往1 2 4 3里插, 一直到5 1 2 4 3
    继续此操作, 直到变成5 4 1 2 3, 5的中介+1后边0, 进位, 4的也+1, 然而4在最左边, 所以4的也变0
    注意这里的变0, 移到右边45才是两个都是0, 而不是54, 注意这个顺序
    1 2 3 4 5, 最左不是3, 可以直接加3的中介, 即左移1, 1 3 2 4 5, 然后又可以移动5了
    继续此循环, 直到变成5 4 3 2 1, 没有下一位了, 因为t最终会得到0, 可以把这个作为边界条件返回-1
"""

def f10():
    l = ['c', 'a', 't', 'd', 'o', 'g']
    r = []
    n = len(l)
    k = list(range(n))

    def nextK():

        t = n-1
        tmp = []
        # 54231变23145再变32145
        while k and k[0] == t:
            k.pop(0)
            tmp.insert(0, t)
            t -= 1
        k.extend(tmp)

        for i in range(n - 1, -1, -1):
            if k[i] == t:
                k[i], k[i - 1] = k[i - 1], k[i]
                break

    for i in range(math.factorial(n)):
        r.append("".join([l[i] for i in k]))
        nextK()

    return r

print(len(f10()))