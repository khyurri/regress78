# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-07 17:29
from __future__ import unicode_literals

import commons.core
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170319_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to=commons.core.UploadTo('adv'), verbose_name='изображение')),
                ('event_date', models.DateTimeField(verbose_name='дата события')),
                ('event_week_day', models.TextField(verbose_name='день недели')),
                ('event_location', models.TextField(verbose_name='место события')),
            ],
            options={
                'verbose_name': 'баннер',
                'verbose_name_plural': 'баннеры',
            },
        ),
    ]