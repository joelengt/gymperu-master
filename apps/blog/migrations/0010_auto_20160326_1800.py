# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(help_text='No llenar, este campo se llena solo'),
        ),
    ]