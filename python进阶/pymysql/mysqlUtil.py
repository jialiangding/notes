import pymysql

from readConfig import ReadConfig




def connect(cls):
    conn =pymysql.connect(
    host=cls.getConfig("host"),
    user=cls.getConfig("user"),password=cls.getConfig("passwd"),
    database=cls.getConfig("database"),charset=("utf8")
    )
    return conn
if __name__ == '__main__':
   conn=connect(ReadConfig)
   cursor = conn.cursor() 
   sql = "select * from user"
   print(cursor.execute(sql))