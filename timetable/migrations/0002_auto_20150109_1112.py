# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='period',
            field=models.ForeignKey(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81 \xd0\xbf\xd0\xb0\xd1\x80', to='timetable.Time', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1420801962.456048),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1420801962.455064),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1420801962.452101),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1420801962.453185),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1420801962.457052),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1420801962.454159),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1420801962.459657),
            preserve_default=True,
        ),
    ]
