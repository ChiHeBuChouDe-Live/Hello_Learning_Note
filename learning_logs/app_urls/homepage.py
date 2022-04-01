"""
@file: app_urls
@author: zouweicheng.wy_zou1103@163.com
@date: 2022/03/29
@decs
定义learning_logs的URL模式
"""
from django.urls import path
from learning_logs import views


urlpatterns = [
    # 主页
    # 这里设置name，为了在模板文件中，写name，就能找到这个路由
    # path(route,view,kwargs,name),name 给 URL 起个别名，常用于 url 的反向解析，避免在模板中适应硬编码的方式使用嵌入 url
    path('', views.index, name='index'),
]
