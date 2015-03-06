# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20150109_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='subgroup',
            field=models.IntegerField(default=0, max_length=1, verbose_name=b'\xd0\x9f\xd1\x96\xd0\xb4\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0', choices=[(0, b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0'), (1, b'1 \xd0\xbf\xd1\x96\xd0\xb4\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0'), (2, b'2 \xd0\xbf\xd1\x96\xd0\xb4\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0'), (3, b'3 \xd0\xbf\xd1\x96\xd0\xb4\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1421225136.616836),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1421225136.616355),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1421225136.614532),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1421225136.61532),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1421225136.618018),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1421225136.615908),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.IntegerField(default=0, max_length=1, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c', choices=[(0, b'\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd1\x96\xd0\xbb\xd0\xbe\xd0\xba'), (1, b'\xd0\x92\xd1\x96\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xba'), (2, b'\xd0\xa1\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0'), (3, b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80'), (4, b"\xd0\x9f'\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8f"), (5, b'\xd0\xa1\xd1\x83\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0'), (6, b'\xd0\x9d\xd0\xb5\xd0\xb4\xd1\x96\xd0\xbb\xd1\x8f')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1421225136.620407),
            preserve_default=True,
        ),
    ]
