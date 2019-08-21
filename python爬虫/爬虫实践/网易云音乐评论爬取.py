from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://music.163.com/#/song?id=1369798757")
#等待页面载入
time.sleep(5)

#找到用户评论--->切换ifram
#找到可以指定到唯一iframm的标识 不能唯一 则driver.find_elements
ifram=driver.find_element_by_class_name("g-iframe")
#切换
driver.switch_to_frame(ifram)

#利用xpath找到所有评论项目
s=driver.find_elements_by_xpath("//div[@class='cnt f-brk']")
print("---------------------------------")
for comment in s:
    print(comment.text)
#切换回到主页面
driver.switch_to_default_content()


