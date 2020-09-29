# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    统计特定目录磁盘使用情况

    注意, os.path.getsize(url), 对于目录, 返回的是目录本身的大小, 不包括里面的东西
    这与直接右键查看目录大小不同, 后者只返回目录里面的所有东西的大小, 而不包括目录本身大小

    递归思路还是找边界条件和递推式:
                size(url), 如果是文件
    f(url) =
                size(url)+ 所有f(url_next), 如果是目录
"""
import os
def f(url):
    size = os.path.getsize(url)

    if os.path.isdir(url):
        for each in os.listdir(url):
            size += f(os.path.join(url, each))

    print('{:<7}'.format(size), url)
    return size

f('.')