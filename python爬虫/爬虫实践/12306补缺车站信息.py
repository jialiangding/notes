
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import os
import re
import io
import sys


start_url="https://www.12306.cn/index/script/core/common/station_name_v10036.js"
re=requests.get(start_url)
data=re.text
list="var station_names ='"  #多余的字符，需要截取
data=data[20:-2]

#print(data)


print("-------------------------------------------------------")
#根据@分割
data= data.split("@")
for i in data:
   print(i)












