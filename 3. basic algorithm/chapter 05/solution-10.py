# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    字符串类
"""
"""
    重点掌握KMP算法的思路
    ababcabcacbab
      abcac
    
    基本思路, 上指针不回溯
    比如这里, 上指针指向b, 下指针指向c, 不匹配
    传统思路是整个抛弃此次匹配, 上方从a的下一个, 再重来一遍匹配
    
    而KMP算法, 提前算出c的next值为1, 即前面子串的前缀后缀最大公共子串长度a-bc-a
    
    匹配到了b-c, 说明前面abca部分是匹配上了的
    abcab
     abcac
    假设下方右移一位, a-bca-b, abc-ac, 绝对不可能匹配上, 否则和c的next值为1矛盾
    abcab
      abcac
    下方移动两位, 同理, 与next值为1矛盾
    
    只有下方移动3位时, 才能匹配上, 也就是下指针 b-(b-next[b])
    
    这么思考其实有点绕, 换个思路, aabaac, 假设c那里没匹配上, 显然, next[c] = 2
    aabaad
    aabaac, 把下面的想象凹下去的, 上面凸的, 为2表示
    aabaad
       aabaac, 把下面拉到这个位置时, 上下才能嵌到一起, 参照系为上指针, 那么相当于下指针变成next[c]
    即从next[c]位置继续和上串匹配, 前面的就不比了
"""

# 生成
s1 = "hello world"  # 静态紧密数组, 先分配空间, 再一个一个赋值, 时间复杂度和长度有关, O(n)

# 比较
print(s1.islower())  # 遍历数组, 最好O(1), 最差O(n), 平均O(n)
print(s1 > "hello")  # 最差需要遍历完短的那个, O(n短)

# 样例匹配, __contains__, find, index, count, replace, split, 其实都依赖于模式匹配, 即找子串
print('ll' in s1)  # True
print(s1.find("ld"))  # 9
print(s1.index("ld"))  # 9
print(s1.count('ld'))  # 1
print(s1.replace('ld', '**'))  # **
print(s1.split("or"))  # ['hello w', 'ld']
# 最简单的模式匹配思路是一个个遍历, 分别以n-m+1为起始, 往后找m个元素, 看一不一样
def f(s, sub):
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1
print(f(s1, "or"))  # 7
# 第一个优化思路是大跳, 比如hello world, lla, 匹配到o的时候, 看o在不在lla里, 不在, 大跳
def f(s, sub):
    l1, l2, d = len(s), len(sub), set(sub)

    pos = 0

    # 0, 1, 2, 3, 4, 5; 2, 要到4
    while pos <= l1-l2:

        for i in range(l2):
            if s[pos+i] != sub[i]:
                if s[pos+i] in d:
                    pos += 1
                else:
                    pos = pos+i+1
                break
        # 这里的else用的就很巧妙, 内层break只能退出内层
        # 不用else, 这里无法判断内层是执行完出来的还是break出来的
        else:
            return pos
    return -1
print(f(s1, "ooo"))
# 上面第一种优化思路只是增加了大跳, 实际上还有其他情况也可以跳, 即KMP算法
"""
    KMP算法, 一种改进的字符串匹配算法, 可以在O(n+m)的时间复杂度上完成串的模式匹配
    其基本思想是, 每当匹配过程中出现字符不相同时, 不需要回溯指针, 而是利用已经得到的
    部分匹配结果, 将模式整体右滑尽可能远的一段距离
    
    lloword
    lle
    传统的算法, e匹配不上, 模式串移动一位, 然后从头开始比较
    
    KMP算法, 引入了一个叫next数组的概念
    
    ababcabcacbab
      abcac, -1, 0, 0, 0, 1, 该位置元素前面的元素最大前后同后缀
    
    abca部分都匹配上了, b-c没匹配上, 对应next值为1, 即abca的最大前后缀公共部分a
    注意最大不光意味着a-a相等, 也意味着ab != ca, abc != bca
    
    再观察移动和这里的不等式的关系
    
    ab-abca-bcacbab  ->  ab-abca-bcacbab
       abca-c                abca-c
    首先, 匹配到了b-c, 说面前面的abca是匹配上的
    如果模式串移动1位, 意味着拿上面abca的的3位后缀和下面abca的3位前缀去做比较
    
    然而, 既然c的next值是1, 说明这里是匹配不上的, 不然next值就是3了
    
    移动2位同理
    
    应该移动的位数, 4-1 = 3
    
    
"""

def f(s, p):

    # 先计算p的next
    next = [0]*len(p)
    # next[0], next[1]恒定为0, 从next[2]开始算就行
    # 琢磨这里算next的方法, 比如ABCDA-B, S算B的时候A==A, 即1
    # ABCDAB-D, 算D的时候, 要借助next[B]的结果, 左指针指向A的下一个位置即左B
    # 右指针指向D的前一个位置, 如果相等, 则next[D] = next[B]
    # 如果不相等, 则next[D] = 0, 同时左指针归位到最头部, 归位这个动作千万不要忽略了!
    pos = 0
    for i in range(2, len(p)):
        if p[pos] == p[i-1]:
            next[i] = next[i-1]+1
            pos += 1
        else:
            next[i] = 0
            pos = 0
    print(next)

    # next算完就开始匹配了, 注意, p右移反应到代码上相当于指向p的指针左移(保持指向s的指针不回退)
    t, b = 0, 0
    # 上下指针都没超限
    while t <= len(s)-1 and b <= len(p)-1:
        # 相等, 上下指针都右移, 这个没有疑问
        if s[t] == p[b]:
            t, b = t+1, b+1
        else:
            # 不相等的时候, 怎么移动就是个问题了
            # 第一种情况, p第一个就没匹配上, t右移就行
            # 第二种情况, 中间没匹配上, 这时候前面子串长度b, 公共缀长度next[b]
            # 移动长度=b-next[b], 最终索引 b-(b-next[b]) = next[b]
            if b == 0:
                # 这里, 如果前面设置next[0] = -1, t = t+1可以写到上面那个if里去, 更简洁, 更难理解
                t = t+1
            else:
                b = b-(b-next[b])

    return t-len(p) if b > len(p)-1 else -1

print(f('BBC ABCDAB ABCDABCDABDE', 'ABCDABD'))
print(f('ababcabcacbab', 'abcac'))
"""
ababcabcacbab
abcac
"""
