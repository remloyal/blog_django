from datetime import date

from django.db import models
from django.db.models.base import ModelBase
from django.utils import timezone
import uuid


class ArticleSort(models.Model):
    id = models.IntegerField(primary_key=True, default="1")
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    article_name = models.CharField(max_length=255)
    article_alias = models.CharField(max_length=255)
    article_description = models.CharField(max_length=255)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.article_name


class Article(models.Model):
    id = models.IntegerField(primary_key=True, default="1")
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    title = models.CharField(max_length=255)
    content = models.CharField(max_length=2550)
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=2550)
    comments = models.BooleanField(default=True)
    top_img = models.CharField(max_length=255)
    cover = models.CharField(max_length=2550)
    mathjax = models.CharField(max_length=255)
    katex = models.CharField(max_length=255)
    aside = models.CharField(max_length=2550)
    aplayer = models.CharField(max_length=255)

    def __str__(self):
        return self.key


class Lables(models.Model):
    id = models.IntegerField(primary_key=True, default="1")
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    acticle_id = models.CharField('文章id', max_length=255)
    label_id = models.CharField('标签id', max_length=255)

    def __str__(self):
        return self.key


'''
分类表
'''


class Sort(models.Model):
    id = models.IntegerField(primary_key=True, default="1")
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    acticle_id = models.CharField('文章id', max_length=255)
    sort_id = models.CharField('标签id', max_length=255)

    def __str__(self):
        return self.key


'''
资源管理表
'''


class FileControl(models.Model):
    # id = models.IntegerField(primary_key=True, default="1")
    # file_id = models.UUIDField(default=uuid.uuid4,)
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    name = models.CharField('资源名称', max_length=255)
    type = models.CharField('资源类型', max_length=255)
    suffix_name = models.CharField('后缀名', max_length=255)
    flie_path = models.CharField('资源路径', max_length=255)
    # picture = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.file_id
