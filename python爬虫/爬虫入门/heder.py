
import json
 
# 使用三引号将浏览器复制出来的requests headers参数赋值给一个变量
headers = """
GET /index/script/core/common/station_name_v10036.js HTTP/1.1
Host: www.12306.cn
Connection: keep-alive
Sec-Fetch-Mode: no-cors
If-None-Match: "5d4a7b5b-17a72"
If-Modified-Since: Wed, 07 Aug 2019 07:18:51 GMT
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36
Accept: */*
Sec-Fetch-Site: same-origin
Referer: https://www.12306.cn/index/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BIGipServerpool_index=770703882.43286.0000; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=200278538.50210.0000; RAIL_EXPIRATION=1566808775088; RAIL_DEVICEID=VaL5dufLUbBvhJzfuLX6XYq-yQtB1F2jFVVNQW3rGoKo2iPdjo6DNp3gqpAbPAvNqUcrloNoHA4LGL3K97GDak0pr1WfjTxStBzR8Czo6DppEa10uBL0LGY_1HI0N53ncRWYozITij6vNaIeRlb79GldaHe2eRbG

"""
 
# 去除参数头尾的空格并按换行符分割
headers = headers.strip().split('\n')
print(headers)
 
# 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}
 
# 使用json模块将字典转化成json格式打印出来
print(json.dumps(headers,indent=1))
