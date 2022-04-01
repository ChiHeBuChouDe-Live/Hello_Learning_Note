"""
@file: topics
@author: zouweicheng.wy_zou1103@163.com
@date: 2022/03/31
@decs

"""
from django.urls import path, re_path
from learning_logs import views


urlpatterns = [
    path('', views.topics, name='topics'),
    re_path(r'(?P<topic_id>\d+)/$', views.topic, name='topic')  # ?P<topic_id>指定位置参数，需要要在视图函数指定一个同名的形参,接受路由传递的参数
]
