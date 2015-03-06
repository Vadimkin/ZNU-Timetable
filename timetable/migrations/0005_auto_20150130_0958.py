# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_auto_20150127_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audience',
            options={'ordering': ['campus', 'audience'], 'verbose_name': '\u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0456\u044f', 'verbose_name_plural': '\u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0456\u0457'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['course'], 'verbose_name': '\u0433\u0440\u0443\u043f\u0430', 'verbose_name_plural': '\u0433\u0440\u0443\u043f\u0438'},
        ),
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1422611906),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1422611906),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1422611906),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1422611906),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1422611906),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1422611906),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='date_end',
            field=models.DateField(default=datetime.date(2015, 5, 30), verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbd\xd0\xb5\xd1\x86\xd1\x8c \xd0\xbf\xd0\xb0\xd1\x80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='date_start',
            field=models.DateField(default=datetime.date(2015, 2, 2), verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd0\xb0\xd1\x82\xd0\xbe\xd0\xba \xd0\xbf\xd0\xb0\xd1\x80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1422611906),
            preserve_default=True,
        ),
    ]
