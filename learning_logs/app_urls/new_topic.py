"""
@file: new_topic
@author: zouweicheng.wy_zou1103@163.com
@date: 2022/04/01
@decs

"""
from django.urls import path
from learning_logs import views

urlpatterns = [
    path('', views.new_topic, name='new_topic')
]