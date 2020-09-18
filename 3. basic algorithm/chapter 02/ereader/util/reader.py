# -*- coding:utf-8 -*-
# Author: Cynthia
from util.dao import reader_handler as rh
from util.dao import book_handler as bh
from util.dao import shelf_handler as sh
from util.dao import history_handler as hh

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
@Singleton
class Reader:
    def __init__(self):
        self.login_name = None

    def is_login(self):
        return True if self.login_name else False

    def get_user(self):
        # log里用这个方法获取用户名, 所以这里不能@common.log, 不然会死循环
        return self.login_name

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
        i, title, p, f = bh.get_info(bookid)
        l, pwd, b = rh.get_info(self.login_name)

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
        return hh.get(self.login_name, bookid)

    def save_pos(self, bookid, pos):
        state = hh.save(self.login_name, bookid, pos)
        return state

