"""
@file: forms
@author: zouweicheng.wy_zou1103@163.com
@date: 2022/04/01
@decs
meta,它告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段
"""
from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
