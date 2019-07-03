
工具：

　　Python3

　　requests

　　BeautifulSoup

二、爬虫的基本流程：
 

用户获取网络数据的方式：

方式1：浏览器提交请求--->下载网页代码--->解析成页面

方式2：模拟浏览器发送请求(获取网页代码)->提取有用的数据->存放于数据库或文件中

爬虫要做的就是方式2；

 

1、发起请求

使用http库向目标站点发起请求，即发送一个Request

Request包含：请求头、请求体等 

Request模块缺陷：不能执行JS 和CSS 代码

 

2、获取响应内容(获取网页)

如果服务器能正常响应，则会得到一个Response

Response包含：html，json，图片，视频等

 

3、解析内容

解析html数据：正则表达式（RE模块），第三方解析库如Beautifulsoup，pyquery等

解析json数据：json模块

解析二进制数据:以wb的方式写入文件

 

4、保存数据

数据库（MySQL，Mongdb、Redis）

文件
