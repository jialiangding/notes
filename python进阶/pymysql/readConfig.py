import os
import  codecs
import configparser




#print("getcwd:"+os.getcwd())

class ReadConfig(object):


    @staticmethod
    def getConfig(configkey):

        path=os.path.abspath('python进阶/config.ini')
        # root_dir = os.path.dirname(os.path.abspath(''))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
        cf = configparser.ConfigParser()
        cf.read(path)

        secs = cf.sections()


        options = cf.options("DATABASE")  # 获取某个section名为Mysql-Database所对应的键

        items = cf.items("DATABASE")#获取section名为DATABASE所对应的全部键值对
        #print(items)
        return  cf.get("DATABASE", configkey)  # 获取[Mysql-Database]中host对应的值

if __name__ == "__main__":
    print(getConfig("host"))
