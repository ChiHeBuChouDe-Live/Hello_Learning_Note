from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.8/ref/models/fields/ 模型字段参考


class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)     # text由字符或文本组成的数据,并数据库中预留多少空间(200个字符)
    date_added = models.DateTimeField(auto_now_add=True)    # 记录日期和时间的数据 每当用户创建新主题时，这都让Django将这个属性自动设置成当前日期和时间

    def __str__(self):
        """
        返回模型的字符串表示方法(返回一个对象的详细信息)，在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
        当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
        """
        return self.text
