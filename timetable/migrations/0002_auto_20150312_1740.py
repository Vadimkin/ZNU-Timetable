# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbf\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xba\xd0\xb8', blank=True)),
                ('contacts', models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8', blank=True)),
                ('ip', models.IPAddressField(verbose_name=b'IP')),
                ('fixed', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd0\xb8\xd1\x80\xd1\x96\xd1\x88\xd0\xb5\xd0\xbd\xd0\xbe')),
                ('last_update', models.IntegerField(default=1426182046, verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81 \xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8c\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb4\xd0\xbe\xd0\xb4\xd0\xb0\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f')),
                ('group', models.ForeignKey(verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0', to='timetable.Group')),
                ('timetable', models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xb7\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4', blank=True, to='timetable.Timetable', null=True)),
            ],
            options={
                'verbose_name': '\u0431\u0430\u0433-\u0440\u0435\u043f\u043e\u0440\u0442',
                'verbose_name_plural': '\u0431\u0430\u0433-\u0440\u0435\u043f\u043e\u0440\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='audience',
            name='last_update',
            field=models.IntegerField(default=1426182046),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campus',
            name='last_update',
            field=models.IntegerField(default=1426182046),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='department',
            name='last_update',
            field=models.IntegerField(default=1426182046),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='last_update',
            field=models.IntegerField(default=1426182046),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='last_update',
            field=models.IntegerField(default=1426182046),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.IntegerField(default=1426182046),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='last_update',
            field=models.IntegerField(default=1426182046),
            preserve_default=True,
        ),
    ]
