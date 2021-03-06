#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : haolv

from django.conf.urls import url
from account import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'own_login/$',views.user_login,name='user_login'),   # 自定义登录
    url(r'login/$',auth_views.login,{"template_name":"account/login.html"},name='user_login'),   # django内置登录，p56
    url(r'login_out/$',auth_views.logout,{'template_name':'account/logout.html'},name='user_logout'),
    url(r'register/$',views.register,name='user_register'),   # django的注册没有内置方法，因为注册过程，网站需求不同
]

