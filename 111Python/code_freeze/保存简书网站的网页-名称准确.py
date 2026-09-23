import requests
import re

# 目  录： https://www.jianshu.com/nb/27681479?order_by=added_at&page=1
# 每一页： https://www.jianshu.com/p/2cdfd18006b6
# 规  律:  <a class="title" target="_blank" href="/p/2cdfd18006b6">第五十八课：论一只爬虫的自我修养：特殊符号及用法</a>

#网站有防爬虫，header用于伪装成浏览器
head = {}
head["User-Agent"] ="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36 Maxthon/5.2.1.1000"

page_num = []
for i in range(1,9):
    url = f"https://www.jianshu.com/nb/27681479?order_by=added_at&page={i}"
    resp = requests.get(url , headers = head).text 

    p = re.findall(u'<a class="title" target="_blank" href="/p/(.*?)">(.*?)</a>' ,resp)
    for each_page in p:
        page_num.append(each_page)

page_dict = dict(page_num)
for page in page_dict.keys():
    page_url = f"https://www.jianshu.com/p/{page}"
    resp = requests.get(page_url ,headers= head).text
    file_name = f"H:/简书/{page_dict[page]}.html"
    print(page_dict[page])
    # with open(file_name , "w" ,encoding= "utf-8") as f:
    #     f.write(resp)
