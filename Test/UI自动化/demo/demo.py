from poium import Page,PageElement
import yaml
import os

from selenium import webdriver
from bs4 import BeautifulSoup
# curPath = os.path.dirname(os.path.realpath(__file__))
# yamlPath = os.path.join(curPath, "config.yaml")

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)  # 设置无图模式
chrome_driver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
