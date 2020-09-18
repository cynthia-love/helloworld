# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import os
import settings

def get_list():
    """
    查询库存小说列表
    :return: 库存小说列表, 列表项格式(小说ID, 小说名, 价格, 文件名)
    """
    res = []
    with open(settings.DB_PATH_BOOK, 'r', encoding='utf-8') as f:
        for line in f:
            i, t, p, f = line.strip().split(':')
            res.append((i, t, float(p), f))
    return res

def get_info(bookid):
    """
    查询单本书的详细信息
    :param bookid:
    :return: 小说ID, 小说名, 价格, 文件名, 找不到则返回None
    """
    with open(settings.DB_PATH_BOOK, 'r', encoding='utf-8') as f:
        for line in f:
            i, t, p, f = line.strip().split(':')
            if bookid == i:
                return i, t, float(p), f

def get_content(file):
    """
    根据文件名返回文件全部内容
    :param file:
    :return: 文件内容
    """
    with open(os.path.join(settings.BOOK_PATH, file), 'r', encoding='utf-8') as f:
        content = f.read()
        return content

def get_lines(file, start):
    """
    根据文件名, 起始行, 返回起始行开始共settings.PAGE_LINE行内容
    :param file: 文件名
    :param start: 起始行, 首行编号为1
    :return: 指定范围内的内容
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