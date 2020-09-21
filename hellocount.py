# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    统计代码量
"""
import os
from datetime import date

res = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            file_py = os.path.join(root, file)
            with open(file_py, 'r', encoding='utf-8') as f:
                res += len(f.readlines())

print("")
print("By {}, coding: {}, target finished: {:.2%}".format(
    date.today(), res, res/500000
))