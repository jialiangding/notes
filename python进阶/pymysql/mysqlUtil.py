import pymysql






def connect(config):


    conn =pymysql.connect(
    host=config("host"),
    user=config("host"),password=config("host"),
    database=config("host"),charset=("utf8")
    )
    return conn
if __name__ == '__main__':
    
    connect(getConfig)
