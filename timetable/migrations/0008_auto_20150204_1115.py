# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_auto_20150201_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1423048486),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1423048486),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1423048486),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1423048486),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1423048486),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1423048486),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='audience',
            field=models.ForeignKey(default=40, verbose_name=b'\xd0\x90\xd1\x83\xd0\xb4\xd0\xb8\xd1\x82\xd0\xbe\xd1\x80\xd1\x96\xd1\x8f', to='timetable.Audience'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='free_trajectory',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x96\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0 \xd1\x82\xd1\x80\xd0\xb0\xd0\xb5\xd0\xba\xd1\x82\xd0\xbe\xd1\x80\xd1\x96\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1423048486),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='teacher',
            field=models.ForeignKey(default=50, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87', to='timetable.Teacher'),
            preserve_default=False,
        ),
    ]
