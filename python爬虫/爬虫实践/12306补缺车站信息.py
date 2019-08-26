from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import os
import re
import io
import sys
import pymysql



def result():
    conn = pymysql.connect(host='47.98.63.111', port=3306, user='root', passwd='86680334', db='test', charset='utf8')
    result = conn.cursor()
    return result


def getAllLocalStation_trup():
    cursor=result()
    cursor.execute("select * from train_station")
    row=cursor.fetchall()
    return row


class StationInfo():
    def __init__(self,station_code,station_name,station_code_big,station_pinyin,station_pinyin_sho):
     self.station_code=station_code
     self.station_name=station_name
     self.station_code_big=station_code_big
     self.station_pinyin=station_pinyin
     self.station_pinyin_sho=station_pinyin_sho
    def  tolist(self):
        station_list=[self.station_code,self.station_name,self.station_code_big,self.station_pinyin,self.station_pinyin_sho]
        return  station_list


def getLocalStationDict():
    local_dict = {}
    for i in getAllLocalStation_trup():
        # 转换为字典
        # print(i)   #(2449, 'rqw', '荣昌北', 'RQW', 'rongchangbei', 'rcb')
        z = i[1]
        station_code = i[1]
        station_name = i[2]
        station_code_big = i[3]
        station_pinyin = i[4]
        station_pinyin_sho = i[5]
        station_info = StationInfo(station_code, station_name, station_code_big, station_pinyin, station_pinyin_sho)
        # list_local=
        # print(
        local_dict[z] = station_info.tolist()
    return  local_dict


def  get12306StationNow():
    start_url = "https://www.12306.cn/index/script/core/common/station_name_v10036.js"
    re = requests.get(start_url)
    data = re.text
    more_str = "var station_names ='"  # 多余的字符，需要截取
    data = data[21:-2]
    data = data.split("@")
    station_dict = {}
    for i in data:
      station_list = i.split("|")  # ['zzn', '株洲南', 'KVQ', 'zhuzhounan', 'zzn', '2875']
      # print(station_list)
      # print()
      station_dict[station_list[0]]=station_list

    print(station_dict)
    return  station_dict

#    return  data   #['zzn', '株洲南', 'KVQ', 'zhuzhounan', 'zzn', '2875']

def check_station():
    count=0
    remote_station=get12306StationNow()
    for i in remote_station.keys():
        if i in getLocalStationDict().keys():
            print("已存在")
        else:
            count+=1

    print(count)



if __name__ == '__main__':
    # remote_station = get12306StationNow()
    # # print(remote_station.keys())
    # get12306StationNow()
    check_station()






