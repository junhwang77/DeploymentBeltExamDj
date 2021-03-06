# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('travel_start', models.DateField(blank=True, null=True)),
                ('travel_end', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('planner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usertoplanner', to='login_reg.Users')),
                ('travel_id', models.ManyToManyField(related_name='usertotrip', to='login_reg.Users')),
            ],
            managers=[
                ('usermanager', django.db.models.manager.Manager()),
            ],
        ),
    ]
