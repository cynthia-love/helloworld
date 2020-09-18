# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import os
import settings
# 进度的添加比较特殊, 必须保证唯一
# 所以是不是首次添加都得先查一下
# 当然, 除了这种思路, 还可以不唯一, 多存个时间戳字段, 查找记录时从后往前找最新的
def save(login_name, bookid, pos):
    """
    更新阅读记录
    :param login_name:
    :param bookid:
    :param pos:
    :return:
    """
    res = ""
    # 先遍历老记录, 把同用户名-小说编号的行过滤掉
    if os.path.exists(settings.DB_PATH_HISTORY):
        with open(settings.DB_PATH_HISTORY, 'r', encoding='utf-8') as f:
            for line in f:
                n, b, p = line.strip().split(':')
                if login_name == n and bookid == b:
                    continue
                else:
                    res += line

    # 然后添加上最新的记录
    res += "{}:{}:{}\n".format(login_name, bookid, pos)

    with open(settings.DB_PATH_HISTORY, 'w', encoding='utf-8') as f:
        f.truncate()  # 清空原数据
        f.write(res)

    return True

def get(login_name, bookid):
    """
    查询某人阅读某书的记录
    :param login_name:
    :param bookid:
    :return: 有记录则返回起始行, 否则返回1
    """
    with open(settings.DB_PATH_HISTORY, 'r', encoding='utf-8') as f:
        for line in f:
            n, i, p = line.strip().split(':')
            if n == login_name and i == bookid:
                return int(p)
        return 1