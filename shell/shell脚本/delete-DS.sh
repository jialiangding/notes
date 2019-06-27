#!/bin/sh
#解压文件
unzip -o $1

#对解压后的目录删除.DS
cd ./
 dir=$1
# #echo ${dir}
 unzipdir=${dir%.*}  #% 从左边截取
#echo unzipdir

cd ./${unzipdir}
ls -a
find . -name "*.DS_Store" -type f -print -exec rm -rf {} \;
#删除完之后重新打包
zip -q -r data.zip WEB-INF

cp  data.zip  C:\\Users\\djl\\Desktop\\一鸣的打包文件\\${unzipdir}.zip
cd ..
pwd
#删除除了脚本文件的其余所有文件
# find . ! -name  delete-DS.sh -exec rm -f {} \;
for i in $(ls -l . |grep -v "delete-DS.sh" |awk '{print $9}');
do 
rm -rf $i;
done




