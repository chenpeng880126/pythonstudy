# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='bpub_dat',
            new_name='bpub_date',
        ),
    ]