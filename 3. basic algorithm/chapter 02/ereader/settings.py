# -*- coding; utf-8 -*-
# Author: Cynthia

"""

"""
import os

PAGE_LINE = 4  # 位置记忆可以采用行计, 也可以采用字符数计, 不过用字符计中文不好处理

BASE_PATH = os.path.dirname(__file__)

DB_PATH = os.path.join(BASE_PATH, 'db')

DB_PATH_READER = os.path.join(DB_PATH, 'reader.db')
DB_PATH_BOOK = os.path.join(DB_PATH, 'book.db')

DB_PATH_SHELF = os.path.join(DB_PATH, 'shelf.db')
DB_PATH_HISTORY = os.path.join(DB_PATH, 'history.db')

BOOK_PATH = os.path.join(BASE_PATH, 'book')

LOG_PATH = os.path.join(BASE_PATH, 'log', 'user.log')