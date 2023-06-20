# Generated by Django 4.2.2 on 2023-06-20 01:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSort',
            fields=[
                ('id', models.IntegerField(default='1', primary_key=True, serialize=False)),
                ('article_id', models.CharField(max_length=255)),
                ('article_name', models.CharField(max_length=255)),
                ('article_alias', models.CharField(max_length=255)),
                ('article_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField()),
                ('mod_date', models.DateField(default=datetime.date.today)),
                ('number_of_comments', models.IntegerField(default=0)),
                ('number_of_pingbacks', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=5)),
                ('authors', models.ManyToManyField(to='blog.author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
