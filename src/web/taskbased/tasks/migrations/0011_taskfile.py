# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 13:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import relativefilepathfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_auto_20160702_2041'),
        ('tasks', '0010_auto_20160614_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', relativefilepathfield.fields.RelativeFilePathField(max_length=1000, path=settings.DRAPO_TASKS_FILES_DIR, recursive=True)),
                ('content_type', models.CharField(default='application/octet-stream', max_length=1000)),
                ('participant', models.ForeignKey(default=None, help_text='None if this file is for all participants', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contests.AbstractParticipant')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='tasks.Task')),
            ],
        ),
    ]
