from selenium import webdriver
from bs4 import BeautifulSoup
chrome_driver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)  # 设置无图模式
driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
driver.get("https://www.amazon.cn/")