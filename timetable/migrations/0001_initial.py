# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audience', models.TextField(verbose_name=b'\xd0\x90\xd1\x83\xd0\xb4\xd0\xb8\xd1\x82\xd0\xbe\xd1\x80\xd1\x96\xd1\x8f')),
                ('last_update', models.IntegerField(default=1425733235)),
            ],
            options={
                'ordering': ['campus', 'audience'],
                'verbose_name': '\u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0456\u044f',
                'verbose_name_plural': '\u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0456\u0457',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'', verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xbf\xd1\x83\xd1\x81', blank=True)),
                ('last_update', models.IntegerField(default=1425733235)),
                ('longitude', models.FloatField(null=True, verbose_name=b'Longitude', blank=True)),
                ('latitude', models.FloatField(null=True, verbose_name=b'Latitude', blank=True)),
            ],
            options={
                'verbose_name': '\u043a\u043e\u0440\u043f\u0443\u0441',
                'verbose_name_plural': '\u043a\u043e\u0440\u043f\u0443\u0441\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5\xd1\x82')),
                ('last_update', models.IntegerField(default=1425733235)),
            ],
            options={
                'verbose_name': '\u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442',
                'verbose_name_plural': '\u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb8')),
                ('course', models.IntegerField(default=1, choices=[(1, b'1 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (2, b'2 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (3, b'3 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (4, b'4 \xd0\xba\xd1\x83\xd1\x80\xd1\x81'), (5, b'5 \xd0\xba\xd1\x83\xd1\x80\xd1\x81')])),
                ('last_update', models.IntegerField(default=1425733235)),
                ('department', models.ForeignKey(verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5\xd1\x82', to='timetable.Department')),
            ],
            options={
                'ordering': ['course'],
                'verbose_name': '\u0433\u0440\u0443\u043f\u0430',
                'verbose_name_plural': '\u0433\u0440\u0443\u043f\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbc\xd0\xb5\xd1\x82')),
                ('last_update', models.IntegerField(default=1425733235)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u043f\u0440\u0435\u0434\u043c\u0435\u0442',
                'verbose_name_plural': '\u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name=b"\xd0\x86\xd0\xbc'\xd1\x8f \xd1\x82\xd0\xb0 \xd0\xbf\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5 \xd0\xb2\xd0\xb8\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb0")),
                ('last_update', models.IntegerField(default=1425733235)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u0432\u0438\u043a\u043b\u0430\u0434\u0430\u0447',
                'verbose_name_plural': '\u0432\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0456',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(max_length=1)),
                ('time_start', models.TimeField(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81 \xd0\xbf\xd0\xbe\xd1\x87\xd0\xb0\xd1\x82\xd0\xba\xd1\x83 \xd0\xbf\xd0\xb0\xd1\x80\xd0\xb8')),
                ('time_end', models.TimeField(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81 \xd0\xba\xd1\x96\xd0\xbd\xd1\x86\xd1\x8f \xd0\xbf\xd0\xb0\xd1\x80\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u0447\u0430\u0441',
                'verbose_name_plural': '\u0433\u043e\u0434\u0438\u043d\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subgroup', models.IntegerField(default=0, max_length=1, verbose_name=b'\xd0\x9f\xd1\x96\xd0\xb4\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0', choices=[(0, b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0'), (1, b'1 \xd0\xbf\xd1\x96\xd0\xb4\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0'), (2, b'2 \xd0\xbf\xd1\x96\xd0\xb4\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0'), (3, b'3 \xd0\xbf\xd1\x96\xd0\xb4\xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0')])),
                ('day', models.IntegerField(default=0, max_length=1, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c', choices=[(0, b'\xd0\x9f\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd1\x96\xd0\xbb\xd0\xbe\xd0\xba'), (1, b'\xd0\x92\xd1\x96\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xba'), (2, b'\xd0\xa1\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0'), (3, b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80'), (4, b"\xd0\x9f'\xd1\x8f\xd1\x82\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8f"), (5, b'\xd0\xa1\xd1\x83\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0'), (6, b'\xd0\x9d\xd0\xb5\xd0\xb4\xd1\x96\xd0\xbb\xd1\x8f')])),
                ('periodicity', models.IntegerField(default=0, max_length=1, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd1\x96\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x87\xd0\xbd\xd1\x96\xd1\x81\xd1\x82\xd1\x8c', choices=[(0, b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb6\xd0\xb4\xd0\xb8'), (1, b'\xd0\xa7\xd0\xb8\xd1\x81\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba'), (2, b'\xd0\x97\xd0\xbd\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb8\xd0\xba')])),
                ('date_start', models.DateField(default=datetime.date(2015, 2, 2), verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd0\xb0\xd1\x82\xd0\xbe\xd0\xba \xd0\xbf\xd0\xb0\xd1\x80')),
                ('date_end', models.DateField(default=datetime.date(2015, 5, 30), verbose_name=b'\xd0\x9a\xd1\x96\xd0\xbd\xd0\xb5\xd1\x86\xd1\x8c \xd0\xbf\xd0\xb0\xd1\x80')),
                ('lesson_type', models.IntegerField(default=0, max_length=1, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbc\xd0\xb5\xd1\x82\xd1\x83', choices=[(0, b'\xd0\x9d\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xbe'), (1, b'\xd0\x9b\xd0\xb5\xd0\xba\xd1\x86\xd1\x96\xd1\x8f'), (2, b'\xd0\xa1\xd0\xb5\xd0\xbc\xd1\x96\xd0\xbd\xd0\xb0\xd1\x80'), (3, b'\xd0\x9b\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd0\xbd\xd0\xb0'), (4, b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x81\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x86\xd1\x96\xd1\x8f'), (5, b'\xd0\x95\xd0\xba\xd0\xb7\xd0\xb0\xd0\xbc\xd0\xb5\xd0\xbd')])),
                ('free_trajectory', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x96\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0 \xd1\x82\xd1\x80\xd0\xb0\xd0\xb5\xd0\xba\xd1\x82\xd0\xbe\xd1\x80\xd1\x96\xd1\x8f')),
                ('last_update', models.IntegerField(default=1425733235)),
                ('audience', models.ForeignKey(verbose_name=b'\xd0\x90\xd1\x83\xd0\xb4\xd0\xb8\xd1\x82\xd0\xbe\xd1\x80\xd1\x96\xd1\x8f', to='timetable.Audience')),
                ('group', models.ManyToManyField(to='timetable.Group', verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0')),
                ('lesson', models.ForeignKey(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbc\xd0\xb5\xd1\x82', to='timetable.Lesson')),
                ('period', models.ForeignKey(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81 \xd0\xbf\xd0\xb0\xd1\x80', to='timetable.Time', null=True)),
                ('teacher', models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xb8\xd0\xba\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87', to='timetable.Teacher')),
            ],
            options={
                'verbose_name': '\u0440\u043e\u0437\u043a\u043b\u0430\u0434',
                'verbose_name_plural': '\u0440\u043e\u0437\u043a\u043b\u0430\u0434\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='audience',
            name='campus',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xbf\xd1\x83\xd1\x81', to='timetable.Campus'),
            preserve_default=True,
        ),
    ]
