#!/bin/bash
#################################################
#         Name: init.sh
#     Function: 自动拉取maven docker及源码打war包，
#               并复制war包到将要运行的tomcat docker挂载目录
#################################################
# 必须要要脚本所在目录运行该脚本以防出错

# 换个方式打包，不把maven和tomcat做成一个images，另起一个docker自动拉取maven docker及源码打war包，打包完成并复制war包到将要运行的tomcat docker挂载目录下，完成打包工作后再docker-compose；

# # 1.源码仓库地址，不要加http
# URL=IP/AAA/trade.git
# # 2.git用户名
# GIT_USERNAME=
# # 3.git密码
# GIT_PASSWORD=Qwer1234
# # 4.分支选择
# BRANCH=release
# # 5.打包环境及mvn参数指定，maven:3.6.0-jdk-8一定放在最前面
# MVN_ENV="maven:3.6.0-jdk-8 mvn clean package -U -DskipTests -P pro"
# # 6.在宿主机上的工作目录
# WORK_DIR=/mvn/build
# # 7.maven下载的依赖包存放在宿主机的目录，以便下次打包不用重新下载，加快打包速度
# M2_DIR=/mvn/m2-volume
# # 8.源码下载目录，根据GIT的URL生成
# SRC_DIR=`echo ${URL} | awk -F'/' '{print $3}' | cut -f1 -d "."`
# # 9.打好的war包要传送到容器外的tomcat/webapps将要挂载的目录
# # 默认为脚本当前目录下的tomcat/webapps，一般情况不用更改
# TOMCAT_DIR=/tomcat/webapps
# ===========================================

# 指定运行的maven容器名称
CTN_NAME=mvngo007
# 脚本当前目录
PWD_DIR=`pwd`
# 读取当前目录init-git.cnf文件参数
source ${PWD_DIR}/init-git.cnf

# 清除源码目录
rm -fr ${WORK_DIR}/${SRC_DIR}
# 建立工作目录
mkdir -p ${WORK_DIR} && cd ${WORK_DIR}
# 克隆项目源码
git clone -b ${BRANCH} "http://"${GIT_USERNAME}":"${GIT_PASSWORD}"@"${URL}
#git clone -b release http://longanhou:Qwer1234@47.106.125.91/chenercheng/trade.git

# 建立maven下载的依赖包目录
mkdir -p ${M2_DIR}
# 判断容器名称是否存在，如果不处理脚本会出错中止
# 如果存在就删除或可重启，没有就重新运行docker maven生成war包
docker ps -a|grep ${CTN_NAME}
if [[ $? -eq 0 ]];then
  docker rm ${CTN_NAME}
  #docker start ${CTN_NAME}
  #docker logs -f ${CTN_NAME}
else
  # 调用docker maven生成war包
  docker run -it --rm --name ${CTN_NAME} -v ${PWD_DIR}/maven/conf:/usr/share/maven/ref -v ${WORK_DIR}/${SRC_DIR}:/usr/src/mymaven -v ${M2_DIR}:/root/.m2 -w /usr/src/mymaven ${MVN_ENV}
fi
#docker run -it --name mvngo007 -v /server/docker/mvn/maven/conf:/usr/share/maven/ref -v /mvn/build/trade:/usr/src/mymaven -v /mvn/m2-volume:/root/.m2 -w /usr/src/mymaven maven:3.6.0-jdk-8 mvn clean package -U -DskipTests -P pro
# –name mvngo007：表示容器名称为mvngo007；
# -v ${PWD_DIR}/maven/conf:/usr/share/maven/ref：表示将宿主机的目录映射到Docker容器的/usr/share/maven/ref目录，也就是更改maven中央仓库源配置文件
# -v ${WORK_DIR}/${SRC_DIR}:/usr/src/mymaven：表示将宿主机的目录映射到Docker容器的/usr/src/mymaven目录，也就是源码的目录
# -w /usr/src/mymaven：表示容器的工作目录为/usr/src/mymaven；
# maven:3.6.0-jdk-8 mvn clean package -U -DskipTests：表示启动容器后在工作目录下执行的命令；

# 工作完成后复制所以war包到tomcat将要挂载的目录
mkdir -p ${PWD_DIR}${TOMCAT_DIR}
cp -fr ${WORK_DIR}/${SRC_DIR}/target/* ${PWD_DIR}${TOMCAT_DIR}

# 启动
cd ${PWD_DIR}
docker-compose up -d
