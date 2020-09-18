# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import settings

def add_reader(login_name, password, balance=0):
    """
    增加一条用户记录, 格式, 用户名:密码:余额
    这里没有控制重复, 需要在调用函数那控制
    实际项目中会设置数据库主键/unique约束, 不会存在此问题
    :param login_name:
    :param password:
    :param balance: 默认0
    :return:
    """
    with open(settings.DB_PATH_READER, 'a', encoding='utf-8') as f:
        f.write("{}:{}:{}\n".format(login_name, password, balance))

def get_info(login_name):
    """
    根据用户名获取用户的密码和余额, 查不到返回None
    :param login_name:
    :return:
    """
    with open(settings.DB_PATH_READER, 'r', encoding='utf-8') as f:
        for line in f:
            n, p, b = line.strip().split(':')
            if login_name == n:
                return n, p, float(b)

def update_password(login_name, password):
    """
    更新用户的密码, 取出原信息, 遍历行, 目标用户行修改密码后拼接, 其他行直接拼接
    :param login_name:
    :param password:
    :return:
    """
    data = ""
    with open(settings.DB_PATH_READER, 'r', encoding='utf-8') as f:
        for line in f:
            n, p, b = line.strip().split(':')
            if n == login_name:
                p = password
            data += "{}:{}:{}\n".format(n, p, b)

    with open(settings.DB_PATH_READER, 'w') as f:
        f.truncate()  # 清空原数据
        f.write(data)

def update_balance(login_name, balance):
    """
    更新余额, 逻辑同更新密码
    :param login_name:
    :param balance:
    :return:
    """

    data = ""
    with open(settings.DB_PATH_READER, 'r', encoding='utf-8') as f:
        for line in f:
            n, p, b = line.strip().split(':')
            if n == login_name:
                b = balance
            data += "{}:{}:{}\n".format(n, p, b)

    with open(settings.DB_PATH_READER, 'w', encoding='utf-8') as f:
        f.truncate()
        f.write(data)

# 扣费函数存在扣款失败的情况
def charge(login_name, val):
    """

    :param login_name:
    :param val:
    :return:
    """
    n, p, b = get_info(login_name)  # 先查询用户当前余额
    b = float(b)
    if val > b: return False
    update_balance(login_name, b-val)
    return True

def recharge(login_name, val):
    n, p, b = get_info(login_name)  # 先查询用户当前余额
    b = float(b)
    update_balance(login_name, b+val)
    return True