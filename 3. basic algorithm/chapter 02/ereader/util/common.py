# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""

import time
import settings

def log(func):
    """

    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        # 如果reader和common存在相互引用, import不能放在上面
        # 当然, 最好的方式是不要有相互引用, 不要直接在reader里@log, @auth
        from util.reader import Reader
        res = func(*args, **kwargs)
        now = time.strftime('%Y-%m-%d %X')
        # 记录内容为时间, 用户名, 操作名, 返回值
        data = "{}|{}|{}|{}\n".format(now, Reader().get_user(), func.__name__, res)
        with open(settings.LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(data)

        return res

    return wrapper

def auth(func):
    """

    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        from util.reader import Reader
        reader = Reader()
        if reader.is_login():
            wrapper.__name__ = func.__name__
            res = func(*args, **kwargs)
            return res
        else:
            wrapper.__name__ = 'login_passively'
            res = reader.login()
            return res
    return wrapper

