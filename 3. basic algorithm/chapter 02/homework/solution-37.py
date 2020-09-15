# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    在第36题的基础上, 给动物增加性别和力量值属性, 力量值为浮点数
    不同性别碰到才会产子后会到原位置, 同性别碰到力量值大的生存(即吃的效果)
    同样, 会遇到同物种三个一起的情况, 需要确定处理规则
    公母公, 母公母, 公母母, 母公公
    约定生殖 > PK, 比如公母公, 生俩, 母公母生俩, 公母母, 生一个, 左边公的不动,
    右边母的左移和中间的母的PK活一个

    另外, 尝试一下实现多对多碰撞检测函数
"""

import random
from typing import List

SIZE = 100
COUNT_BEAR = 5
COUNT_FISH = 60

class Animal:
    def __init__(self):
        self.gender = random.choice(['male', 'female'])
        self.strength = random.random()
        self.pos = random.randrange(SIZE)
        self.step = None

    def rand(self):
        self.pos = random.randrange(SIZE)

    def move(self):
        if self.pos == 0:
            step = random.choice([0, 1])
        elif self.pos == SIZE-1:
            step = random.choice([0, -1])
        else:
            step = random.choice([0, -1, 1])

        self.pos += step
        self.step = step

    def unmove(self):
        # step有0的情况, 不能直接判断
        if self.step is not None:
            self.pos -= self.step
            self.step = None

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

def collide_any(animal: Animal, target: List[Animal]):
    for each in target:
        if each is animal: continue
        if animal.pos == each.pos:
            return True
    return False

def collide_group(animals1: List[Animal], animals2: List[Animal]):
    res = []

    for e1 in animals1:
        for e2 in animals2:
            if e2 is e1: continue
            if (e2, e1) in res: continue
            if e1.pos == e2.pos:
                res.append((e1, e2))

    return res

river = []

for _ in range(COUNT_BEAR):
    bear = Bear()
    while collide_any(bear, river):
        bear.rand()

    river.append(bear)

for _ in range(COUNT_FISH):
    fish = Fish()
    while collide_any(fish, river):
        fish.rand()

    river.append(fish)

def show():
    bm, bf, fm, ff = 0, 0, 0, 0
    for each in river:
        if isinstance(each, Bear):
            if each.gender == 'male':
                bm += 1
            else: bf += 1

        else:
            if each.gender == 'male':
                fm += 1
            else: ff += 1

    print("公熊: {}, 母熊: {}, 公鱼: {}, 母鱼: {}".format(bm, bf, fm, ff))

while True:
    show()

    col = collide_group(river, river)
    # 几种不动的情况: 公母熊, 公母鱼, 同力量公公/母母
    # 还是类似36中的思路, 先让不动的达到稳定态
    for each in river:
        each.move()

    col = collide_group(river, river)

    bear_dif_sex = []
    fish_dif_sex = []
    bear_same_sex_stren = []
    fish_same_sex_stren = []

    for e1, e2 in col:
        if isinstance(e1, Bear) and isinstance(e2, Bear):
            if e1.gender != e2.gender:
                bear_dif_sex.append((e1, e2))
            elif e1.strength == e2.strength:
                bear_same_sex_stren.append((e1, e2))
        elif isinstance(e1, Fish) and isinstance(e2, Fish):
            if e1.gender != e2.gender:
                fish_dif_sex.append((e1, e2))
            elif e1.strength == e2.strength:
                fish_same_sex_stren.append((e1, e2))

    inc_bear = len(bear_dif_sex)
    inc_fish = len(fish_dif_sex)

    while bear_dif_sex or fish_dif_sex or bear_same_sex_stren or fish_same_sex_stren:

        for e1, e2 in bear_dif_sex:
            e1.unmove()
            e2.unmove()

        for e1, e2 in fish_dif_sex:
            e1.unmove()
            e2.unmove()

        for e1, e2 in bear_same_sex_stren:
            e1.unmove()
            e2.unmove()

        for e1, e2 in fish_same_sex_stren:
            e1.unmove()
            e2.unmove()

        col = collide_group(river, river)

        bear_dif_sex = []
        fish_dif_sex = []
        bear_same_sex_stren = []
        fish_same_sex_stren = []

        for e1, e2 in col:
            if isinstance(e1, Bear) and isinstance(e2, Bear):
                if e1.gender != e2.gender:
                    bear_dif_sex.append((e1, e2))
                elif e1.strength == e2.strength:
                    bear_same_sex_stren.append((e1, e2))
            elif isinstance(e1, Fish) and isinstance(e2, Fish):
                if e1.gender != e2.gender:
                    fish_dif_sex.append((e1, e2))
                elif e1.strength == e2.strength:
                    fish_same_sex_stren.append((e1, e2))

    # 处理完不动的再处理要生产的和要吃的, 先生再吃

    # 如果熊和鱼同时达到繁殖条件, 优先熊
    for _ in range(inc_bear):
        if len(river) == SIZE:
            break  # 如果生态系统满了, 不繁殖了
        bear = Bear()
        while collide_any(bear, river):
            bear.rand()
        river.append(bear)

    for _ in range(inc_fish):
        if len(river) == SIZE:
            break
        fish = Fish()
        while collide_any(fish, river):
            fish.rand()
        river.append(fish)

    # 生产的都是占用空地, 不会对碰撞检测产生影响
    col = collide_group(river, river)

    die = set()
    for e1, e2 in col:
        if isinstance(e1, Bear) and isinstance(e2, Bear):
            if e1.gender == e2.gender:
                if e1.strength > e2.strength:
                    die.add(e2)
                if e1.strength < e2.strength:
                    die.add(e1)
        elif isinstance(e1, Fish) and isinstance(e2, Fish):
            if e1.gender == e2.gender:
                if e1.strength > e2.strength:
                    die.add(e2)
                if e1.strength < e2.strength:
                    die.add(e1)

        elif isinstance(e1, Bear) and isinstance(e2, Fish):
            die.add(e2)
        else: die.add(e1)

    for each in die: river.remove(each)

