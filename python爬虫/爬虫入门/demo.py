import requests
r=requests.get("http://tmc.flybycloud.com/auth/login")
r.encoding='urf-8'
#print(r.text)

from bs4 import BeautifulSoup

soup=BeautifulSoup(r.text,'lxml')
print(soup.prettify())


