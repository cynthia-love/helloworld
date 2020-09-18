# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
from util.dao import book_handler as bh

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
            self.content = bh.get_content(self.file)
        return self.content

    def get_lines(self, start):
        return bh.get_lines(self.file, start)


