import requests

resp=requests.get("https://www.12306.cn/index/index.html")
print(resp.text)