from django.shortcuts import render
# Create your views here.


def index(request):
    """学习笔记的主题"""
    return render(request, template_name='index.html')
