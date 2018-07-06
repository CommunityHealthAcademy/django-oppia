# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 17:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oppia', '0010_move_userprofile'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, default=None, null=True)),
                ('can_upload', models.BooleanField(default=False)),
                ('job_title', models.TextField(blank=True, default=None, null=True)),
                ('organisation', models.TextField(blank=True, default=None, null=True)),
                ('phone_number', models.TextField(blank=True, default=None, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
