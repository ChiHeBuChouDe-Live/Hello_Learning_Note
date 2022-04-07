"""
@file: urls
@author: zouweicheng.wy_zou1103@163.com
@date: 2022/04/07
@decs

"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
app_name = 'users'

urlpatterns = [
    # 登陆页面
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # 注销页面
    path('logout/', views.logout_view, name='logout'),
    # 注册页面
    path('register/', views.register, name='register'),
]
