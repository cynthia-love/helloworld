# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    模拟生态系统, 包含两种动物熊和鱼, 还包含一条河流, 用列表实现
    列表中的每一个元素可能为Bear, Fish, None
    在每一个时间步长, 基于随机过程, 每一个动物都试图进入一个相邻
    的列表位置或停留在原处, 如果两只同类竞争同一单元格, 停留在原处
    并在列表为None的地方随机生成一个同类型对象, 如果竞争的是Bear
    和Fish, 则Fish消失. 条件1高于条件2, 比如鱼熊鱼, 移动1,0,-1
    结果是都不动, 不会有鱼被吃; 但左鱼和右鱼由于有竞争关系, 新的
    小鱼仔还是会出生的

"""
"""
    分析
    直接按题目描述的那样去实现, 首先想到的是把river设置为一个普通list
    每一个索引位置随机初始化为Bear, Fish, None
    但这么设计有个问题, 怎么移动, 以及移动后怎么判断碰撞都无从下手
    结合pygame里精灵的概念, 重新设计如下:
    1. 确定索引范围(类似pygame里的屏幕大小)
    2. 确定初始熊和鱼的数量, 并一个个初始化, 保证两两无碰撞
    3. 全部随机移动一次, 先处理条件1, 即同类不碰撞, 如果碰了则回退, 回退
    完还是有同类碰撞, 继续回退(为了实现只回退一次的效果, 需要对animal的unmove
    函数做特殊处理); 注意把第一次同类碰撞的数量记下来, 后面繁殖要用
    4. 同类无冲突后, 再去判断是否有鱼熊碰撞, 有的话把鱼吃掉
    
"""
import random
from typing import List

SIZE = 100
COUNT_BEAR = 3
COUNT_FISH = 20

class Animal:
    def __init__(self):
        self.pos = random.randrange(SIZE)
        self.step = None

    def rand(self):
        self.pos = random.randrange(SIZE)

    def move(self):
        # 最左边和最右边只有两个选择
        if self.pos == 0:
            step = random.choice([0, 1])
        elif self.pos == SIZE-1:
            step = random.choice([0, -1])
        else:
            step = random.choice([0, -1, 1])

        self.pos += step
        self.step = step

    def unmove(self):
        if self.step is not None:
            self.pos -= self.step
            self.step = None  # 只允许回退一步

class Bear(Animal):
    pass

class Fish(Animal):
    pass

def collide(animal1: Animal, animal2: Animal):
    if animal1 is animal2:
        return False
    if animal1.pos == animal2.pos:
        return True
    return False

def collideAny(animal: Animal, target: List[Animal]):
    for each in target:
        if each is animal: continue  # 1对多需要忽略自己和自己
        if animal.pos == each.pos:
            return True
    return False

river = []
bears = []  # 熊和鱼再单独存一个是为了简化后续碰撞逻辑
fishes = []

# 初始化
for _ in range(COUNT_BEAR):
    bear = Bear()
    while collideAny(bear, river):
        bear.rand()

    river.append(bear)
    bears.append(bear)

for _ in range(COUNT_FISH):
    fish = Fish()
    while collideAny(fish, river):
        fish.rand()

    river.append(fish)
    fishes.append(fish)

# 主循环, 每一个时间步长进行一次随机过程
while True:
    print(len(bears), len(fishes))

    """除了题目要求, 其实还可以加一个熊饿死条件
    不然哪怕初始熊再少, 假以时日, 也会吃光鱼的
    while len(fishes) / len(bears) <= 10:
        # 假定, 生态系统中鱼熊比至少10:1, 不然就会有熊饿死
        # 加这个是为了限制熊的数量, 避免把鱼吃绝
        bear = random.choice(bears)
        print("a bear died")
        bears.remove(bear)
        river.remove(bear)
    """

    # 先不管碰撞, 全部移动一次
    for each in river:
        each.move()

    # 熊和熊之间碰撞了
    b2b = []
    # 这里没有直接用1对多碰撞是因为存在3个一起的情况导致len(b2b)为奇数
    for e1 in bears:
        for e2 in bears:
            if e1 == e2: continue
            if collide(e1, e2):
                b2b.append(e1)

    # 鱼和鱼之间碰撞了
    f2f = []
    for e1 in fishes:
        for e2 in fishes:
            if e1 == e2: continue
            if collide(e1, e2):
                f2f.append(e1)

    # 幼崽数量要在这里计算, 因为并不是没动
    # 而是实际上动了->繁殖->再回原位置
    inc_bear = len(b2b) // 2
    inc_fish = len(f2f) // 2

    # 如果有同类碰撞, 回撤, 回撤后还是碰撞, 继续回撤
    # 由于unmove里有控制, 所以多次循环也不会回撤越过原位置
    while b2b or f2f:
        for each in b2b:
            each.unmove()

        for each in f2f:
            each.unmove()

        # 熊和熊之间碰撞了
        b2b = []
        for e1 in bears:
            for e2 in bears:
                if e1 == e2: continue
                if collide(e1, e2):
                    b2b.append(e1)

        # 鱼和鱼之间碰撞了
        f2f = []
        for e1 in fishes:
            for e2 in fishes:
                if e1 == e2: continue
                if collide(e1, e2):
                    f2f.append(e1)

    # 鱼和熊之间的碰撞要放在同类碰撞处理完成后
    # 因为鱼最终是和没碰撞的熊+碰了回到原位置的熊进行碰撞检测
    f2b = []
    for each in fishes:
        if collideAny(each, bears):
            f2b.append(each)

    # 熊和鱼碰到了, 吃掉
    for each in f2b:
        print("a fish ate")
        fishes.remove(each)
        river.remove(each)

    # 如果熊和鱼同时达到繁殖条件, 优先熊
    for _ in range(inc_bear):
        if len(river) == SIZE:
            break  # 如果生态系统满了, 不繁殖了
        bear = Bear()
        while collideAny(bear, river):
            bear.rand()
        print("a new bear born")
        bears.append(bear)
        river.append(bear)

    for _ in range(inc_fish):
        if len(river) == SIZE:
            break
        fish = Fish()
        while collideAny(fish, river):
            fish.rand()
        print("a new fish born")
        fishes.append(fish)
        river.append(fish)
