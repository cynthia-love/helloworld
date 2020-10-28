# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    枚举求解:
    pot + pan = bib
    dog + cat = pig
    boy + girl = baby
    从0-9里枚举
    (注意这里是3道题, 并不是方程组)
"""

"""
    首先要确定有几个字母
    比如 pot + pan = bib
    p, o, t, a, n, b, i, 一共7个字母
    10*9*8*7*6*5*4种情况
    
    用一个数组表示这几个字母的值, s
    则pot: s[0]*100+s[1]*10+s[2]
    pan: s[0]*100+s[3]*10+s[4]
    bib: s[5]*100+s[6]*10+s[5]
    
    另外, 注意, 此题是排列而不是组合
    比如从a, b, c, d里选两个:
    1. 排列: 先选a, 然后从剩下的里面选第二个比如ab; 先选b, 第二次还可以选a, ab和ba认为是不同的
    2. 组合: 先选a, 然后从剩下的里面选第二个比如ab; 轮到b的时候, 第二次选只能从c, d里去选了
    这里有一个点需要明确, 对于排列问题, 目标集可以直接用set
    {a, b, c, d}从里面选3个:
    先选a, 然后从{b, c, d}里选, 这里是{b, c, d}还是{d, b, c}无所谓
    再选b, 然后从{a, c, d}里选, 同样, a, c, d的顺序不重要
    但是对于组合问题, 用set的时候要注意
    {a, b, c, d}
    第一重递归, 选第一个
    1. a, 下一递归待选{b, c, d}
    2. b, 下一递归待选{c, d}, 这里没有a, 即子递归返回后, 不再把a添加回去
    3. c
    4. d
    
    另外, 组合问题其实用list更合适
    [a, b, c, d], 顺序不会变
    第一重递归遍历到i的时候, 子递归从i+1开始选
"""

def f(k, s, b):
    if k <= 0:
        if (s[0]*100+s[1]*10+s[2])+s[0]*100+s[3]*10+s[4] == s[5]*100+s[6]*10+s[5]:
            print(s)
            return

    for e in b.copy():
        b.remove(e)
        s.append(e)
        f(k-1, s, b)
        s.remove(e)
        b.append(e)


# f(7, [], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 能不能设计的更智能化呢?
"""
    f(v1, v2, vs)
    三个参数分别表示第一个加数, 第二个加数, 第三个加数
    
    找个简单的例子测试: aa + ba = cb
"""

def f2(v1, v2, vs):
    # 第一步, 要得到待枚举的字母数量
    # 转成list是为了保证对应顺序不变
    # c-char, s-str
    cs = list(set(v1+v2+vs))

    """
    比如[b, c, a], 那么: 假设选出的
    三个数字是1, 8, 2, 那么直接得到: {b:1, c:8, a:2}
    借助zip, [(b, 1), (c, 8), (a, 2)]
    """
    def s2i(c2i, s):
        """

        :param c2i: {b:1, c:8, a:2}
        :param s: dog + cat = pig里的dog, cat, pig
        :return: 在{b:1, c:8, a:2}下的dog表示的整数值
        """
        res = 0
        for e in s:
            res = res*10+c2i[e]
        return res

    def check(c2i):
        """

        :param c2i: {b:1, c:8, a:2}
        :return:
        """
        return s2i(c2i, v1)+s2i(c2i, v2) == s2i(c2i, vs)

    from helloutils.tracker import Track

    def rf(k, res, base):
        if k <= 0:
            d = dict(zip(cs, res))
            if check(d):
                print(d)
                return True
        else:
            for e in base.copy():
                base.remove(e)
                res.append(e)
                if rf(k-1, res, base): return True
                res.remove(e)
                # 排列问题, abcd, 第一次选b的时候, 第二次还能选a, 所以a得加回去
                # 如果是组合问题, 这里就不加回去了
                base.add(e)

    # 结果是排列, 即有序, res得用list而不是set
    rf(len(cs), [], {1, 2, 3, 4, 5, 6, 7, 8, 9, 0})

f2("aa", "ba", "cb")

# 再理一下排列和组合, 先排列, res得用list, base都行
def f1():

    from helloutils.tracker import Track

    def rf(k, res:list, base:set):
        if k == 0:
            print(res)
            return
        for e in base.copy():
            base.remove(e)
            res.append(e)
            rf(k-1, res, base)
            res.remove(e)
            base.add(e)

    rf(3, [], {1, 2, 3, 4})

f1()

# 组合, res, base用list或set都行, 不过用set的时候有点小问题, 还是建议用list
def f2():
    from helloutils.tracker import Track

    def rf(k, res: list, base:set):
        if k == 0:
            print(res)
            return

        for e in base.copy():
            base.remove(e)
            res.append(e)
            rf(k-1, res, base.copy())
            res.remove(e)

    rf(3, [], {1, 2, 3, 4})

f2()

def f3():

    def rf(k, res: set, pos: int, base: list):
        if k == 0: print(res)
        if len(base)-pos < k: return

        for i in range(pos, len(base)):
            res.add(base[i])
            rf(k-1, res, i+1, base)
            res.remove(base[i])

    rf(3, set(), 0, [1, 2, 3, 4])

f3()

# 综上, 建议排列: list-set, 组合: set-list