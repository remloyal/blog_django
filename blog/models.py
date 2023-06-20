from datetime import date

from django.db import models
from django.db.models.base import ModelBase


class ModelCustomName(ModelBase):
    def __new__(mcs, name, bases, attrs, **kwargs):
        table_name = f't_da_{name}'
        if not attrs.get('Meta', None):
            attrs['Meta'] = type("Meta", (), dict(db_table=table_name))
        abstract = getattr(attrs["Meta"], 'abstract', False)
        if not hasattr(attrs["Meta"], 'db_table') and not abstract:
            setattr(attrs['Meta'], 'db_table', table_name)

        return super().__new__(mcs, name, bases, attrs, **kwargs)


class BaseModel(models.Model, metaclass=ModelCustomName):
    id = models.BigAutoField(primary_key=True, verbose_name="ID")
    objects = models.Manager()

    class Meta:
        abstract = True


class ArticleSort(models.Model):
    id = models.IntegerField(primary_key=True, default="1")
    article_id = models.CharField(max_length=255)
    article_name = models.CharField(max_length=255)
    article_alias = models.CharField(max_length=255)
    article_description = models.CharField(max_length=255)

    def __str__(self):
        return self.article_name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
