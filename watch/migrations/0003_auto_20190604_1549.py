# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-04 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_auto_20190603_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
