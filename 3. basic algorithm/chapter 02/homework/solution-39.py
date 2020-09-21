# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    基类: Polygon, 有两个方法, 求周长和面积, 以及判断两个多边形是否相似
    扩展基类得到Triangle, Quadrilateral, Pentagon, Hexagon, Octagon
    再扩展IsoscelesTriangle, EquilateralTriangle, Rectangle, Square

"""
"""
    小技巧, 多边形面积计算转换成多个三角形面积计算加和
    而三角形面积: 
    1/2|x1y2+x2y3+x3y1-x1y3-x2y1-x3y2|
    = 1/2*abs(
            x1 y1 1
            x2 y2 1
            x3 y3 1 的行列式)
"""
from typing import List
from decimal import Decimal
from abc import ABCMeta, abstractmethod

class Polygon(metaclass=ABCMeta):
    def __init__(self):
        self.nodes = []
        self.edges = []

    # 其实周长和面积没必要声明为抽象方法, 因为可以有通用计算方式
    # 不过既然题目要求了, 那就设为抽象吧, 不过基类提供cal_perimeter和cal_area方法
    @abstractmethod
    def perimeter(self):
        """周长"""

    @abstractmethod
    def area(self):
        """面积"""

    def cal_perimeter(self):
        return sum(self.edges)

    def cal_area(self):
        # 将多边形拆分三角形, 比如ABCDEFGH
        # 实际上是求: ABC, ACD, ADE, AEF, AFG, AGH, 六个三角形的面积和
        # 求单个三角形利用行列式1/2*abs(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
        res = 0
        for i in range(1, len(self)-1):
            x1, y1 = self.nodes[0]
            x2, y2 = self.nodes[i]
            x3, y3 = self.nodes[i+1]
            area = Decimal('0.5')*abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2)
            res += area

        return res

    # 要求输入的顶点按顺序来
    def set_nodes(self, nodes: List[tuple]):
        self.nodes = nodes
        for i in range(len(self.nodes)):
            j = (i+1) % len(self.nodes)
            x1, y1 = self.nodes[i][0], self.nodes[i][1]
            x2, y2 = self.nodes[j][0], self.nodes[j][1]
            dis = ((x1-x2)**2+(y1-y2)**2)**Decimal('0.5')
            self.edges.append(dis)

    def __len__(self):
        return len(self.edges)

    def is_similar(self, other):
        if not isinstance(other, Polygon):
            raise TypeError

        if len(self) != len(other):
            raise ValueError

        # 注意这里对于比值的要求很高, 差一点就不相等
        # 所以普通的float就不满足要求了, 得用精度更高的Decimal
        # x = 1.1存的不是1.1, 而是和接近1.1的一个浮点数, x = Decimal('1.1')存的才是1.1
        # 除了用Decimal, 还可以修改判断相等条件, 用容忍误差的math.isclose(a, b, rel_tol=xx)
        ratio = other.perimeter()/self.perimeter()

        # 求相似要注意, 由于输入的顶点不一定从哪个开始, 所以
        # 这里要转一圈, 都不相似才认为不相似, 转第一个, 第二个始终从0开始
        # 比如第一个从1开始, 那么第二个0号边和第一个1号比, 第二个1号和第一个2号比
        for i in range(len(self)):
            similar = True
            for j in range(len(other)):
                ratio_edge = other.edges[j] / self.edges[(i+j) % len(self)]
                if ratio_edge != ratio:
                    similar = False
                    break
            if similar: return True

        return False

# 三角形
class Triangle(Polygon):
    def set_nodes(self, nodes: List[tuple]):
        if len(nodes) != 3:
            raise ValueError
        super().set_nodes(nodes)

    def perimeter(self):
        return self.cal_perimeter()

    def area(self):
        return self.cal_area()


# 四边形
class Quadrilateral(Polygon):
    def set_nodes(self, nodes: List[tuple]):
        if len(nodes) != 4:
            raise ValueError
        super().set_nodes(nodes)

    def perimeter(self):
        return self.cal_perimeter()

    def area(self):
        return self.cal_area()

# 五边形
class Pentagon(Polygon):
    def set_nodes(self, nodes: List[tuple]):
        if len(nodes) != 5:
            raise ValueError
        super().set_nodes(nodes)

    def perimeter(self):
        return self.cal_perimeter()

    def area(self):
        return self.cal_area()

# 六边形
class Hexagon(Polygon):
    def set_nodes(self, nodes: List[tuple]):
        if len(nodes) != 6:
            raise ValueError
        super().set_nodes(nodes)

    def perimeter(self):
        return self.cal_perimeter()

    def area(self):
        return self.cal_area()

# 八边形
class Octagon(Polygon):
    def set_nodes(self, nodes: List[tuple]):
        if len(nodes) != 8:
            raise ValueError
        super().set_nodes(nodes)

    def perimeter(self):
        return self.cal_perimeter()

    def area(self):
        return self.cal_area()

# 等腰三角形
class IsoscelesTriangle(Triangle):
    def set_nodes(self, nodes: List[tuple]):
        super().set_nodes(nodes)
        # 这里要先调父类的set_nodes, 因为判断条件要用到边
        flag = False
        for i in range(len(self)):
            for j in range(i+1, len(self)):
                if self.edges[i] == self.edges[j]:
                    flag = True
        if not flag: raise ValueError("非等腰三角形")

# 等边三角形
class EquilateralTriangle(Triangle):
    def set_nodes(self, nodes: List[tuple]):
        super().set_nodes(nodes)
        flag = True
        for i in range(1, len(self)):
            if self.edges[i] != self.edges[0]:
                flag = False
        if not flag: raise ValueError("非等边三角形")

# 矩形
class Rectangle(Quadrilateral):
    def set_nodes(self, nodes: List[tuple]):
        super().set_nodes(nodes)
        # 其实这里已经确定了形状, 直接比较就行, 不用写通用判断形式
        if self.edges[0] != self.edges[2]:
            raise ValueError("非矩形")
        if self.edges[1] != self.edges[3]:
            raise ValueError("非矩形")

# 正方形
class Square(Quadrilateral):
    def set_nodes(self, nodes: List[tuple]):
        super().set_nodes(nodes)
        if not self.edges[0] == self.edges[1] == self.edges[2] == self.edges[3]:
            raise ValueError("非正方形")

o1 = Triangle()
o1.set_nodes([
    (Decimal("0"), Decimal("0")),
    (Decimal("1.1"), Decimal("0")),
    (Decimal('0'), Decimal("1.1"))
])


o2 = Triangle()
o2.set_nodes([
    (Decimal("0"), Decimal("0")),
    (Decimal("1.8"), Decimal("0")),
    (Decimal('0'), Decimal("1.8"))
])
print(o1.perimeter(), o1.area())
print(o1.is_similar(o2))

o3 = Square()
o3.set_nodes([
    (Decimal('1'), Decimal('1')),
    (Decimal('1'), Decimal('2')),
    (Decimal('2'), Decimal('2')),
    (Decimal('2'), Decimal('1')),
])
print(o3.perimeter(), o3.area())
