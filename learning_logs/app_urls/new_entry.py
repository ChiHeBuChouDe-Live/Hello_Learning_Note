"""
@file: new_topic
@author: zouweicheng.wy_zou1103@163.com
@date: 2022/04/01
@decs

"""
from django.urls import re_path
from learning_logs import views

urlpatterns = [
    re_path(r'(?P<topic_id>\d+)/$', views.new_entry, name='new_entry')
]