import requests
r=requests.get("https://movie.douban.com/top250")
r.encoding='urf-8'
#print(r.text)

from bs4 import BeautifulSoup

soup=BeautifulSoup(r.text,'lxml')
print(soup.prettify())  #打印 soup 对象的内容，格式化输出


# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

# Tag   Tag就是 HTML 中的一个个标签， Tag，它有两个重要的属性，name 和 attrs ：
# NavigableString
# BeautifulSoup
# Comment
