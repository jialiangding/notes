import  requests
from requests.exceptions import  RequestException
from bs4 import  BeautifulSoup
import  lxml
import  re
def get_one_page(url):
    try:
         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
         response=requests.get(url,headers=headers)
         if response.status_code==200:
          return  response.text
    except RequestException:
        return  None


def parse_one_page(html):
    # patten=re.compile('')
#     # item=re.findall(patten,html)
#     # print(item)
     soup=BeautifulSoup(html,'lxml')
     
     soup2 = soup.find_all('dd')
     print(soup2)
#     images=soup.find_all( class_ ="board-img")
#     for item in images:
#         print(item.attrs['alt'])
#         print(item.attrs['data-src'])
    #  items= soup.find_all( class_ ="board-wrapper")
    #  for item in items:
    #      print(item)
    #      num=item.find('i').text
    #      # movie_name=item.find('img',class_='board-img"').attrs['alt']
    #      # pic=item.find('img',class_='board-img"').attrs['data-src']
    #      # print(movie_name)
    #      # print(pic)
    #      print(num)







#
#
# for child in content.children:
#     if child.string is not None:
#         print(child.string.strip())

def main(url):

    html=get_one_page(url)
    #print(html)


if __name__ == '__main__':
    url = "http://maoyan.com/board/4?offset=0"
    html=get_one_page(url)
   # parse_one_page()
    parse_one_page(html)