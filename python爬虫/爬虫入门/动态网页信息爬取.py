import requests
resp=requests.get("https://www.dianping.com/search/keyword/3/0_烧烤")
print(resp)  #403  此时需要加入请求头
resp=requests.get("https://www.dianping.com/search/keyword/3/0_烧烤",headers={'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'is_xhr': '1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'is_params': 'imes=2.4.280',
    'Accept': '*/*',
    'Referer': 'https://www.baidu.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'is_referer': 'https://www.baidu.com/',})
print(resp) #200

from selenium import webdriver
import os

driver=webdriver.Chrome()
# driver.get("https://www.dianping.com/search/keyword/3/0_烧烤")
# print(driver.page_source)

# driver.quit()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("iphone")
driver.find_element_by_id("su").click()
import time
time.sleep(3)
abspath = os.getcwd()  
print(abspath)
driver.save_screenshot("python爬虫/src")
print(driver.current_url)
# for elem in driver.find_element_by_xpath("//*[contains(@class,'result')]/h3/a")
#   print(elem.text)
driver.quit()


