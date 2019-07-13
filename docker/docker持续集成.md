1. 可以使用dockerfile生成镜像 并为镜像打一个tag  生成后存放在本地
2. docker-registry是存放docker镜像的仓库
3. 需要部署一个企业内部的docker-hub
4. docker tag 可以为镜像打一个tag
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
