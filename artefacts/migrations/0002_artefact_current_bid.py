# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-16 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artefacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artefact',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
