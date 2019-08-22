from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import os
import re
# chrome_driver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver)
# start_url="https://movie.douban.com/top250"
# driver.get(start_url)

# print(driver.current_url)


def download(url, page):
    print(f"正在爬取：{url}")
    html = requests.get(url).text   # 这里不加text返回<Response [200]>
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.select("ol li")
    for li in lis:
        index = li.find('em').text
        title = li.find('span', class_='title').text
        rating = li.find('span', class_='rating_num').text
        strInfo = re.search("(?<=<br/>).*?(?=<)", str(li.select_one(".bd p")), re.S | re.M).group().strip()
        infos = strInfo.split('/')
        year = infos[0].strip()
        area = infos[1].strip()
        type = infos[2].strip()
        write_fo_file(index, title, rating, year, area, type)
    page += 25
    if page < 250:
        time.sleep(2)
        download(f"https://movie.douban.com/top250?start={page}&filter=", page)


def write_fo_file(index, title, rating, year, area, type):
    f = open('movie_top250.csv', 'a')
    f.write(f'{index},{title},{rating},{year},{area},{type}\n')
    f.closed


def main():
    if os.path.exists('movie_top250.csv'):
        os.remove('movie_top250.csv')

    url = 'https://movie.douban.com/top250'
    download(url, 0)
    print("爬取完毕。")


if __name__ == '__main__':
    main()


