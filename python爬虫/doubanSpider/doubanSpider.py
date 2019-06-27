from bs4 import BeautifulSoup
import requests
import time
import json
import os


def get_html(web_url):
   header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko Core/1.70.3704.400 QQBrowser/10.4.3587.400"}
   html = requests.get(url=web_url, headers=header).text
   Soup = BeautifulSoup(html, "lxml")
   data = Soup.find("ol").find_all("li")
   return data


# #筛选出信息，保存进文本
def get_info():
       root_dir = os.path.dirname(os.path.abspath('.'))
     
       data_dir=root_dir+'/data/'
       f = open(data_dir,'r') 
   # pass





if __name__ == "__main__":
      data=get_html("https://movie.douban.com/top250")
      get_info()
