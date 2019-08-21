from selenium import webdriver
from bs4 import BeautifulSoup
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
prefs = {"profile.managed_default_content_settings.images": 2}
#chrome_options.add_experimental_option("prefs", prefs)  # 设置无图模式
#chrome_driver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

#driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.cn/")
print(driver.current_url)
driver.find_element_by_class_name("nav-line-2").click()
print(driver.current_url)
account=13758241239
password="a86680334"

driver.find_element_by_id("ap_email").send_keys(account)
driver.find_element_by_id("ap_password").send_keys(password)
driver.find_element_by_id("signInSubmit").click()
print(driver.current_url)
print(driver.find_element_by_class_name("nav-line-1").text)

###无界面浏览器下------elenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":".nav-line-1"}
 ## (Session info: headless chrome=76.0.3809.100)
 #界面浏览器成功运行