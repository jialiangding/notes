#  四、完成登录功能
## 4.1 首页和登录页面的配置
1. 把html文件中index.html拷贝到templates文件夹内
2. 新建static目录用来存放静态文件
```
在settings.py中设置路径

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
```
3. 将html中引用静态文件的地方进行修改

4. 配置路由
```
rom django.contrib import admin
from django.urls import path
from apps.users.views import  user_login
import xadmin
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),

    
]
```
## 4.2 用户登录
1. 配置路由
```
path('login/', user_login, name='login'),
```
2. 配置视图
users.view
```
rom django.shortcuts import render

# Create your views here.


from django.contrib.auth import authenticate, login
###登录逻辑
def user_login(request):
    if request.method=="POST":
        user_name=request.POST.get("username",None)
        pass_word=request.POST.get("password",None)

        ##开始验证
        user=authenticate(username=user_name,password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
    else:
        return render(request, 'login.html')

```
3. 更改login.html
```
<form action="/login/" method="post" autocomplete="off">
                    <input type='hidden' name='csrfmiddlewaretoken' value='mymQDzHWl2REXIfPMg2mJaLqDfaS1sD5' />
                    <div class="form-group marb20 ">
                        <label>用&nbsp;户&nbsp;名</label>
                        <input name="username" id="account_l" type="text" placeholder="手机号/邮箱" />
                    </div>
                    <div class="form-group marb8 ">
                        <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
                        <input name="password" id="password_l" type="password" placeholder="请输入您的密码" />
                    </div>
                    <div class="error btns login-form-tips" id="jsLoginTips">{{ msg }}</div>
                     <div class="auto-box marb38">

                        <a class="fr" href="forgetpwd.html">忘记密码？</a>
                     </div>
                     <input class="btn btn-green" id="jsLoginBtn" type="submit" value="立即登录 > " />
                <input type='hidden' name='csrfmiddlewaretoken' value='5I2SlleZJOMUX9QbwYLUIAOshdrdpRcy' />
                    {% csrf_token %}
                </form>

```
>csrf_token 跨域处理 


4. 修改index.html
到了此时，登录成功后
![](./res/登录成功后.png)
需要做个验证，当用户已登录状态的时候，显示用户姓名和图像及其个人中心信息
需要修改index.html

```
   <header>
        <div class=" header">
            <div class="top">


                <!--登录后跳转-->
                {% if request.user.is_authenticated %}


                <div class="personal">
                    <dl class="user fr">
                        <dd>bobby<img class="down fr" src="/static/images/top_down.png"/></dd>
                        <dt><img width="20" height="20" src="/static/media/image/2016/12/default_big_14.png"/></dt>
                    </dl>
                    <div class="userdetail">
                        <dl>
                            <dt><img width="80" height="80" src="/static/media/image/2016/12/default_big_14.png"/></dt>
                            <dd>
                                <h2>django</h2>
                                <p>bobby</p>
                            </dd>
                        </dl>
                        <div class="btn">
                            <a class="personcenter fl" href="usercenter-info.html">进入个人中心</a>
                            <a class="fr" href="/logout/">退出</a>
                        </div>
                    </div>
                </div>
                {% else %}
                <div class="wp">
                    <div class="fl"><p>服务电话：<b>33333333</b></p></div>
                    <a style="color:white" class="fr registerbtn" href="register.html">注册</a>
                    <a style="color:white" class="fr loginbtn" href="/login/">登录</a>

                </div>
            </div>

            {% endif%}
        </div>
```

5. 增加邮箱登录
让用户可以通过邮箱或者用户名都可以登录，用自定义authenticate方法
这里是继承ModelBackend类来做的验证
首先需要在setting中重载一个变量
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)
```
from django.shortcuts import render

# Create your views here.


from django.contrib.auth import authenticate, login

from django.contrib.auth.backends import ModelBackend
from .models import  UserProfile


from django.db.models import Q


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if(user.check_password(password)):
                return  user
        except Exception as e:
            return  None




###登录逻辑
def user_login(request):
    if request.method=="POST":
        user_name=request.POST.get("username",None)
        pass_word=request.POST.get("password",None)

        ##开始验证
        user=authenticate(username=user_name,password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
    else:
        return render(request, 'login.html')




```
