1. docker server gave HTTP response to HTTPS client 
```
在/etc/docker下，创建daemon.json文件，写入：

{ "insecure-registries":["192.168.163.131:5000"]}

```
