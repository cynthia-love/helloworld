# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import os
import settings

def get_list():
    """

    :return:
    """
    res = []
    with open(settings.DB_PATH_BOOK, 'r', encoding='utf-8') as f:
        for line in f:
            i, t, p, f = line.strip().split(':')
            res.append((i, t, float(p), f))
    return res

def get_info(bookid):
    """

    :param bookid:
    :return:
    """
    with open(settings.DB_PATH_BOOK, 'r', encoding='utf-8') as f:
        for line in f:
            i, t, p, f = line.strip().split(':')
            if bookid == i:
                return i, t, float(p), f

def get_content(file):
    """

    :param file:
    :return:
    """
    with open(os.path.join(settings.BOOK_PATH, file), 'r', encoding='utf-8') as f:
        content = f.read()
        return content

def get_lines(file, start):
    """

    :param start:
    :param limit:
    :return:
    """
    res = ""
    with open(os.path.join(settings.BOOK_PATH, file), 'r', encoding='utf-8') as f:
        mark = 0
        for l in f:
            mark += 1
            if mark < start:
                continue
            if mark >= start+settings.PAGE_LINE:
                break
            res += l
    return res