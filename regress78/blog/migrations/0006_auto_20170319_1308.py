# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-19 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170319_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogitem',
            name='topic_type',
            field=models.IntegerField(choices=[(0, 'Топик в блоге'), (1, 'Событие')], default=0, verbose_name='тип записи'),
        ),
    ]