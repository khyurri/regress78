# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-19 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoalbumtree',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
