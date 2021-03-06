# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20160613_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractparticipant',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='abstractparticipant',
            name='is_disqualified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='abstractparticipant',
            name='is_visible_in_scoreboard',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='taskbasedcontest',
            name='tasks_grouping',
            field=models.CharField(choices=[('By categories', 'By categories'), ('One by one', 'One by one')], max_length=20, validators=[djchoices.choices.ChoicesValidator({'By categories': 'By categories', 'One by one': 'One by one'})]),
        ),
    ]
