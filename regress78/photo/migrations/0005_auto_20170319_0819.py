# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-19 08:19
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20170219_1004'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='photoalbumtree',
            managers=[
                ('published_items', django.db.models.manager.Manager()),
            ],
        ),
    ]