from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField('标题', max_length=256, null=True, blank=True, default='')
    desc = models.CharField('描述', max_length=256, null=True, blank=True, default='')
    author = models.ForeignKey(User, verbose_name='作者', related_name='blog', on_delete=models.SET_NULL,
                               null=True, blank=True)
    lover = models.ManyToManyField(User, verbose_name='点赞人', related_name='love_blog', blank=True)
    content = models.TextField('内容', null=True, blank=True)
    update = models.DateTimeField('更新时间', auto_now=True, null=True, blank=True)