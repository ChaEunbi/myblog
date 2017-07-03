# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-02 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='one word for title alias.', null=True, unique=True, verbose_name='SLUG'),
        ),
    ]
