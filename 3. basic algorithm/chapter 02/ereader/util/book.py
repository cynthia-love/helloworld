# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
from util.dao import book_handler as bh

# 书本身没有存储和用户相关的信息, 其实可以采用服务定位器模式
# 同bookid的就不新创建Book对象了, 这样可以充分利用已加载的content, 减少数据库访问
class Book:
    def __init__(self, bookid, title, file):
        self.bookid = bookid
        self.title = title
        self.file = file
        self.content = None

    @staticmethod
    def get_list():
        return bh.get_list()

    def get_content(self):
        if not self.content:
            # 首次获取内容, 从文件中获取
            self.content = bh.get_content(self.file)
        return self.content

    def get_lines(self, start):
        # 其实这里也应该从缓存里取好些
        return bh.get_lines(self.file, start)


