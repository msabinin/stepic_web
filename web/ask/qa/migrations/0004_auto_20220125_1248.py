# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2022-01-25 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_remove_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]