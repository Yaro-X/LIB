import requests     #获取网址
import os           #创建文件夹
import urllib.request   #下载图片
import jsonpath     #读取json文件
import time

# https://lol.qq.com/data/info-heros.shtml , https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
# https://game.gtimg.cn/images/lol/act/img/js/hero/64.js

url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
resp = requests.get(url).json()                      #所有英雄的汇总
hero_id_list = jsonpath.jsonpath(resp , "$..heroId") #读取json文件， 提取resp里的hero_list的id

for hero_id in hero_id_list:
    hero_url = f"https://game.gtimg.cn/images/lol/act/img/js/hero/{hero_id}.js"  #每个英雄的详细信息
    skin_resp = requests.get(hero_url).json()                   
    skin_list = jsonpath.jsonpath(skin_resp , "$..mainImg")     #json文件，提取 皮肤序号 ，提取后 生成一个列表，里面有空元素
    hero_name = jsonpath.jsonpath(skin_resp , "$..alias")       #json文件，提取 英雄名称
    hero_name = hero_name[0]        #将列表 转为 字符串

    print(hero_name)
    skin = [i for i in skin_list if i != ""]    #去除 列表里的 空元素， 剩下的每一个元素 均是 有效的皮肤url
    save_path = f"H:\9999\{hero_name}"
    os.makedirs(save_path)
    j = 0
    for skin_url in skin :
        try:        #正常的话所有网址都正确有内容 ，偏偏有一个会报404错误。。。
            urllib.request.urlretrieve(skin_url ,save_path + f"/-{j}.jpg" )
            j = j+1

        except:     #如有错误，记录错误
            print(f"{hero_name} have mistakes")
        continue    #记录错误后，跳过目前错误，执行后续的循环
    time.sleep(0.2)




