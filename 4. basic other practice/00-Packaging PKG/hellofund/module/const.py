# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    常量
"""

from datetime import date, timedelta

TODAY = date.today()
ONE_DAY_BEFORE = TODAY-timedelta(days=1)
ONE_YEAR_BEFORE = ONE_DAY_BEFORE-timedelta(days=365*1)
THREE_YEAR_BEFORE = ONE_DAY_BEFORE-timedelta(days=365*3)
FIVE_YEAR_BEFORE = ONE_DAY_BEFORE-timedelta(days=365*5)
TEN_YEAR_BEFORE = ONE_DAY_BEFORE-timedelta(days=365*10)

