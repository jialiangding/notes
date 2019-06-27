from bs4 import BeautifulSoup
import requests
import time
import json


def get_html(web_url):
   header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko Core/1.70.3704.400 QQBrowser/10.4.3587.400"}
   html = requests.get(url=web_url, headers=header).text
   Soup = BeautifulSoup(html, "lxml")
   data = Soup.find("ol").find_all("li")
   return data