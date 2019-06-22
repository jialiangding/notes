### ubuntu16.04安装过程
1. 获取ubuntu16.04镜像
http://ubuntu.cn99.com/ubuntu-releases/16.04/ubuntu-16.04.6-server-amd64.iso
2. 更新源,安装ssh、vim，重置root密码
   >更新源
   >apt-update
   >安装ssh,vim

   >重置root密码
3. 安装docker apt-get install -y docker.io
4. docker镜像加速器 
   > curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://d552c9b5.m.daocloud.io
5. 拉去mysql5.6镜像
   > docker pull mysql:5.6
6. 构建并启动mysql5.6容器 
   > docker run  -p 3306:3306 --name  mymysql -v  /home/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.6
7. 配置网卡
   > vim /etc/network/interfaces
   
   ```
source /etc/network/interfaces.d/*
auto lo
iface lo inet loopback
auto ens33
iface ens33 inet static
address 192.168.1.113
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameserver 8.8.8.8
   ```

配置科学上网


