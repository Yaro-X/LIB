import requests

head = {}
head["User-Agent"] ="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36 Maxthon/5.2.1.1000"

url = "https://www.jianshu.com/p/2cdfd18006b6"
resp = requests.get(url , headers = head)
text = resp.text

save_path = "H:\999"
file_name = f"H://999/11111.html"

with open(file_name,"w",encoding = "utf-8") as f:
    f.write(text)
