# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20150114_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.IntegerField(default=1, choices=[(1, b'1 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (2, b'2 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (3, b'3 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (4, b'4 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (5, b'5 \xd0\xba\xd1\x83\xd1\x80\xd1\x81')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1422361777),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1422361777),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1422361777),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1422361777),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1422361777),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1422361777),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1422361777),
            preserve_default=True,
        ),
    ]
