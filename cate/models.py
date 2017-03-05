# encoding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SearchRecord(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id') #主键
    title = models.CharField(max_length=100)  # 标题
    url =models.CharField(max_length=200) #搜索地址

    def __unicode__(self):
        return self.title