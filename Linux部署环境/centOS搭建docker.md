系统环境

虚拟机 --- CentOS Linux release 7.1.1503 (Core) 
### 进入虚拟机进行初始化配置
1. 配置网卡
> vim /etc/sysconfig/network-scripts/ifcfg-eno16777736
```
TYPE=Ethernet
BOOTPROTO=static
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_PEERDNS=yes
IPV6_PEERROUTES=yes
IPV6_FAILURE_FATAL=no
NAME=eno16777736
UUID=ef2781c6-e74d-49d4-bd43-f82d201b6f5b
DEVICE=eno16777736
ONBOOT=yes
GATEWAY=192.168.1.1        
IPADDR=192.168.1.111
NETMASK=255.255.255.0 
DNS1=8.8.8.8

```

2. 更新yum 源
> yum -y update


3. 搭建docker环境
   1. 安装yum-utils
   > yum install -y yum-utils
   2. 新增yum源
   > yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

   3. 建立元数据缓存
   > yum makecache fast
   4. 安装最新版本的docker
   >  yum -y install docker-ce
   5. 配置docker 加速器
    curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://d552c9b5.m.daocloud.i

   

   
