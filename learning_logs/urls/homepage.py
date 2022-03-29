"""
@file: urls
@author: zouweicheng.wy_zou1103@163.com
@date: 2022/03/29
@decs
定义learning_logs的URL模式
"""
from django.urls import path
from learning_logs import views


urlpatterns = [
    # 主页
    path('', views.index),
]
