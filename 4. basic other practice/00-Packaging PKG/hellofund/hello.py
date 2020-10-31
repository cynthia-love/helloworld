# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import re
import sys
import requests
from hellofund.data.const import *
from datetime import datetime, date
from requests.exceptions import ConnectionError, HTTPError, RequestException

def stamp2struct(stamp: datetime):
    """

    :param stamp: 13位字符串
    :return: 基金分析只需要考虑到天, 所以返回date即可
    """
    stamp_float = int(stamp[:-3])
    return datetime.fromtimestamp(stamp_float).date()

def struct2str(struct: date):
    """
    :param struct:
    :return:
    """
    return struct.strftime("%Y-%m-%d")

def get_fund_list():

    url_fund_list = r"http://fund.eastmoney.com/js/fundcode_search.js"

    try:
        res = requests.get(url_fund_list).text
        pattern = r'\["([0-9]{6})",".*?","(.*?)",".*?",".*?"\]'
        return re.findall(pattern, res)
    except (ConnectionError, HTTPError, RequestException):
        print("fail to get fund list!")
        sys.exit(1)

print(get_fund_list())

def get_fun_detail(code: str):
    url_fund_detail = r"http://fund.eastmoney.com/pingzhongdata/{}.js"
    try:
        res = requests.get(url_fund_detail.format(code)).text

        fund_code = re.search(r'fS_code\s?=\s?"([0-9]{6})"', res).group(1)

        fund_name = re.search(r'fS_name\s?=\s?"(.*?)"', res).group(1)

        cur_stock = re.search(r'stockCodesNew\s?=\s?\[(.*?)\]', res).group(1)
        cur_stock = [e[3:-1] for e in cur_stock.split(',')]

        ac_value = re.search(r'Data_ACWorthTrend\s?=\s?\[\[(.*?)\]\]\s?;', res).group(1)
        ac_value = [e.split(',') for e in re.split(r'\],\[', ac_value[1:-1])]
        print(ac_value[-10:])
        for i in range(len(ac_value)):
            ac_value[i][0] = stamp2struct(ac_value[i][0])
            ac_value[i][1] = float(ac_value[i][1])
            if i == 0:
                ac_value[i].append(0.0)
            else:
                ac_value[i].append((ac_value[i][1]-ac_value[i-1][1])/ac_value[i-1][1]*100)

        """
        如果基金建立不到一年, 返回-1, 不要买这样的
        """
        found_date = ac_value[0][0]

        if found_date >= ONE_YEAR_BEFORE: return -1

        ac_value_5year = [e for e in ac_value if e[0] >= FIVE_YEAR_BEFORE]

        yield_1month = re.search(r'syl_1y\s?=\s?"(.*?)"', res).group(1)
        yield_1month = float(yield_1month)

        yield_3month = re.search(r'syl_3y\s?=\s?"(.*?)"', res).group(1)
        yield_3month = float(yield_3month)

        yield_6month = re.search(r'syl_6y\s?=\s?"(.*?)"', res).group(1)
        yield_6month = float(yield_6month)

        yield_1year = re.search(r'syl_1n\s?=\s?"(.*?)"', res).group(1)
        yield_1year = float(yield_1year)


    except (ConnectionError, HTTPError, RequestException):
        print("fail to get fund detail!")
        sys.exit(1)

get_fun_detail("000001")

print(stamp2struct("1601395200000"))
print(stamp2struct("1603987200000"))