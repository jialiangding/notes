实验环境
主机manager 192.168.1.247
node        192.168.1.249
consul      192.168.1.248


三台服务器初始化配置参考
/Linux部署环境/centOS搭建docker.md

 ec2-user 添加到 docker 组，以便您能够执行 Docker 命令，而无需使用 sudo：

ps:usermod -a -G group1 user1 添加用户user1到组group1里。
>sudo usermod -a -G docker ec2-user



进入consul 192.168.1.248
> $ docker run -d -p 8500:8500 --name=consul progrium/consul -server -bootstrap -advertise=<consul0_ip>


#

