# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20180502_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.FileField(default='C:\\Users\\redoa\\Desktop\\boi2\\media\\default.jpg', null=True, upload_to='Profile_Picture'),
        ),
    ]