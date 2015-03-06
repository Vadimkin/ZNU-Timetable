# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0011_auto_20150214_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='department',
            name='longitude',
        ),
        migrations.AddField(
            model_name='campus',
            name='latitude',
            field=models.FloatField(null=True, verbose_name=b'Latitude', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campus',
            name='longitude',
            field=models.FloatField(null=True, verbose_name=b'Longitude', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1423907074),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1423907074),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1423907074),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1423907074),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1423907074),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1423907074),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1423907074),
            preserve_default=True,
        ),
    ]
