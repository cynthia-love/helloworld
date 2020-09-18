# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import settings
from util.dao import book_handler as bh

def get_list(login_name):
    """
    查询用户已购买的所有书籍
    :param login_name:
    :return:
    """
    res = []
    with open(settings.DB_PATH_SHELF, 'r', encoding='utf-8') as f:
        for line in f:
            n, i = line.strip().split(':')
            if n == login_name:
                i, t, p, f = bh.get_info(i)
                res.append((i, t, float(p), f))
        return res

def add(login_name, bookid):
    """
    往书架添加新的书籍
    :param login_name:
    :param bookid:
    :return:
    """
    # 如果书籍已存在, 则什么都不做
    # 实际项目中会把login_name, bookid设置为主键
    # 且入口处就会查书籍是不是可购买状态, 根本就不会调到此函数
    res = get_list(login_name)
    for i, t, p, f in res:
        if i == bookid:
            return

    with open(settings.DB_PATH_SHELF, 'a', encoding='utf-8') as f:
        f.write("{}:{}\n".format(login_name, bookid))

def delete(login_name, bookid):
    """
    删除书架上的某本书
    :param login_name:
    :param bookid:
    :return:
    """
    res = ""
    with open(settings.DB_PATH_SHELF, 'r', encoding='utf-8') as f:
        for line in f:
            n, i = line.strip().split(':')
            if n == login_name and i == bookid:
                continue
            res += line

    with open(settings.DB_PATH_SHELF, 'w', encoding='utf-8') as f:
        f.truncate()
        f.write(res)



