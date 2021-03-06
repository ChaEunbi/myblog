# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-02 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='TITLE')),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'my_post',
                'ordering': ('-modify_date',),
            },
        ),
    ]
