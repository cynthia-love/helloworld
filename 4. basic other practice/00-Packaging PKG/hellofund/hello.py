# -*- coding: utf-8 -*-
# Author: Cynthia

"""

"""
import re
import sys
import requests
import numpy as np
from hellofund.module.const import *
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

        # 基金编号
        fund_code = re.search(r'fS_code\s?=\s?"([0-9]{6})"', res).group(1)

        # 基金中文名
        fund_name = re.search(r'fS_name\s?=\s?"(.*?)"', res).group(1)

        # 基金评分
        fund_score = re.search(r'Data_performanceEvaluation.*?"avr":"(.*?)"', res).group(1)

        # 投资股票的比例
        stock_ratio = re.search(r'"股票占净比".*?"data".*?\[(.*?)]', res).group(1)
        stock_ratio = np.mean([float(e)/100 for e in stock_ratio.split(',')])
        # 这里加一步限制, 如果股票持仓比例小于50%, 不买这种
        if stock_ratio <= 0.5: return -1

        # 机构持有比例
        org_ratio = re.search(r'"机构持有比例".*?\[(.*?)]}', res).group(1)
        org_ratio = np.mean([float(e)/100 for e in org_ratio.split(',')])

        # 内部持有比例
        inner_ratio = re.search(r'"内部持有比例".*?\[(.*?)]}', res).group(1)
        inner_ratio = np.mean([float(e)/100 for e in inner_ratio.split(',')])
        print(inner_ratio)

        # 基金经理名称
        manager_name = re.search(r'Data_currentFundManager\s?=\s?.*?"name":"(.*?)"', res).group(1)
        # 基金经理工作时长, 文字描述
        manager_worktime = re.search(r'Data_currentFundManager\s?=\s?.*?"workTime":"(.*?)"', res).group(1)
        print(manager_worktime)
        # 基金经理评分
        manager_score = re.search(r'Data_currentFundManager\s?=\s?.*?"avr":"(.*?)"', res).group(1)
        # 基金经理跑赢沪深300能力
        manager_beyond300 = re.search(r'Data_currentFundManager\s?=\s?.*?"y":(.*?)}.*?"y":(.*?)}.*?"y":(.*?)}', res)
        manager_beyond300 = float(manager_beyond300.group(1))/float(manager_beyond300.group(3))

        # 当前持仓
        cur_stock = re.search(r'stockCodesNew\s?=\s?\[(.*?)\]', res).group(1)
        cur_stock = [e[3:-1] for e in cur_stock.split(',')]

        # 累计净值
        ac_value = re.search(r'Data_ACWorthTrend\s?=\s?\[\[(.*?)\]\]\s?;', res).group(1)
        ac_value = [e.split(',') for e in re.split(r'\],\[', ac_value[1:-1])]
        for i in range(len(ac_value)):
            ac_value[i][0] = stamp2struct(ac_value[i][0])
            ac_value[i][1] = float(ac_value[i][1])
            if i == 0:
                ac_value[i].append(0.0)
            else:
                ac_value[i].append((ac_value[i][1]-ac_value[i-1][1])/ac_value[i-1][1])

        # 10年以前成立的, 按10年前算
        ac_value = [e for e in ac_value if e[0] >= TEN_YEAR_BEFORE]
        """
        如果基金建立不到一年, 返回-1, 不要买这样的
        """
        # 成立日期
        found_date = ac_value[0][0]
        if found_date >= ONE_YEAR_BEFORE: return -1

        # 近一月收益
        yield_1month = re.search(r'syl_1y\s?=\s?"(.*?)"', res).group(1)
        yield_1month = float(yield_1month)/100

        # 近三月收益
        yield_3month = re.search(r'syl_3y\s?=\s?"(.*?)"', res).group(1)
        yield_3month = float(yield_3month)/100

        # 近6月收益
        yield_6month = re.search(r'syl_6y\s?=\s?"(.*?)"', res).group(1)
        yield_6month = float(yield_6month)/100

        # 近一年收益
        yield_1year = re.search(r'syl_1n\s?=\s?"(.*?)"', res).group(1)
        yield_1year = float(yield_1year)/100

        # 同类排名走势
        rate_order = re.search(r'Data_rateInSimilarType\s?=\s?\[(.*?)]', res).group(1)
        rate_order = re.findall(r'{"x":(.*?),"y":(.*?),"sc":"(.*?)"', rate_order)
        rate_order = [(stamp2struct(e[0]), float(e[1])/float(e[2])) for e in rate_order]
        # 参照累计净值, 这里过滤10年以上的
        rate_order = [e for e in rate_order if e[0] >= TEN_YEAR_BEFORE]
        print(rate_order)

    except (ConnectionError, HTTPError, RequestException):
        print("fail to get fund detail!")
        sys.exit(1)

get_fun_detail("000001")

print(stamp2struct("1601395200000"))
print(stamp2struct("1588176000000"))
