# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_auto_20150130_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['name'], 'verbose_name': '\u043f\u0440\u0435\u0434\u043c\u0435\u0442', 'verbose_name_plural': '\u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['name'], 'verbose_name': '\u0432\u0438\u043a\u043b\u0430\u0434\u0430\u0447', 'verbose_name_plural': '\u0432\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0456'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name': '\u0447\u0430\u0441', 'verbose_name_plural': '\u0433\u043e\u0434\u0438\u043d\u0438'},
        ),
        migrations.AddField(
            model_name='timetable',
            name='free_trajectory',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1422802593),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1422802593),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1422802593),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1422802593),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1422802593),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1422802593),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1422802593),
            preserve_default=True,
        ),
    ]
