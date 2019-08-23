
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import os
import re
import io
import sys

chrome_driver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
start_url="https://www.12306.cn/index/script/core/common/station_name_v10036.js"
driver.get(start_url)
print(driver.page_source)
