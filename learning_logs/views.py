from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    """学习笔记的主题"""
    return render(request, template_name='index.html')


@login_required     # 检查是否登录，未登录重定向到登陆页面，登录就执行下边视图
def topics(request):
    """显示所有主题"""
    # Topic.objects.filter(owner=request.user)让Django只从数据库中获取owner属性为当前用户的Topic对象
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # 必须将变量封装到字典中才允许传递到模板上
    context = {'topics': topics}
    return render(request, template_name='topics.html', context=context)


@login_required
def topic(request, topic_id):
    """显示单个主题以及其所有条目"""
    topic = get_object_or_404(Topic, id=topic_id)  # get_object_or_404()。这个函数尝试从数据库获取请求的对象，如果这个对象不存在，就引发404异常
    # 确认请求的主题属于当前用户,限制单个主题页面的访问
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, template_name='topic.html', context=context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != "POST":
        # 未提交数据: 创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, template_name='new_topic.html', context=context)


@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新的条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        # 未提交数据: 创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑现有的条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        # 初次请求, 使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)
