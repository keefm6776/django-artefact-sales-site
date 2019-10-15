# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-13 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artefacts', '0003_auto_20190929_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=254)),
                ('full_name', models.CharField(default='', max_length=60)),
                ('street_Address1', models.CharField(default='', max_length=40)),
                ('street_Address2', models.CharField(default='', max_length=40)),
                ('town_or_city', models.CharField(default='', max_length=40)),
                ('county', models.CharField(default='', max_length=40)),
                ('country', models.CharField(default='', max_length=40)),
                ('postcode', models.CharField(default='', max_length=20)),
                ('phone_number', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='artefact',
            name='current_bid',
        ),
        migrations.AddField(
            model_name='bidhistory',
            name='artefact_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artefacts.Artefact'),
        ),
        migrations.AddField(
            model_name='bidhistory',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artefacts.Customer'),
        ),
    ]