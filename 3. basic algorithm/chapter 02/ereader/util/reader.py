# -*- coding:utf-8 -*-
# Author: Cynthia
from util.dao import reader_handler as rh
from util.dao import book_handler as bh
from util.dao import shelf_handler as sh
from util.dao import history_handler as hh

# 单例装饰器, Reader = Singleton(Reader)
# 实例化Reader的时候实际上是执行Singleton的实例的__call__方法
# 即用Singleton的实例去实例化Reader
# 装饰多个类时, 每个类对应一个Singleton的实例
# 这么看来, _instance其实没必要声明为dict
# 要么也可以把_instance提成类变量, 但没必要, 享元模式里才会那么写, 且是直接改类, 而不是外层装饰器
class Singleton:
    def __init__(self, cls):
        self._instance = {}
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if self._cls.__name__ in self._instance:
            res = self._instance[self._cls.__name__]
        else:
            res = self._cls(*args, **kwargs)
            self._instance[self._cls.__name__] = res

        return res

# Reader置为单例, 全局唯一, 有点类似Session或Context
"""
    理解decorator的机制
    @ClassA
    ClassB
    实际上运行之前, 就执行了ClassB = ClassA(ClassB)(装饰后无法再直接访问到classB)
    o = ClassB()实际上是ClassA(ClassB)()
    即执行装饰器的instance的__call__函数
    o = ClassA(classB)() = ...
    
    当然, 还有一种写法
    @ClassA()
    ClassB
    无非是多了一级
    ClassB = ClassA()(ClassB)
    o = ClassB() = ClassA()(ClassB)(), 那么__call__里就得再嵌一级wrapper了
    外层__call__参数是func, 内层wrapper参数是 *args, **kwargs
    
"""
@Singleton
class Reader:
    def __init__(self):
        self.login_name = None

    def is_login(self):
        return True if self.login_name else False

    def get_user(self):
        # log里用这个方法获取用户名, 所以这里不能@common.log, 不然会死循环
        return self.login_name

    # 其实这里可以声明static, 但带装饰器的类写static方法会报错, 暂时还没找到解决办法
    def register(self):
        login_name = input('请输入用户名: ').strip()
        reader_info = rh.get_info(login_name)
        if reader_info:
            print("用户名已存在, 请重新指定!")
            return False
        password1 = input("请输入密码: ").strip()
        password2 = input("请确认密码: ").strip()
        if password1 != password2:
            print("两次密码不不一致, 请重新注册!")
            return False

        rh.add_reader(login_name, password1)
        print("注册成功")
        return True

    def login(self):
        login_name = input("请输入用户名: ").strip()

        reader_info = rh.get_info(login_name)
        if not reader_info:
            print('用户名不存在!')
            return False
        password = input("请输入密码: ").strip()
        if password != reader_info[1]:
            print('密码错误!')
            return False
        print('登陆成功!')
        self.login_name = login_name
        return True

    def recharge(self, val):
        state = rh.recharge(self.login_name, val)
        return state

    def charge(self, val):
        state = rh.charge(self.login_name, val)
        return state

    def buy(self, bookid):
        shelf = sh.get_list(self.login_name)
        for bid, name, price, url in shelf:
            if bid == bookid:
                return False  # 如果书架里已经有了, 则不让买

        i, title, p, f = bh.get_info(bookid)  # 获取最新价格, 当然价格也可以前端传
        l, pwd, b = rh.get_info(self.login_name)  # 获取当前余额

        p, b = float(p), float(b)

        if p > b:
            return False
        else:
            state = self.charge(p)
            if not state: return False
            sh.add(self.login_name, bookid)
            return True

    def get_shelf(self):
        book_list = sh.get_list(self.login_name)
        return book_list

    def logout(self):
        self.login_name = None

    def get_pos(self, bookid):
        """
        获取特定客户读目标书籍的进度
        :param bookid:
        :return:
        """
        return hh.get(self.login_name, bookid)

    def save_pos(self, bookid, pos):
        """
        更新进度
        :param bookid:
        :param pos:
        :return:
        """
        state = hh.save(self.login_name, bookid, pos)
        return state

