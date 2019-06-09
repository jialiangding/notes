# 进程和服务管理
  ## 1. netstat 
   > netstat - atulnp会显示所有端口和所有对应的程序，用grep管道可以过滤出想要的字段
   1. -a ：all，表示列出所有的连接，服务监听，Socket资料
   2. -t ：tcp，列出tcp协议的服务
   3. -u ：udp，列出udp协议的服务
   4. -n ：port number， 用端口号来显示
   5. -l ：listening，列出当前监听服务
   6. -p ：program，列出服务程序的PID

  ## 2. lsof -i:端口号 ***查看某一端口的占用情况***

