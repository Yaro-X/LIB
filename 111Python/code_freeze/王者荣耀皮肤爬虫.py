#图片:http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/155/155-bigskin-2.jpg
#英雄列表:https://pvp.qq.com/web201605/js/herolist.json

import requests #用于获取网页
import os
import urllib #用于下载图片 全称urllib.request.urlretrieve(网址，保存地址) 这个request 不是requests(带s的是模块名)
import time #用于休息，过于频繁的下载图片会被官网屏蔽，需要休息一下


url ="https://pvp.qq.com/web201605/js/herolist.json" #信息列表 的网址

resp = requests.get(url)
hero_list = resp.json() #读取信息列表
for hero in hero_list:
    hero_id = hero["ename"]  #提取 信息列表 的"ename"
    hero_name = hero["cname"]#提取 信息列表 的"cname"
    path_save = f"K:/999-/skin_img/{hero_name}"
    os.makedirs(path_save ) #os.makedirs 这个用于建多层文件
    print(hero_name)
    for i in range(1,9):
        skin_url = f"http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero_id}/{hero_id}-bigskin-{i}.jpg"
        hero_resp = requests.get(skin_url)
        if hero_resp.status_code == 404: #网页代码 200为正常，404则错误（不存在页面）
            continue                     #如果代码为404 ，跳过当前剩下循环，开始新一轮循环
        urllib.request.urlretrieve(skin_url , path_save + f"/-{i}.jpg")
        #print(skin_url , hero_resp.status_code)

    time.sleep(0.5)
