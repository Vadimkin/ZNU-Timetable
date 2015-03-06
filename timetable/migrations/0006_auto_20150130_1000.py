# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20150130_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1422612001),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1422612001),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1422612001),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1422612001),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1422612001),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1422612001),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='audience',
            field=models.ForeignKey(verbose_name=b'\xd0\x90\xd1\x83\xd0\xb4\xd0\xb8\xd1\x82\xd0\xbe\xd1\x80\xd1\x96\xd1\x8f', blank=True, to='timetable.Audience', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1422612001),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='teacher',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xb8\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87', blank=True, to='timetable.Teacher', null=True),
            preserve_default=True,
        ),
    ]
