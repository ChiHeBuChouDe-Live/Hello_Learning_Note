from django.shortcuts import render
from .models import Topic
# Create your views here.


def index(request):
    """学习笔记的主题"""
    return render(request, template_name='index.html')


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    # 必须将变量封装到字典中才允许传递到模板上
    context = {'topics': topics}
    return render(request, template_name='topics.html', context=context)


def topic(request, topic_id):
    """显示单个主题以及其所有条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, template_name='topic.html', context=context)
