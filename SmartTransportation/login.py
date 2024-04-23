from functools import wraps

from django.conf.global_settings import SESSION_EXPIRE_AT_BROWSER_CLOSE
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.decorators import csrf
from Model.models import User as administrators
from django.contrib import auth


def logincheck(request):
    if administrators.objects.filter(userid=request.POST['A_id'], password=request.POST['password']):
        messages.success(request, '欢迎回来！')
        user = administrators.objects.get(userid=request.POST['A_id'], password=request.POST['password'])
        # print(request.session['user_id'])
        print('------------------------------------------')
        request.session['is_login'] = True
        request.session['user_id'] = user.userid
        request.session['password'] = user.password
        request.session.set_expiry(0)
        return render(request, 'mainpage.html')
    else:
        request.session.pop('user_id')
        messages.success(request, '账号或密码错误，请重新输入')
        return render(request, 'login.html', {})


def deletecheck(request):
    request.encoding = 'utf-8'
    user = administrators.objects.get(A_id=request.session['user_id'], password=request.session['password'])
    user.delete()
    messages.success(request, '注销成功!')
    return render(request, 'Register.html', {})


def checksession(request):
    a = request.session['user_id']
    print(a)
    return 1


# 登录界面session

def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.session.get("is_login")
        # 1. 获取cookie中的随机字符串
        # 2. 根据随机字符串去数据库取 session_data --> 解密 --> 反序列化成字典
        # 3. 在字典里面 根据 is_login 取具体的数据

        if ret == True:
            # 已经登录，继续执行
            return func(request, *args, **kwargs)
        # 没有登录过
        else:
            # ** 即使登录成功也只能跳转到home页面，现在通过在URL中加上next指定跳转的页面
            # 获取当前访问的URL
            return render(request, 'login.html')

    return inner
