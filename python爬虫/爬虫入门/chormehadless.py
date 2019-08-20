from selenium import webdriver

chrome_driver="E:\notes\python爬虫\driver\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
driver.get("https://www.baidu.com")
print(driver.current_url)
driver.close()