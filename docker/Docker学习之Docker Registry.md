docker官方提供了Docker Hub来维护管理所有的镜像,只是对于免费用户而言,只能创建一个私有仓库,付费用户才拥有更多私有仓库的权限,对此官方开源了Docker Registry的源代码,我们可以通过它在局域网内部搭建私有的镜像注册中心.

Docker Hub是Docker官方维护的公共镜像注册中心,用户可以将自己的镜像推送到Docker Hub免费的仓库中,要想使用Docker Hub得先注册一个Docker Hub账号.
账号注册地址:https://hub.docker.com/(注意要想成功注册账号得先科学上网)

注册成功后就可以通过docker login命令输入账号密码登录进去创建我们自己的私有仓库和推送镜像了.



###  搭建本地注册中心
1. docker pull registry

```
[root@192 ~]# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
registry            latest              f32a97de94e1        4 months ago        25.8MB
```

2. 通过registry镜像启动一个容器.
> docker run -d -p 5000:5000 --name jeremy_registry  registry:latest

>docker tag 可以为镜像打一个tag

```
[root@192 ~]# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
registry            latest              f32a97de94e1        4 months ago        25.8MB
jenkins             latest              cd14cecfdb3a        12 months ago       696MB
[root@192 ~]# docker tag jenkins:latest  192.168.1.111:5000/jeremy_jenkins/jeremy_jenkins:0.11.1
[root@192 ~]# docker images
REPOSITORY                                         TAG                 IMAGE ID            CREATED             SIZE
registry                                           latest              f32a97de94e1        4 months ago        25.8MB
192.168.1.111:5000/jeremy_jenkins/jeremy_jenkins   0.11.1              cd14cecfdb3a        12 months ago       696MB
jenkins                                            latest              cd14cecfdb3a        12 months ago       696MB

```
3. 如何将镜像上传到registry库中,如何查看库中的内容
```
[root@192 docker]# docker push 192.168.1.111:5000/bosybox:v1.0
The push refers to repository [192.168.1.111:5000/bosybox]
6194458b07fc: Pushed 
v1.0: digest: sha256:bf510723d2cd2d4e3f5ce7e93bf1e52c8fd76831995ac3bd3f90ecc866643aff size: 527
```
> http://192.168.1.111:5000/v2/_catalog
> {"repositories":["bosybox"]}
```
- 列出所有存储库
http://192.168.1.111:5000/v2/_catalog
{"repositories":["bosybox"]}
- 列出镜像所有tags
http://192.168.1.111:5000/v2/{images-name}/tags/list
>http://192.168.1.111:5000/v2/bosybox/tags/list
>{"name":"bosybox","tags":["v1.0"]}

```


4. 从私有镜像中心拉取镜像
docker pull 192.168.1.111:5000/bosybox:v1.0
```
[root@192 docker]# docker pull 192.168.1.111:5000/bosybox:v1.0
v1.0: Pulling from bosybox
Digest: sha256:bf510723d2cd2d4e3f5ce7e93bf1e52c8fd76831995ac3bd3f90ecc866643aff
Status: Downloaded newer image for 192.168.1.111:5000/bosybox:v1.0
```