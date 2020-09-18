# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    实现一个电子阅读器
    数据库采用本地文件模拟
"""
import os
import sys
import settings
from util import common
from util.book import Book
from util.reader import Reader
from util.dao import reader_handler as rh
from util.dao import book_handler as bh
from util.dao import shelf_handler as sh
from util.dao import history_handler as hh

reader = Reader()

# 注册
@common.log
def register():
    """

    :return:
    """
    while True:
        state = reader.register()
        if state: return state

# 主动登陆
@common.log
def login():
    while True:
        state = reader.login()
        if state: return state

# 注意这里的双层decorator, 先下面的再上面的
# 另外, 注意装饰器在@的时候就会执行第一层里的代码(所以才会包一个wrapper)
# 所以一些判断条件什么的不能写在外层
@common.log
@common.auth
def recharge():
    """

    :param val:
    :return:
    """
    while True:
        amount = input("请输入充值金额: ").strip()
        if not amount.isdigit():
            print("请输入数字")
            continue

        state = reader.recharge(float(amount))
        if state: return state

@common.log
@common.auth
def buy():
    """

    :return:
    """
    book_list = Book.get_list()
    id_list = [x[0] for x in book_list]
    for bookid, name, price, url in book_list:
        print("小说编号[{}], 小说名[{}], 小说价格[{}]".format(bookid, name, price))

    while True:
        cmd = input('请输入您想购买的小说编号, 输入q退出: ').strip()
        if cmd == 'q': return
        if cmd not in id_list:
            print("请输入正确的编号")
            continue
        state = reader.buy(cmd)
        if state:
            print("购买成功!")
        else:
            print("余额不足, 请充值!")

@common.log
@common.auth
def read():
    book_list = reader.get_shelf()
    id_list = [x[0] for x in book_list]
    for bookid, name, price, url in book_list:
        print("小说编号[{}], 小说名[{}]".format(bookid, name))

    cmd = input("请输入要阅读的小说编号: ").strip()
    if cmd not in id_list:
        print("请输入正确的编号")
        return

    bookid, name, price, url = book_list[id_list.index(cmd)]
    book = Book(bookid, name, url)

    pos = reader.get_pos(book.bookid)

    while True:
        data = book.get_lines(pos)
        print(data)
        cmd = input("输入p上一页, 输入n下一页, 输入q退出阅读: ").strip()
        if cmd == 'q':
            return
        elif cmd == 'n':
            pos += settings.PAGE_LINE
            reader.save_pos(book.bookid, pos)

        elif cmd == 'p':
            pos = max(1, pos-settings.PAGE_LINE)
            reader.save_pos(book.bookid, pos)

def logout():
    reader.logout()
    sys.exit()

def main():

    while True:
        print("""
=====欢迎来到电子阅读器=====
        0 注册
        1 登陆
        2 充值
        3 购买
        4 阅读
        q 登出
==========================
        """)
        cmd = input().strip()
        if cmd == '0': register()
        elif cmd == '1': login()
        elif cmd == '2': recharge()
        elif cmd == '3': buy()
        elif cmd == '4': read()
        else: logout()


if __name__ == '__main__':
    main()