一、Django数据同步过程中遇到的问题：

　　

1、raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

　　　django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.

　　解决办法：C:\Python37\Lib\site-packages\django\db\backends\mysql（python安装目录）打开base.py，注释掉以下内容：

 　　　　　　　if version < (1, 3, 13):

　　　　　　　　　　raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

　　

2、File "C:\Python37\lib\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_query

　　  query = query.decode(errors='replace')

　　AttributeError: 'str' object has no attribute 'decode'

　　解决办法：打开此文件把146行的decode修改为encode


二、Django连接MySQL出错
错误一：No module named 'MySQLdb'

原因：python3连接MySQL不能再使用mysqldb，取而代之的是pymysql。

解决方法：在python的MySQL包中，即路径：C:\Users\adong\AppData\Local\Programs\Python\Python36\Lib\site-packages\Django-2.0.3-py3.6.egg\django\db\backends\mysql

下的__init__.py文件中加入：

import pymysql

pymysql.install_as_MySQLdb()

 

错误二：django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11.None

原因：在解决了错误一以后出现了此错误。

解决方法：在python的MySQL包中，即路径：C:\Users\adong\AppData\Local\Programs\Python\Python36\Lib\site-packages\Django-2.0.3-py3.6.egg\django\db\backends\mysql

下的 base.py 文件中，注释掉一下两行代码：

if version < (1, 3, 3):
     raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__) 

错误三 AttributeError: 'str' object has no attribute 'decode'
```
    query = query.decode(errors='replace')
AttributeError: 'str' object has no attribute 'decode'

/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/django/db/backends/mysql/operations.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

decode  --> encode
 if query is not None:
            query = query.encode(errors='replace')
        return query
```
