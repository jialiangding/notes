### 系统环境centos7.5
#### 安装环境依赖
 yum install gcc-c++
 yum install -y pcre pcre-devel
 yum install -y zlib zlib-devel
 yum install -y openssl openssl-devel
#### 开启防火墙端口
我们把nginx和vsftp要用到的端口先开启，免得后面出错:
```
irewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --zone=public --add-port=443/tcp --permanent
firewall-cmd --zone=public --add-port=22/tcp --permanent
firewall-cmd --zone=public --add-port=21/tcp --permanent
firewall-cmd --zone=public --add-port=30000-30999/tcp --permanent
```
#### yum安装nginx
yum -y install nginx
#### 修改nginx 默认端口
`vim /etc/nginx/nginx.conf`
默认修改为88端口
```
 server {
        listen       88 default_server;
        listen       [::]:88 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
```
service nginx restart
访问 主机ip:88  就能看到nginx的欢迎页
#### 配置nginx为图片服务器
vim /etc/nginx/conf.d/images.conf
内容如下

```
server {
        listen       8190;
        location ^~ /img/ {
                alias  /usr/local/images/;
                autoindex on;
        }

}


```
#### <font color=#FF0000 >配置中出现的问题</font>
在我百度nginx搭建图片服务器中，大多是博客都是在配置conf都是如下图所示

------------


![avatar](http://47.98.63.111:8190/note-pic/nginx-mistake.png)


------------
起初我也是这样配置的

```xml
server {
        listen       8190;

      location  /images/ {
                root   /usr/local/images/;
                autoindex on;
        }
}

```
当时配置的我图片路径就是/usr/local/images/
然后我去访问ip:8190/images/xxx.png ,返回404
后来百度到 
root路径原理：

root 配置的意思是，会在root配置的目录后跟上URL，组成对应的文件路径。

那么我访问 ip:8190/images/xxx.png 实际上nginx 访问的是 ip:8190//usr/local/images/images/xxx.png
所以我这里要修改成如下
```

      location  /images/{
                root   /usr/local/;
                autoindex on;
        }

```
这样
那么我访问 ip:8190/images/xxx.png 实际上nginx 访问的是 ip:8190//usr/local/images/xxx.png

#### 还有一种办法 就是不要配置root，用alias代替
```
location ^~ /img/ {
                alias  /usr/local/images/;
                autoindex on;
        }

```
 alias响应的路径：配置路径+静态文件(去除location中配置的路径)
1. 使用alias时，目录名后面一定要加"/"。
3. alias在使用正则匹配时，必须捕捉要匹配的内容并在指定的内容处使用。
4. alias只能位于location块中。（root可以不放在location中） 

**总结
root的处理结果是：root路径＋location路径
alias的处理结果是：使用alias路径替换location路径**


[========]

### 安装vsftp
yum -y install vsftpd

### 开启vsftp
systemctl start vsftpd.service

### 关闭firewall和SELinux
```
setenforce 0  # 设置SELinux 成为permissive模式 （关闭SELinux）
setenforce 1  # 设置SELinux 成为enforcing模式  （开启SELinux）
 
# 或者修改配置
vi /etc/selinux/config
# SELINUX=enforcing
# 注释掉
# SELINUXTYPE=targeted
# 注释掉
SELINUX=disabled
# 增加
:wq! #保存退出
setenforce 0
```






















