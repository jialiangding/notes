import requests
from requests.exceptions import  RequestException
from bs4 import  BeautifulSoup
import  lxml
import  re




def start_requests(url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
        response=requests.get(url,headers=headers)
        html=response.text
        soup=BeautifulSoup(html,"lxml")
        #1.所有电影信息存储在dl标签
        dlObj = soup.find('dl',class_='board-wrapper')
        # 2.获取每个电影的详细信息，存储在li标签
        details = dlObj.find_all('dd')
        # 3.获取需要的电影信息
        for detail in details:
                # 电影名称
             movieId = detail.find('i',class_='board-index').get_text()
             movieName=detail.find('img',class_='board-img').get('alt')
             moviePic=detail.find('img',class_='board-img').get('data-src')
             movieStar1=detail.find('i',class_='integer').get_text()
             movieStar2=detail.find('i',class_='fraction').get_text()
             movieStar=movieStar1+movieStar2
             #print(movieStar)

def main():
        nextUrlObj = soup.find('ul',class_='list-pager')
        print(nextUrlObj)




if __name__ == '__main__':
   #start_requests("https://maoyan.com/board/4?offset=0")
    