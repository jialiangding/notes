### app设计
user - 用户管理
course -课程管理
organizaton - 机构和教师管理
operation - 用户操作管理
### 搭建环境
>mkvirtualenv mxonline
>pip3 install django==2.2.0


### 配置mysql连接
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mxonline",
        'USER':"root",
        'PASSWORD':"86680334",
        'HOST':"47.98.63.111",
    }
}
```
生成数据库脚本文件
> makemigrations

>migrate


### 设计user-app 的model
首先新建app 
>startapp users
编写modle
自定义userprofile 覆盖默认的user表
需要继承自django的Users
```

##继承django的User表
from  django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    #添加自己的字段
    nick_name=models.CharField(max_length=50,verbose_name="昵称",default="")
    birthday=models.DateField(verbose_name="生日",null=True,blank=True)
    SEX_CHOICES = (("male","男"),("female","女"))

    sex= models.CharField(
        max_length=2,
        choices=SEX_CHOICES,
        default="female"),
    address=models.CharField(max_length=100,default="",verbose_name="地址")
    mobile=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100)
```
定义表的mate信息
   ```
  class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name
   ```

### 注册APP
setting文件中配置
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

AUTH_USER_MODEL="users.UserProfile"

```
重启项目
此时会遇到几个问题
>1. Cannot use ImageField because Pillow is not installed
>2. ValueError: Dependency on app with no migrations: users
解决办法
1. pip3 install Pillow 
2. 重新进行makemigrations users   

此时在报错
>django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
删除之前数据库中的表 
重新执行 migrate
重合服务成功

### 对app进行分层
为什么需要分层---为了防止互相循环引用

###继续构建model
>startapp courses
>一个课程对应多个章节 一对多
>一个章节下有多个视频  一对多
所以可以建立三张表 课程表 章节表   视频资源表
课程需要下课件--->所以课程对应多个课件  一对多
第四张 课程资源表




