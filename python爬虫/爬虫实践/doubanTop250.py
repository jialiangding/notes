from selenium import webdriver
from bs4 import BeautifulSoup
chrome_driver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
start_url="https://movie.douban.com/top250"
driver.get(start_url)


