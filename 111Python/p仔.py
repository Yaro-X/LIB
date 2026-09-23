#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: main.py 
@time: 2022/5/18 下午11:46 
@description：瓜子二手车
"""
import json
import time

import requests
from fontTools.ttLib import TTFont

# 公众号：AirPython，专注于 Python 原创技术干货！

# 字体映射关系
# PS：由于字体数目很少，所以可以直接写死字体的映射关系
font_relation_map = {
    'uniE9CE': 0,
    'uniE41D': 1,
    'uniE630': 2,
    'uniEAF2': 3,
    'uniE325': 4,
    'uniE891': 5,
    'uniEC4C': 6,
    'uniE1D0': 7,
    'uniE76E': 8,
    'uniE52E': 9
}


# 目标网站：https://www.guazi.com/buy

def get_font_map():
    """
    获取字体映射关系
    :return:
    """
    font = TTFont(r'gzfont.woff2')

    # 字体文件转为xml文件
    # font.saveXML(r"font.xml")

    font_map = font.getBestCmap()
    font.close()

    # print(font_map)

    new_font_map = {}

    # 遍历字典，重新组成一个新的映射字典
    for index, key in enumerate(font_map):
        # print("key:", key)
        value = font_map[key]

        # 为防止对关系中没有相应的value导致报错，这里捕捉下异常
        try:
            temp = font_relation_map[value]
        except:
            temp = ''
        if temp != '':
            # 根据响应结果中字体反爬数据格式，将键值前面添加字符串&#，用于匹配
            new_font_map['&#' + str(key) + ";"] = temp

    return new_font_map


def get_car_list(pagenum: int, new_font_map: dict):
    """
    获取车列表数据
    :param new_font_map:
    :return:
    """
    url = f"https://mapi.guazi.com/car-source/carList/pcList?osv=IOS&minor=&sourceType=&ec_buy_car_list_ab=&location_city=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&page={pagenum}&pageSize=20&city_filter=15&city=15&guazi_city=15&qpres=540290128116654080&platfromSource=wap&versionId=0.0.0.0&sourceFrom=wap&deviceId=fdce5329-461d-4213-a6ce-e4c6d96a5e25"

    payload = {}
    headers = {
        'authority': 'mapi.guazi.com',
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://www.guazi.com',
        'platform': '5',
        'referer': 'https://www.guazi.com/',
        'token': '',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    }

    resp_str = requests.request("GET", url, headers=headers, data=payload).text

    # 全局替换
    for key, value in new_font_map.items():
        if key in resp_str:
            resp_str = resp_str.replace(key, str(value))

    # 数据解析
    resp = json.loads(resp_str)
    postList = resp.get("data").get("postList")

    for item in postList:
        title = item.get("title")
        road_haul = item.get("road_haul")  # 公里
        license_date = item.get("license_date")  # 购买时间
        price = item.get("price")  # 价格
        first_pay = item.get("first_pay")  # 首付

        print(f'车型：{title},公里数：{road_haul}，购买时间：{license_date}，价格：{price}，首付：{first_pay}')


if __name__ == '__main__':
    new_font_map = get_font_map()
    print(new_font_map)

    # 获取前5页的数据
    for pagenum in range(5):
        get_car_list(pagenum + 1, new_font_map)
        time.sleep(1)
        print('==' * 5)
