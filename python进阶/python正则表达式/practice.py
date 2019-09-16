import re

str1='imooc python'
print(str1.find('imooc'))
print(str1.find('ll'))
print(str1.startswith('imooc'))

###生成一个pattern的对象
pa=re.compile('imooc')
print(type(pa))

print(pa.match('imooc'))