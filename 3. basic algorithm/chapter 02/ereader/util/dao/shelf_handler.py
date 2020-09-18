# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import settings
from util.dao import book_handler as bh

def get_list(login_name):
    """

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

    :param login_name:
    :param bookid:
    :return:
    """
    with open(settings.DB_PATH_SHELF, 'a', encoding='utf-8') as f:
        f.write("{}:{}\n".format(login_name, bookid))

def delete(login_name, bookid):
    """

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



