# -*- coding: utf-8 -*-
# !/usr/bin/env python
import glob
import re
import os
import sys
import xlrd
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/settings.py')
os.environ['DJANGO_SETTINGS_MODULE'] = 'znu.settings'
django.setup()

from timetable.models import Timetable, Group, Lesson, Audience, Teacher

__author__ = 'vadim'

week_days = {
    u"понеділок": 0,
    u"вівторок": 1,
    u"середа": 2,
    u"четвер": 3,
    u"четверг": 3,
    u"п'ятниця": 4,
    u"пятниця": 4,
    u'п’ятниця': 4,
    u"субота": 5
}

numerator = {
    u"чисельник": 1,
    u"знаменник": 2,
    u"знаменик": 2
}

lesson_type = {
    u"лекція": 1,
    u"семінар": 2,
    u"cемінар": 2,
    u"лабораторна": 3,
    u"практика": 3,
    u"пр.": 3,
    u"1": 1,
    u"2": 2,
    u"3": 3
}


def replace_all(repls, str):
    # return re.sub('|'.join(repls.keys()), lambda k: repls[k.group(0)], str)
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str)

for filename in glob.glob(os.path.dirname(os.path.abspath(__file__)) + '/data/new/*.xls'):
    print("Open {0}".format(filename))

    rb = xlrd.open_workbook(filename, formatting_info=False)
    sheet = rb.sheet_by_index(0)

    main_info = {}
    main_info['faculty'] = sheet.row_values(1)[0]
    main_info['group'] = sheet.row_values(1)[1]
    main_info['course'] = int(sheet.row_values(1)[2])

    main_info['faculty'] = 3

    # if group not found, then create it
    group, created = Group.objects.get_or_create(department_id=main_info['faculty'], name=main_info['group'],
                                                 course=main_info['course'])
    main_info['group_id'] = group.id

    print(main_info['group_id'])

    for rownum in range(3, sheet.nrows):
        row = sheet.row_values(rownum)

        lesson = {}

        print(row[0].strip())
        print(row[4].strip())

        try:
            lesson['week_day'] = week_days[row[0].strip().lower()]
        except KeyError:
            continue
        try:
            lesson['time'] = int(row[1])
        except (UnicodeEncodeError, ValueError):
            continue

        lesson['periodicity'] = 0 if row[2] == "" else numerator[row[2].lower().strip()]
        lesson['type'] = 0 if row[3] == "" else lesson_type[row[3].lower()]
        lesson['name'] = row[4].strip()
        lesson['teacher'] = u"—" if row[5] == "" else row[5].strip()

        replace_all({"доц.": "", "ст.викл.": "", "проф.": ""}, lesson['teacher'])
        lesson['teacher'] = lesson['teacher'].strip()

        try:
            lesson['audience'] = u"—" if row[6] == "" else int(row[6])
        except UnicodeEncodeError:
            lesson['audience'] = u"—" if row[6] == "" else row[6]

        lesson['campus'] = 9 if row[7] == "" else int(row[7])
        lesson['subgroup'] = 0 if row[8] == "" else int(row[8])
        lesson['free_trajectory'] = 0 if row[9] == "" else int(row[9])

        lesson_object = Lesson.objects.get_or_create(name=lesson['name'])[0]
        lesson['name_id'] = lesson_object.id

        audience_object = Audience.objects.get_or_create(campus_id=lesson['campus'], audience=lesson['audience'])[0]
        lesson['audience_id'] = audience_object.id

        teacher_object = Teacher.objects.get_or_create(name=lesson['teacher'])[0]
        lesson['teacher_id'] = teacher_object.id

        timetable = Timetable.objects.get_or_create(lesson_id=lesson['name_id'], day=lesson['week_day'],
                                                    audience_id=lesson['audience_id'],
                                                    periodicity=lesson['periodicity'], lesson_type=lesson['type'],
                                                    teacher_id=lesson['teacher_id'], period_id=lesson['time'],
                                                    subgroup=lesson['subgroup'],
                                                    free_trajectory=lesson['free_trajectory'])[0]

        timetable.group.add(main_info['group_id'])