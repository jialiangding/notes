实验环境
主机manager 192.168.1.247
node        192.168.1.248
consul      192.168.1.249


三台服务器初始化配置参考
/Linux部署环境/centOS搭建docker.md

 ec2-user 添加到 docker 组，以便您能够执行 Docker 命令，而无需使用 sudo：
sudo usermod -a -G docker ec2-user