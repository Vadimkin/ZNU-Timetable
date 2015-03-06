# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_auto_20150204_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='group',
        ),
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1423156887),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1423156887),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1423156887),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1423156887),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1423156887),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1423156887),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1423156887),
            preserve_default=True,
        ),
    ]
